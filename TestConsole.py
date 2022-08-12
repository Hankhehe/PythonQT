from AtheNACWebAPI import AthenacWebAPILibry
import base64

ProbeID = 10925416137
netName = 'VLAN 118'
VLANId = 118
manageIP = '192.168.118.171/24'
gatewayIP = '192.168.118.254'

option = AthenacWebAPILibry('http://192.168.21.180:8000','admin',base64.b64encode('admin'.encode('UTF-8')))
ID = option.GetNetworkInfoByName('VLAN 118')
option.AddNetwork(ProbeID=ProbeID,NetworkName=netName,VLANID=VLANId)
option.AddRange(mIP=manageIP,gwIP=gatewayIP,NetworkName=netName)
pass

