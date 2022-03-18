from asyncore import read
from pxpowershell_engine import pxpowershell
import tkinter as tk



window = tk.Tk()
window.title('Query VM info by MAC')
window.geometry('800x400')


div3 = tk.Frame(window,  width=200 , height=200)
div3.grid(column=1, row=1, padx=5, pady=5, sticky='nswe')
sendbutton = tk.Button(div3, text='Send', font=('Arial', 12))
sendbutton.grid(column=0, row=0)


window.mainloop()

input()



x = pxpowershell()
x.start_process()
x.run('Connect-VIServer -Server 192.168.10.212 -Protocol https -User pixis.com\\Hank -Password Pixis1aB@')
result = x.run('Get-VM | Get-NetworkAdapter | Where {$_.MacAddress -eq "00:50:56:ae:fe:99"} | Select-Object Parent,Name,MacAddress')
# result = x.run('dir')
print(str(result.decode('utf8','ignore')))
x.stop_process()
