from AtheNACWebAPI import AthenacWebAPILibry
import base64

option = AthenacWebAPILibry('http://192.168.21.180:8000','admin',base64.b64encode('admin'.encode('UTF-8')))
# NetworkID = option.GetNetworkInfoByName('VLAN 21')
option.AddRange(mIP='192.168.98.0/23',gwIP='192.168.99.254',NetworkName='VLAN 21')
pass

