
from PyQt5 import QtCore, QtGui, QtWidgets
from pxpowershell_engine import pxpowershell
import re


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(528, 445)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.process = pxpowershell()
        self.process.start_process()

        self.label_vcenter = QtWidgets.QLabel(self.centralwidget)
        self.label_vcenter.setGeometry(QtCore.QRect(30, 10, 51, 31))
        self.label_vcenter.setObjectName("label_vcenter")
        self.lineEdit_vcenter = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_vcenter.setGeometry(QtCore.QRect(110, 10, 211, 31))
        self.lineEdit_vcenter.setObjectName("lineEdit_vcenter")
        self.lineEdit_vcenter.setText('192.168.10.212')
        
        self.label_account = QtWidgets.QLabel(self.centralwidget)
        self.label_account.setGeometry(QtCore.QRect(30, 50, 47, 31))
        self.label_account.setObjectName("label_account")
        self.lineEdit_account = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_account.setGeometry(QtCore.QRect(110, 50, 211, 31))
        self.lineEdit_account.setObjectName("lineEdit_account")

        self.label_pwd = QtWidgets.QLabel(self.centralwidget)
        self.label_pwd.setGeometry(QtCore.QRect(30, 90, 47, 31))
        self.label_pwd.setObjectName("label_pwd")
        self.lineEdit_pwd = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_pwd.setGeometry(QtCore.QRect(110, 90, 211, 31))
        self.lineEdit_pwd.setObjectName("lineEdit_pwd")
        self.lineEdit_pwd.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

        self.label_queryMAC = QtWidgets.QLabel(self.centralwidget)
        self.label_queryMAC.setGeometry(QtCore.QRect(30, 130, 51, 31))
        self.label_queryMAC.setObjectName("label_queryMAC")
        self.lineEdit_queryMAC = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_queryMAC.setGeometry(QtCore.QRect(110, 130, 211, 31))
        self.lineEdit_queryMAC.setObjectName("lineEdit_queryMAC")
        
        self.button_login = QtWidgets.QPushButton(self.centralwidget)
        self.button_login.setGeometry(QtCore.QRect(330, 90, 75, 31))
        self.button_login.setObjectName("button_login")

        self.button_send = QtWidgets.QPushButton(self.centralwidget)
        self.button_send.setGeometry(QtCore.QRect(330, 130, 75, 31))
        self.button_send.setObjectName("button_Send")

        self.textBrowser_disply = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_disply.setGeometry(QtCore.QRect(10, 281, 501, 151))
        self.textBrowser_disply.setObjectName("textBrowser_disply")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def QueryMACbyVMCLI(self) -> None:
        queryMAC = self.lineEdit_queryMAC.text()
        queryMAC = f'"{self.ConvertMACbyPunctuation(queryMAC,":")}"'
        if queryMAC :
            result = self.process.run('Get-VM | Get-NetworkAdapter | Where {$_.MacAddress -eq '+queryMAC+'} | Select-Object Parent,Name,MacAddress')
            self.textBrowser_disply.setText(str(result.decode('utf8','ignore')))
        else : 
            self.textBrowser_disply.setText('Query Fail')

    def LogintovCenterbyVMCLI(self) -> None:
        vcenter = self.lineEdit_vcenter.text()
        accounttext = self.lineEdit_account.text()
        pwd = self.lineEdit_pwd.text()
        result = self.process.run(f'Connect-VIServer -Server {vcenter} -Protocol https -User {accounttext} -Password {pwd}')
        self.textBrowser_disply.setText(str(result.decode('utf8','ignore')))

    def ConvertMACbyPunctuation(self,mac:str ,Punctuation:str)->str | None :
        '''Covert to example aaaa.aaaa or aa:aa:aa:aa or aa-aa-aa-aa '''
        mac = ''.join(re.split(':|-|\.',mac)).upper()
        if len(mac) != 12 : return
        if Punctuation == '-' or Punctuation == ':' : 
            return Punctuation.join(re.findall(r'.{2}',mac)).lower()
        elif Punctuation == '.' :
            return  Punctuation.join(re.findall(r'.{4}',mac)).lower()
        else : return
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Query VM by MAC"))
        self.button_send.setText(_translate("MainWindow", "查詢"))
        self.button_login.setText(_translate("MainWindow", "登入"))
        self.label_account.setText(_translate("MainWindow", "VM 帳號"))
        self.label_pwd.setText(_translate("MainWindow", "VM 密碼"))
        self.label_queryMAC.setText(_translate("MainWindow", "查詢 MAC"))
        self.label_vcenter.setText(_translate("MainWindow", "vCenter IP"))
        self.button_send.clicked.connect(self.QueryMACbyVMCLI)
        self.button_login.clicked.connect(self.LogintovCenterbyVMCLI)
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
