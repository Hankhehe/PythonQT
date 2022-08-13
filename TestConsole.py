from AtheNACWebAPI import AthenacWebAPILibry
import base64,csv

Datas = list()
with open('IPRange.csv',newline='') as f :
    Rows = csv.reader(f)
    for Row in Rows:
        Datas.append(Row)
del Datas[0]
for Data in Datas:
    option = AthenacWebAPILibry('http://192.168.21.180:8000','admin',base64.b64encode('admin'.encode('UTF-8')))
    option.AddNetwork(ProbeID=Data[0],NetworkName=Data[1],VLANID=Data[2])
    option.AddRange(mIP=Data[3],gwIP=Data[4],NetworkName=Data[1])
pass

