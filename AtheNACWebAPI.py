from email.header import Header
import requests,json,ipaddress
from urllib import parse

class AthenacWebAPILibry :
    def __init__(self,ServerIP:str,Account:str,Pwd:bytes) -> None:
        self.ServerIP = ServerIP
        self.Account = Account
        self.Pwd = Pwd
        self.Token = ''
        self.FreshToken = ''
        self.retriesnum = 3
        self.GetLoginToken()
    
    def GetLoginToken(self)-> None:
        Path = '/api/connect/token'
        Header = {'Content-Type': 'application/x-www-form-urlencoded' }
        FormData = {"grant_type": 'password','scope':'offline_access', 'username': self.Account, 'password': self.Pwd} 
        Data = parse.urlencode(FormData)
        r = requests.post(self.ServerIP+Path,headers=Header,data=Data,verify=False)
        r = json.loads(r.text)
        self.Token = 'Bearer '+ r['access_token']
        self.FreshToken ='Bearer ' + r['refresh_token']
    
    def AddDNSByNetwork(self,NetworkName:str,DNS1:str,DNS2:str,LeaseMinuteTime:int)-> None:
        NetWorkerID = self.GetNetworkInfoByName(NetworkName=NetworkName)
        Path = f'/api/Networks/{NetWorkerID}/DHCPv4Setting'
        Header = {'Authorization':self.Token,'Content-type': 'application/json'}
        Data = {
                "DNS1": DNS1,
                "DNS2": DNS2,
                "LeaseTimeInMinute": LeaseMinuteTime,
                "DhcpProxyServer": "",
                "VlanInformation": "",
                "AvayaOption": "",
                "CallServerInformation": ""
                }
        requests.put(self.ServerIP+Path,headers=Header,data=json.dumps(Data),verify=False)

    def AddDHCPool(self,RangeName:str,StartIP:str,EndIP:str) -> None:
        RangeID = self.GetIPRangeInfoByName(RangeName=RangeName)
        Path = '/api/DhcpPools'
        Header = {'Authorization':self.Token,'Content-type': 'application/json'}
        Data ={
                # "Id": 0,
                "IpRangeId": RangeID,
                "StartIp": StartIP,
                "EndIp": EndIP,
                "PoolType": 0,
                "EnableStaticIpBlock": False,
                "EnableOnlyAssignDHCPStaticIPPolicy": False
                }
        requests.post(self.ServerIP+Path,headers=Header,data=json.dumps(Data),verify=False)

    def AddRange(self,mIP:str,gwIP:str,NetworkName:str) -> None :
        manageIP = str(mIP.split('/')[0])
        networkeIP = str(ipaddress.ip_interface(mIP).network)
        IPrange = ipaddress.IPv4Network(networkeIP)
        submask = str(IPrange.netmask)
        first,last = str(IPrange[1]),str(IPrange[-2])
        NetworkerId = self.GetNetworkInfoByName(NetworkName=NetworkName)
        Path = '/api/IpRanges/V4'
        Header = {'Authorization':self.Token,'Content-type': 'application/json'}
        Data = {"NetworkId": NetworkerId
        ,"Name": networkeIP
        ,"ManagementIp": manageIP
        ,"StartIp": first
        ,"EndIp": last
        ,"GatewayIp": gwIP
        ,"SubnetMask": submask}
        requests.post(self.ServerIP+Path,headers=Header,data=json.dumps(Data),verify=False)

    def AddNetwork(self,ProbeID:int,NetworkName,VLANID:int) -> None :
        Path = '/api/Networks/Create'
        Header = {'Authorization':self.Token,'Content-type': 'application/json'}
        Data = {"PixisProbeId": ProbeID,"NetworkName": NetworkName,"VlanId": VLANID}
        requests.post(self.ServerIP+Path,headers=Header,data=json.dumps(Data),verify=False)

    def GetIPRangeInfoByName(self,RangeName:str) -> int | None:
        Path ='/api/IpRanges/V4'
        Header = {'Authorization':self.Token,'Content-type': 'application/json'}
        r = requests.get(self.ServerIP+Path,headers=Header,verify=False)
        r = json.loads(r.text)
        for i in r:
            if i['Name'] == RangeName:
                return i['Id']

    def GetNetworkInfoByName(self,NetworkName:str)-> int | None :
        r = None
        Path = '/api/Networks/Query'
        Header = {'Authorization':self.Token,'Content-type': 'application/json'}
        Data = {'take':0}
        r = requests.post(self.ServerIP+Path,headers=Header,data=json.dumps(Data),verify=False)
        r = json.loads(r.text)['Data']
        for i in r :
            if i['NetworkName'] == NetworkName :
                return i['NetworkId']
            

    