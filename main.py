from pxpowershell_engine import pxpowershell

x = pxpowershell()
x.start_process()
x.run('Connect-VIServer -Server 192.168.10.212 -Protocol https -User pixis.com\\Hank -Password Pixis1aB@')
result = x.run('Get-VM | Get-NetworkAdapter | Where {$_.MacAddress -eq "00:50:56:AE:FE:99"} | Select-Object Parent,Name,MacAddress')
# result = x.run('dir')
print(str(result.decode('utf8','ignore')))
x.stop_process()
