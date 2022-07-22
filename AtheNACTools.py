import json5,codecs,json,subprocess
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow): 
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1079, 828)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 1051, 441))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_DBConfig = QtWidgets.QWidget()
        self.tab_DBConfig.setObjectName("tab_DBConfig")
        self.pushButton_Change_DBConfig = QtWidgets.QPushButton(self.tab_DBConfig)
        self.pushButton_Change_DBConfig.setGeometry(QtCore.QRect(760, 120, 75, 23))
        self.pushButton_Change_DBConfig.setCheckable(False)
        self.pushButton_Change_DBConfig.setObjectName("pushButton_Change_DBConfig")
        self.label_ConfigPath_DBConfig = QtWidgets.QLabel(self.tab_DBConfig)
        self.label_ConfigPath_DBConfig.setGeometry(QtCore.QRect(120, 30, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_ConfigPath_DBConfig.setFont(font)
        self.label_ConfigPath_DBConfig.setObjectName("label_ConfigPath_DBConfig")
        self.label_Oprator_DBConfig = QtWidgets.QLabel(self.tab_DBConfig)
        self.label_Oprator_DBConfig.setGeometry(QtCore.QRect(420, 30, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_Oprator_DBConfig.setFont(font)
        self.label_Oprator_DBConfig.setObjectName("label_Oprator_DBConfig")
        self.lineEdit_ConfigPath_DBConfig_Web = QtWidgets.QLineEdit(self.tab_DBConfig)
        self.lineEdit_ConfigPath_DBConfig_Web.setGeometry(QtCore.QRect(120, 60, 281, 31))
        self.lineEdit_ConfigPath_DBConfig_Web.setObjectName("lineEdit_ConfigPath_DBConfig_Web")
        self.label_Web_DBConfig = QtWidgets.QLabel(self.tab_DBConfig)
        self.label_Web_DBConfig.setGeometry(QtCore.QRect(10, 60, 47, 12))
        self.label_Web_DBConfig.setObjectName("label_Web_DBConfig")
        self.label_CoreService_DBConfig = QtWidgets.QLabel(self.tab_DBConfig)
        self.label_CoreService_DBConfig.setGeometry(QtCore.QRect(10, 100, 81, 16))
        self.label_CoreService_DBConfig.setObjectName("label_CoreService_DBConfig")
        self.label_Radius_DBConfig = QtWidgets.QLabel(self.tab_DBConfig)
        self.label_Radius_DBConfig.setGeometry(QtCore.QRect(10, 150, 47, 12))
        self.label_Radius_DBConfig.setObjectName("label_Radius_DBConfig")
        self.lineEdit_ConfigPath_DBConfig_CoreService = QtWidgets.QLineEdit(self.tab_DBConfig)
        self.lineEdit_ConfigPath_DBConfig_CoreService.setGeometry(QtCore.QRect(120, 100, 281, 31))
        self.lineEdit_ConfigPath_DBConfig_CoreService.setObjectName("lineEdit_ConfigPath_DBConfig_CoreService")
        self.lineEdit_ConfigPath_DBConfig_Radius = QtWidgets.QLineEdit(self.tab_DBConfig)
        self.lineEdit_ConfigPath_DBConfig_Radius.setGeometry(QtCore.QRect(120, 140, 281, 31))
        self.lineEdit_ConfigPath_DBConfig_Radius.setObjectName("lineEdit_ConfigPath_DBConfig_Radius")
        self.pushButton_Query_DBConfig = QtWidgets.QPushButton(self.tab_DBConfig)
        self.pushButton_Query_DBConfig.setGeometry(QtCore.QRect(420, 70, 101, 21))
        self.pushButton_Query_DBConfig.setObjectName("pushButton_Query_DBConfig")
        self.lineEdit_SQLIP_DBConfig = QtWidgets.QLineEdit(self.tab_DBConfig)
        self.lineEdit_SQLIP_DBConfig.setGeometry(QtCore.QRect(420, 120, 91, 21))
        self.lineEdit_SQLIP_DBConfig.setText("")
        self.lineEdit_SQLIP_DBConfig.setObjectName("lineEdit_SQLIP_DBConfig")
        self.label_SQLIP_DBConfig = QtWidgets.QLabel(self.tab_DBConfig)
        self.label_SQLIP_DBConfig.setGeometry(QtCore.QRect(420, 100, 47, 12))
        self.label_SQLIP_DBConfig.setObjectName("label_SQLIP_DBConfig")
        self.label_SQLAccount_DBConfig = QtWidgets.QLabel(self.tab_DBConfig)
        self.label_SQLAccount_DBConfig.setGeometry(QtCore.QRect(520, 100, 81, 16))
        self.label_SQLAccount_DBConfig.setObjectName("label_SQLAccount_DBConfig")
        self.lineEdit_SQLAccount_DBConfig = QtWidgets.QLineEdit(self.tab_DBConfig)
        self.lineEdit_SQLAccount_DBConfig.setGeometry(QtCore.QRect(520, 120, 91, 21))
        self.lineEdit_SQLAccount_DBConfig.setObjectName("lineEdit_SQLAccount_DBConfig")
        self.pushButton_RestartService_DBConfig = QtWidgets.QPushButton(self.tab_DBConfig)
        self.pushButton_RestartService_DBConfig.setGeometry(QtCore.QRect(840, 120, 91, 23))
        self.pushButton_RestartService_DBConfig.setObjectName("pushButton_RestartService_DBConfig")
        self.lineEdit_SQLPWD_DBConfig = QtWidgets.QLineEdit(self.tab_DBConfig)
        self.lineEdit_SQLPWD_DBConfig.setGeometry(QtCore.QRect(630, 120, 113, 20))
        self.lineEdit_SQLPWD_DBConfig.setObjectName("lineEdit_SQLPWD_DBConfig")
        self.label_SQLPWD_DBConfig = QtWidgets.QLabel(self.tab_DBConfig)
        self.label_SQLPWD_DBConfig.setGeometry(QtCore.QRect(630, 100, 71, 16))
        self.label_SQLPWD_DBConfig.setObjectName("label_SQLPWD_DBConfig")
        self.tabWidget.addTab(self.tab_DBConfig, "")
        self.tab_Server_SSL = QtWidgets.QWidget()
        self.tab_Server_SSL.setObjectName("tab_Server_SSL")
        self.label_ConfigPath_ServerSSL = QtWidgets.QLabel(self.tab_Server_SSL)
        self.label_ConfigPath_ServerSSL.setGeometry(QtCore.QRect(120, 30, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_ConfigPath_ServerSSL.setFont(font)
        self.label_ConfigPath_ServerSSL.setObjectName("label_ConfigPath_ServerSSL")
        self.lineEdit_ConfigPath_ServerSSL_Web = QtWidgets.QLineEdit(self.tab_Server_SSL)
        self.lineEdit_ConfigPath_ServerSSL_Web.setGeometry(QtCore.QRect(120, 70, 281, 31))
        self.lineEdit_ConfigPath_ServerSSL_Web.setObjectName("lineEdit_ConfigPath_ServerSSL_Web")
        self.label_Web_ServerSSL = QtWidgets.QLabel(self.tab_Server_SSL)
        self.label_Web_ServerSSL.setGeometry(QtCore.QRect(10, 70, 47, 12))
        self.label_Web_ServerSSL.setObjectName("label_Web_ServerSSL")
        self.label_CoreService_ServerSSL = QtWidgets.QLabel(self.tab_Server_SSL)
        self.label_CoreService_ServerSSL.setGeometry(QtCore.QRect(10, 110, 81, 16))
        self.label_CoreService_ServerSSL.setObjectName("label_CoreService_ServerSSL")
        self.lineEdit_ConfigPath_ServerSSL_CoreService = QtWidgets.QLineEdit(self.tab_Server_SSL)
        self.lineEdit_ConfigPath_ServerSSL_CoreService.setGeometry(QtCore.QRect(120, 110, 281, 31))
        self.lineEdit_ConfigPath_ServerSSL_CoreService.setObjectName("lineEdit_ConfigPath_ServerSSL_CoreService")
        self.pushButton_RestartService_ServerSSL = QtWidgets.QPushButton(self.tab_Server_SSL)
        self.pushButton_RestartService_ServerSSL.setGeometry(QtCore.QRect(590, 110, 91, 23))
        self.pushButton_RestartService_ServerSSL.setObjectName("pushButton_RestartService_ServerSSL")
        self.pushButton_Change_ServerSSL = QtWidgets.QPushButton(self.tab_Server_SSL)
        self.pushButton_Change_ServerSSL.setGeometry(QtCore.QRect(510, 110, 75, 23))
        self.pushButton_Change_ServerSSL.setCheckable(False)
        self.pushButton_Change_ServerSSL.setObjectName("pushButton_Change_ServerSSL")
        self.pushButton_Query_ServerSSL = QtWidgets.QPushButton(self.tab_Server_SSL)
        self.pushButton_Query_ServerSSL.setGeometry(QtCore.QRect(420, 70, 101, 21))
        self.pushButton_Query_ServerSSL.setObjectName("pushButton_Query_ServerSSL")
        self.label_Oprator_ServerSSL = QtWidgets.QLabel(self.tab_Server_SSL)
        self.label_Oprator_ServerSSL.setGeometry(QtCore.QRect(430, 30, 47, 12))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_Oprator_ServerSSL.setFont(font)
        self.label_Oprator_ServerSSL.setObjectName("label_Oprator_ServerSSL")
        self.checkBox_Enabled_ServerSSL = QtWidgets.QCheckBox(self.tab_Server_SSL)
        self.checkBox_Enabled_ServerSSL.setGeometry(QtCore.QRect(420, 110, 73, 21))
        self.checkBox_Enabled_ServerSSL.setObjectName("checkBox_Enabled_ServerSSL")
        self.tabWidget.addTab(self.tab_Server_SSL, "")
        self.tab_Probe_SSL = QtWidgets.QWidget()
        self.tab_Probe_SSL.setObjectName("tab_Probe_SSL")
        self.tabWidget.addTab(self.tab_Probe_SSL, "")
        self.plainTextEdit_Result_Display = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_Result_Display.setGeometry(QtCore.QRect(20, 470, 1021, 311))
        self.plainTextEdit_Result_Display.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.plainTextEdit_Result_Display.setReadOnly(True)
        self.plainTextEdit_Result_Display.setPlainText("")
        self.plainTextEdit_Result_Display.setCenterOnScroll(False)
        self.plainTextEdit_Result_Display.setObjectName("plainTextEdit_Result_Display")
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
        MainWindow.setWindowTitle(_translate("MainWindow", "AtheNAC Tools"))
        self.pushButton_Change_DBConfig.setText(_translate("MainWindow", "Change"))
        self.label_ConfigPath_DBConfig.setText(_translate("MainWindow", "ConfigPath"))
        self.label_Oprator_DBConfig.setText(_translate("MainWindow", "Oprator"))
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
        self.label_ConfigPath_ServerSSL.setText(_translate("MainWindow", "ConfigPath"))
        self.lineEdit_ConfigPath_ServerSSL_Web.setText(_translate("MainWindow", "C:/PIXIS/Web/Config/PixisWebSetting.cfg"))
        self.label_Web_ServerSSL.setText(_translate("MainWindow", "Web"))
        self.label_CoreService_ServerSSL.setText(_translate("MainWindow", "CoreService"))
        self.lineEdit_ConfigPath_ServerSSL_CoreService.setText(_translate("MainWindow", "C:/PIXIS/CoreService/Config/CoreServiceSetting.cfg"))
        self.pushButton_RestartService_ServerSSL.setText(_translate("MainWindow", "Restart Service"))
        self.pushButton_Change_ServerSSL.setText(_translate("MainWindow", "Change"))
        self.pushButton_Query_ServerSSL.setText(_translate("MainWindow", "Query Value"))
        self.label_Oprator_ServerSSL.setText(_translate("MainWindow", "Oprator"))
        self.checkBox_Enabled_ServerSSL.setText(_translate("MainWindow", "CheckBox"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Server_SSL), _translate("MainWindow", "En/Disable Server SSL"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Probe_SSL), _translate("MainWindow", "En/Disable Probe SSL"))

    
        
        self.pushButton_Query_DBConfig.clicked.connect(self.GetDBConfig)
        self.pushButton_Change_DBConfig.clicked.connect(self.WriteDBConfig)
        self.pushButton_Query_ServerSSL.clicked.connect(self.GetSSLEnabled)
        self.pushButton_Change_ServerSSL.clicked.connect(self.WriteSSLConfig)
        self.pushButton_RestartService_DBConfig.clicked.connect(self.RestartAtheNACService)
        self.pushButton_RestartService_ServerSSL.clicked.connect(self.RestartAtheNACService)
    
    def GetDBConfig(self) -> None:
        try:
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
            self.plainTextEdit_Result_Display.setPlainText(resultstr)
        except Exception as e:
            self.plainTextEdit_Result_Display.setPlainText(str(e))
    
    def GetSSLEnabled(self) -> None:
        try:
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
            self.plainTextEdit_Result_Display.setPlainText(resultstr)
        except Exception as e:
            self.plainTextEdit_Result_Display.setPlainText(str(e))

    def WriteDBConfig(self) -> None:
        try:
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
                    configFile.write(json.dumps(config,indent=4))
            self.GetDBConfig()
        except Exception as e:
            self.plainTextEdit_Result_Display.setPlainText(str(e))

    def WriteSSLConfig(self) -> None:
        try:
            filepaths = []
            filepaths.append(self.lineEdit_ConfigPath_ServerSSL_Web.text())
            filepaths.append(self.lineEdit_ConfigPath_ServerSSL_CoreService.text())
            for filepath in filepaths:
                config = None
                with codecs.open(filename=filepath,encoding='utf-8') as configfile:
                    config = json5.loads(configfile.read())
                config['SecuritySetting']['EnableSSL'] = bool(self.checkBox_Enabled_ServerSSL.checkState())
                with codecs.open(filename=filepath,mode='w',encoding='utf-8') as configFile:
                    configFile.write(json.dumps(config,indent=4))
            self.GetSSLEnabled()
        except Exception as e:
            self.plainTextEdit_Result_Display.setPlainText(str(e))

    def RestartAtheNACService(self) -> None:
        try :
            resultstr = ''
            servicelist = ['PIXISWebUI','PIXISCoreService','PIXISRadiusService']
            for service in  servicelist :
                if subprocess.run(['sc', 'query', service]).returncode ==1060 : 
                    resultstr = resultstr + f'{service} : Service Not Found \n'
                    continue
                subprocess.run(['sc', 'stop', service])
                result = subprocess.run(['sc', 'start', service]).returncode
                resultstr = resultstr + f'{service} : {result} \n'
            self.plainTextEdit_Result_Display.setPlainText(resultstr)
        except Exception as e:
            self.plainTextEdit_Result_Display.setPlainText(str(e))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
