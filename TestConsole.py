from AtheNACWebAPI import AthenacWebAPILibry
import base64

option = AthenacWebAPILibry('http://192.168.21.180:8000','admin',base64.b64encode('admin'.encode('UTF-8')))
option.GetNetworkInfoByName('VLAN21')

