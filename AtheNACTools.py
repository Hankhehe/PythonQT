import json5,codecs
from PyQt5 import QtCore, QtGui, QtWidgets
from pxpowershell_engine import pxpowershell

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1079, 828)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 1051, 781))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_DBConfig = QtWidgets.QWidget()
        self.tab_DBConfig.setObjectName("tab_DBConfig")
        self.pushButton_Change_DBConfig = QtWidgets.QPushButton(self.tab_DBConfig)
        self.pushButton_Change_DBConfig.setGeometry(QtCore.QRect(350, 490, 75, 23))
        self.pushButton_Change_DBConfig.setCheckable(False)
        self.pushButton_Change_DBConfig.setObjectName("pushButton_Change_DBConfig")
        self.label_ConfigPath_DBConfig = QtWidgets.QLabel(self.tab_DBConfig)
        self.label_ConfigPath_DBConfig.setGeometry(QtCore.QRect(120, 30, 61, 16))
        self.label_ConfigPath_DBConfig.setObjectName("label_ConfigPath_DBConfig")
        self.label_Value_DBConfig = QtWidgets.QLabel(self.tab_DBConfig)
        self.label_Value_DBConfig.setGeometry(QtCore.QRect(420, 30, 81, 16))
        self.label_Value_DBConfig.setObjectName("label_Value_DBConfig")
        self.lineEdit_ConfigPath_DBConfig_Web = QtWidgets.QLineEdit(self.tab_DBConfig)
        self.lineEdit_ConfigPath_DBConfig_Web.setGeometry(QtCore.QRect(120, 70, 281, 31))
        self.lineEdit_ConfigPath_DBConfig_Web.setObjectName("lineEdit_ConfigPath_DBConfig_Web")
        self.label_Web_DBConfig = QtWidgets.QLabel(self.tab_DBConfig)
        self.label_Web_DBConfig.setGeometry(QtCore.QRect(10, 70, 47, 12))
        self.label_Web_DBConfig.setObjectName("label_Web_DBConfig")
        self.label_CoreService_DBConfig = QtWidgets.QLabel(self.tab_DBConfig)
        self.label_CoreService_DBConfig.setGeometry(QtCore.QRect(10, 170, 81, 16))
        self.label_CoreService_DBConfig.setObjectName("label_CoreService_DBConfig")
        self.label_Radius_DBConfig = QtWidgets.QLabel(self.tab_DBConfig)
        self.label_Radius_DBConfig.setGeometry(QtCore.QRect(10, 280, 47, 12))
        self.label_Radius_DBConfig.setObjectName("label_Radius_DBConfig")
        self.lineEdit_ConfigPath_DBConfig_CoreService = QtWidgets.QLineEdit(self.tab_DBConfig)
        self.lineEdit_ConfigPath_DBConfig_CoreService.setGeometry(QtCore.QRect(120, 170, 281, 31))
        self.lineEdit_ConfigPath_DBConfig_CoreService.setObjectName("lineEdit_ConfigPath_DBConfig_CoreService")
        self.lineEdit_ConfigPath_DBConfig_Radius = QtWidgets.QLineEdit(self.tab_DBConfig)
        self.lineEdit_ConfigPath_DBConfig_Radius.setGeometry(QtCore.QRect(120, 270, 281, 31))
        self.lineEdit_ConfigPath_DBConfig_Radius.setObjectName("lineEdit_ConfigPath_DBConfig_Radius")
        self.pushButton_Query_DBConfig = QtWidgets.QPushButton(self.tab_DBConfig)
        self.pushButton_Query_DBConfig.setGeometry(QtCore.QRect(940, 340, 101, 21))
        self.pushButton_Query_DBConfig.setObjectName("pushButton_Query_DBConfig")
        self.lineEdit_SQLIP_DBConfig = QtWidgets.QLineEdit(self.tab_DBConfig)
        self.lineEdit_SQLIP_DBConfig.setGeometry(QtCore.QRect(10, 490, 91, 21))
        self.lineEdit_SQLIP_DBConfig.setText("")
        self.lineEdit_SQLIP_DBConfig.setObjectName("lineEdit_SQLIP_DBConfig")
        self.label_SQLIP_DBConfig = QtWidgets.QLabel(self.tab_DBConfig)
        self.label_SQLIP_DBConfig.setGeometry(QtCore.QRect(10, 470, 47, 12))
        self.label_SQLIP_DBConfig.setObjectName("label_SQLIP_DBConfig")
        self.label_SQLAccount_DBConfig = QtWidgets.QLabel(self.tab_DBConfig)
        self.label_SQLAccount_DBConfig.setGeometry(QtCore.QRect(110, 470, 81, 16))
        self.label_SQLAccount_DBConfig.setObjectName("label_SQLAccount_DBConfig")
        self.lineEdit_SQLAccount_DBConfig = QtWidgets.QLineEdit(self.tab_DBConfig)
        self.lineEdit_SQLAccount_DBConfig.setGeometry(QtCore.QRect(110, 490, 91, 21))
        self.lineEdit_SQLAccount_DBConfig.setObjectName("lineEdit_SQLAccount_DBConfig")
        self.pushButton_RestartService_DBConfig = QtWidgets.QPushButton(self.tab_DBConfig)
        self.pushButton_RestartService_DBConfig.setGeometry(QtCore.QRect(430, 490, 91, 23))
        self.pushButton_RestartService_DBConfig.setObjectName("pushButton_RestartService_DBConfig")
        self.lineEdit_SQLPWD_DBConfig = QtWidgets.QLineEdit(self.tab_DBConfig)
        self.lineEdit_SQLPWD_DBConfig.setGeometry(QtCore.QRect(220, 490, 113, 20))
        self.lineEdit_SQLPWD_DBConfig.setObjectName("lineEdit_SQLPWD_DBConfig")
        self.label_SQLPWD_DBConfig = QtWidgets.QLabel(self.tab_DBConfig)
        self.label_SQLPWD_DBConfig.setGeometry(QtCore.QRect(220, 470, 71, 16))
        self.label_SQLPWD_DBConfig.setObjectName("label_SQLPWD_DBConfig")
        self.plainTextEdit_Value_DBConfig = QtWidgets.QPlainTextEdit(self.tab_DBConfig)
        self.plainTextEdit_Value_DBConfig.setGeometry(QtCore.QRect(420, 70, 621, 261))
        self.plainTextEdit_Value_DBConfig.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.plainTextEdit_Value_DBConfig.setReadOnly(True)
        self.plainTextEdit_Value_DBConfig.setPlainText("")
        self.plainTextEdit_Value_DBConfig.setCenterOnScroll(False)
        self.plainTextEdit_Value_DBConfig.setObjectName("plainTextEdit_Value_DBConfig")
        self.tabWidget.addTab(self.tab_DBConfig, "")
        self.tab_Server_SSL = QtWidgets.QWidget()
        self.tab_Server_SSL.setObjectName("tab_Server_SSL")
        self.label_Value_ServerSSL = QtWidgets.QLabel(self.tab_Server_SSL)
        self.label_Value_ServerSSL.setGeometry(QtCore.QRect(450, 30, 81, 16))
        self.label_Value_ServerSSL.setObjectName("label_Value_ServerSSL")
        self.label_ConfigPath_ServerSSL = QtWidgets.QLabel(self.tab_Server_SSL)
        self.label_ConfigPath_ServerSSL.setGeometry(QtCore.QRect(120, 30, 61, 16))
        self.label_ConfigPath_ServerSSL.setObjectName("label_ConfigPath_ServerSSL")
        self.lineEdit_ConfigPath_ServerSSL_Web = QtWidgets.QLineEdit(self.tab_Server_SSL)
        self.lineEdit_ConfigPath_ServerSSL_Web.setGeometry(QtCore.QRect(120, 70, 281, 31))
        self.lineEdit_ConfigPath_ServerSSL_Web.setObjectName("lineEdit_ConfigPath_ServerSSL_Web")
        self.label_Web_ServerSSL = QtWidgets.QLabel(self.tab_Server_SSL)
        self.label_Web_ServerSSL.setGeometry(QtCore.QRect(10, 70, 47, 12))
        self.label_Web_ServerSSL.setObjectName("label_Web_ServerSSL")
        self.label_CoreService_ServerSSL = QtWidgets.QLabel(self.tab_Server_SSL)
        self.label_CoreService_ServerSSL.setGeometry(QtCore.QRect(10, 170, 81, 16))
        self.label_CoreService_ServerSSL.setObjectName("label_CoreService_ServerSSL")
        self.lineEdit_ConfigPath_ServerSSL_CoreService = QtWidgets.QLineEdit(self.tab_Server_SSL)
        self.lineEdit_ConfigPath_ServerSSL_CoreService.setGeometry(QtCore.QRect(120, 170, 281, 31))
        self.lineEdit_ConfigPath_ServerSSL_CoreService.setObjectName("lineEdit_ConfigPath_ServerSSL_CoreService")
        self.label_Enable_ServerSSL = QtWidgets.QLabel(self.tab_Server_SSL)
        self.label_Enable_ServerSSL.setGeometry(QtCore.QRect(10, 270, 47, 12))
        self.label_Enable_ServerSSL.setObjectName("label_Enable_ServerSSL")
        self.pushButton_RestartService_ServerSSL = QtWidgets.QPushButton(self.tab_Server_SSL)
        self.pushButton_RestartService_ServerSSL.setGeometry(QtCore.QRect(190, 290, 91, 23))
        self.pushButton_RestartService_ServerSSL.setObjectName("pushButton_RestartService_ServerSSL")
        self.pushButton_Change_ServerSSL = QtWidgets.QPushButton(self.tab_Server_SSL)
        self.pushButton_Change_ServerSSL.setGeometry(QtCore.QRect(110, 290, 75, 23))
        self.pushButton_Change_ServerSSL.setCheckable(False)
        self.pushButton_Change_ServerSSL.setObjectName("pushButton_Change_ServerSSL")
        self.lineEdit_Enable_ServerSSL = QtWidgets.QLineEdit(self.tab_Server_SSL)
        self.lineEdit_Enable_ServerSSL.setGeometry(QtCore.QRect(10, 290, 91, 21))
        self.lineEdit_Enable_ServerSSL.setText("")
        self.lineEdit_Enable_ServerSSL.setObjectName("lineEdit_Enable_ServerSSL")
        self.pushButton_Query_ServerSSL = QtWidgets.QPushButton(self.tab_Server_SSL)
        self.pushButton_Query_ServerSSL.setGeometry(QtCore.QRect(670, 260, 101, 21))
        self.pushButton_Query_ServerSSL.setObjectName("pushButton_Query_ServerSSL")
        self.plainTextEdit_Value_ServerSSL = QtWidgets.QPlainTextEdit(self.tab_Server_SSL)
        self.plainTextEdit_Value_ServerSSL.setGeometry(QtCore.QRect(450, 50, 321, 201))
        self.plainTextEdit_Value_ServerSSL.setReadOnly(True)
        self.plainTextEdit_Value_ServerSSL.setPlainText("")
        self.plainTextEdit_Value_ServerSSL.setObjectName("plainTextEdit_Value_ServerSSL")
        self.tabWidget.addTab(self.tab_Server_SSL, "")
        self.tab_Probe_SSL = QtWidgets.QWidget()
        self.tab_Probe_SSL.setObjectName("tab_Probe_SSL")
        self.tabWidget.addTab(self.tab_Probe_SSL, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1079, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_Change_DBConfig.setText(_translate("MainWindow", "Change"))
        self.label_ConfigPath_DBConfig.setText(_translate("MainWindow", "ConfigPath"))
        self.label_Value_DBConfig.setText(_translate("MainWindow", "Value"))
        self.lineEdit_ConfigPath_DBConfig_Web.setText(_translate("MainWindow", "C:/PIXIS/Web/Config/PixisWebSetting.cfg"))
        self.label_Web_DBConfig.setText(_translate("MainWindow", "Web"))
        self.label_CoreService_DBConfig.setText(_translate("MainWindow", "CoreService"))
        self.label_Radius_DBConfig.setText(_translate("MainWindow", "Radius"))
        self.lineEdit_ConfigPath_DBConfig_CoreService.setText(_translate("MainWindow", "C:/PIXIS/CoreService/Config/CoreServiceSetting.cfg"))
        self.lineEdit_ConfigPath_DBConfig_Radius.setText(_translate("MainWindow", "C:/PIXIS/RadiusService/Config/RadiusServiceSetting.cfg"))
        self.pushButton_Query_DBConfig.setText(_translate("MainWindow", "Query SQL Value"))
        self.label_SQLIP_DBConfig.setText(_translate("MainWindow", "SQL IP"))
        self.label_SQLAccount_DBConfig.setText(_translate("MainWindow", "SQL Account"))
        self.pushButton_RestartService_DBConfig.setText(_translate("MainWindow", "Restart Service"))
        self.label_SQLPWD_DBConfig.setText(_translate("MainWindow", "SQL Password"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_DBConfig), _translate("MainWindow", "DBConfig"))
        self.label_Value_ServerSSL.setText(_translate("MainWindow", "Value"))
        self.label_ConfigPath_ServerSSL.setText(_translate("MainWindow", "ConfigPath"))
        self.lineEdit_ConfigPath_ServerSSL_Web.setText(_translate("MainWindow", "C:/PIXIS/Web/Config/PixisWebSetting.cfg"))
        self.label_Web_ServerSSL.setText(_translate("MainWindow", "Web"))
        self.label_CoreService_ServerSSL.setText(_translate("MainWindow", "CoreService"))
        self.lineEdit_ConfigPath_ServerSSL_CoreService.setText(_translate("MainWindow", "C:/PIXIS/CoreService/Config/CoreServiceSetting.cfg"))
        self.label_Enable_ServerSSL.setText(_translate("MainWindow", "Enable"))
        self.pushButton_RestartService_ServerSSL.setText(_translate("MainWindow", "Restart Service"))
        self.pushButton_Change_ServerSSL.setText(_translate("MainWindow", "Change"))
        self.pushButton_Query_ServerSSL.setText(_translate("MainWindow", "Query Value"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Server_SSL), _translate("MainWindow", "En/Disable Server SSL"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Probe_SSL), _translate("MainWindow", "En/Disable Probe SSL"))
    
        
        self.pushButton_Query_DBConfig.clicked.connect(self.GetDBConfig)
        self.pushButton_Change_DBConfig.clicked.connect(self.WriteDBConfig)
        self.pushButton_Query_ServerSSL.clicked.connect(self.GetSSLEnabled)
        self.pushButton_Change_ServerSSL.clicked.connect(self.WriteSSLConfig)
        self.pushButton_RestartService_DBConfig.clicked.connect(self.RestartAtheNACService)
        self.pushButton_RestartService_ServerSSL.clicked.connect(self.RestartAtheNACService)
    
    def GetDBConfig(self) -> None:
        result = {}
        with codecs.open(filename=self.lineEdit_ConfigPath_DBConfig_Web.text(),encoding='utf-8') as WebconfigFile:
            configdata = json5.loads(WebconfigFile.read())
            result['Web_PIXIS'] =  configdata['ConnectionStrings']['PIXIS']
            result['Web_PIXISEventLog'] =  configdata['ConnectionStrings']['PIXIS_EventLog']
        with codecs.open(filename=self.lineEdit_ConfigPath_DBConfig_CoreService.text(),encoding='utf-8') as CSconfigFile:
            configdata = json5.loads(CSconfigFile.read())
            result['CS_PIXIS'] =  configdata['ConnectionStrings']['PIXIS']
            result['CS_PIXISEventLog'] =  configdata['ConnectionStrings']['PIXIS_EventLog']
        with codecs.open(filename=self.lineEdit_ConfigPath_DBConfig_Radius.text(),encoding='utf-8') as RadiusconfigFile:
            configdata = json5.loads(RadiusconfigFile.read())
            result['Radius_PIXIS'] =  configdata['ConnectionStrings']['PIXIS']
            result['Radius_PIXISEventLog'] =  configdata['ConnectionStrings']['PIXIS_EventLog']
        resultstr = ''
        for i in result:
            resultstr = resultstr + f'{i} : \n {result[i]} \n\n'
        self.plainTextEdit_Value_DBConfig.setPlainText(resultstr)
    
    def GetSSLEnabled(self) -> None:
        result = {}
        with codecs.open(filename=self.lineEdit_ConfigPath_ServerSSL_Web.text(),encoding='utf-8') as WebconfigFile:
            configdata = json5.loads(WebconfigFile.read())
            result['Web_SSL'] =  configdata['SecuritySetting']['EnableSSL']
        with codecs.open(filename=self.lineEdit_ConfigPath_ServerSSL_CoreService.text(),encoding='utf-8') as CSconfigFile:
            configdata = json5.loads(CSconfigFile.read())
            result['CS_SSL'] =  configdata['SecuritySetting']['EnableSSL']
        resultstr = ''
        for i in result:
            resultstr = resultstr + f'{i} : \n {result[i]} \n\n'
        self.plainTextEdit_Value_ServerSSL.setPlainText(resultstr)

    def WriteDBConfig(self) -> None:
        filepaths = []
        filepaths.append(self.lineEdit_ConfigPath_DBConfig_Web.text())
        filepaths.append(self.lineEdit_ConfigPath_DBConfig_CoreService.text())
        filepaths.append(self.lineEdit_ConfigPath_DBConfig_Radius.text())
        for filepath in filepaths:
            config = None
            with codecs.open(filename=filepath,encoding='utf-8') as configfile:
                config = json5.loads(configfile.read())
            SetPIXISConnectStr = f'Data Source={self.lineEdit_SQLIP_DBConfig.text()};Initial Catalog=PIXIS;User ID={self.lineEdit_SQLAccount_DBConfig.text()};Password={self.lineEdit_SQLPWD_DBConfig.text()};MultipleActiveResultSets=True'
            SetPIXISEventConnectStr = f'Data Source={self.lineEdit_SQLIP_DBConfig.text()};Initial Catalog=PixisEventLog;User ID={self.lineEdit_SQLAccount_DBConfig.text()};Password={self.lineEdit_SQLPWD_DBConfig.text()};MultipleActiveResultSets=True'
            config['ConnectionStrings']['PIXIS'] = SetPIXISConnectStr
            config['ConnectionStrings']['PIXIS_EventLog'] = SetPIXISEventConnectStr
            with codecs.open(filename=filepath,mode='w',encoding='utf-8') as configFile:
                configFile.write(json5.dumps(config,indent=4))
        self.GetDBConfig()

    def WriteSSLConfig(self) -> None:
        filepaths = []
        filepaths.append(self.lineEdit_ConfigPath_ServerSSL_Web.text())
        filepaths.append(self.lineEdit_ConfigPath_ServerSSL_CoreService.text())
        for filepath in filepaths:
            config = None
            with codecs.open(filename=filepath,encoding='utf-8') as configfile:
                config = json5.loads(configfile.read())
            config['SecuritySetting']['EnableSSL'] = eval(self.lineEdit_Enable_ServerSSL.text())
            with codecs.open(filename=filepath,mode='w',encoding='utf-8') as configFile:
                configFile.write(json5.dumps(config,indent=4))
        self.GetSSLEnabled()


    def RestartAtheNACService(self) -> None:
        self.process = pxpowershell()
        self.process.start_process()
        resultPIXISUI = self.process.run('Restart-Service -Name PIXISWebUI')
        resultPIXISRadius = self.process.run('Restart-Service -Name PIXISRadiusService')
        resultPIXISCS = self.process.run('Restart-Service -Name PIXISCoreService')
        resultstr = f'PIXIS_UI : {str(resultPIXISUI)} \n PIXIS_CS : {str(resultPIXISCS)} \n PIXIS_Radius : {str(resultPIXISRadius)}'
        self.plainTextEdit_Value_DBConfig.setPlainText(resultstr)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
