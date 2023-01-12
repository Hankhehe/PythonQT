from AtheNACWebAPI import AthenacWebAPILibry
import base64,csv,paramiko

def RestartProbe() -> None:
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname= '192.168.21.171',username= 'root', password='1111')
        aa,bb,cc =  ssh.exec_command('top -b -o +%MEM | head -n 6')
        result = bb.readlines()
        print(''.join(bb.readlines()))
        # self.plainTextEdit_Result_Display.setPlainText('Finished reboot')
        pass
    except Exception as e :
        print(str(e))

if __name__ == '__main__':
    RestartProbe()
    pass
