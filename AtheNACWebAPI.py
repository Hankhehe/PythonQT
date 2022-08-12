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
    
    def AddRange(self,mIP:str,gwIP:str,NetworkName:str) -> None :
        #需要提供 Networke ID
        #{"NetworkId": "14","Name": "192.168.99.X","ManagementIp": "192.168.99.89","StartIp": "192.168.99.1","EndIp": "192.168.99.254","GatewayIp": "192.168.99.254","SubnetMask": "255.255.255.0"}
        IPrange = ipaddress.IPv4Network(mIP)
        manageIP = str(mIP.split('/')[0])
        submask = str(IPrange.netmask)
        rangeName,first,last =str(IPrange[0]), str(IPrange[1]),str(IPrange[-2])
        NetworkerId = self.GetNetworkInfoByName(NetworkName=NetworkName)
        pass
        Path = '/api/IpRanges/V4'
        Header = {'Authorization':self.Token,'Content-type': 'application/json'}
        
        Data = {}

    def AddNetwork(self) -> None :
        #需要提供 Probe ID
        #{"PixisProbeId": 10925416137,"NetworkName": "VLAnN999","VlanId": 999}
        Path = '/api/Networks/Create'

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
            

    