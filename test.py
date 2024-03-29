# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AtheNACToolsUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


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
        self.pushButton_Change_DBConfig.setGeometry(QtCore.QRect(530, 110, 75, 23))
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
        self.pushButton_Query_DBConfig.setGeometry(QtCore.QRect(420, 110, 101, 21))
        self.pushButton_Query_DBConfig.setObjectName("pushButton_Query_DBConfig")
        self.lineEdit_SQLIP_DBConfig = QtWidgets.QLineEdit(self.tab_DBConfig)
        self.lineEdit_SQLIP_DBConfig.setGeometry(QtCore.QRect(420, 80, 91, 21))
        self.lineEdit_SQLIP_DBConfig.setText("")
        self.lineEdit_SQLIP_DBConfig.setObjectName("lineEdit_SQLIP_DBConfig")
        self.label_SQLIP_DBConfig = QtWidgets.QLabel(self.tab_DBConfig)
        self.label_SQLIP_DBConfig.setGeometry(QtCore.QRect(420, 60, 47, 12))
        self.label_SQLIP_DBConfig.setObjectName("label_SQLIP_DBConfig")
        self.label_SQLAccount_DBConfig = QtWidgets.QLabel(self.tab_DBConfig)
        self.label_SQLAccount_DBConfig.setGeometry(QtCore.QRect(520, 60, 81, 16))
        self.label_SQLAccount_DBConfig.setObjectName("label_SQLAccount_DBConfig")
        self.lineEdit_SQLAccount_DBConfig = QtWidgets.QLineEdit(self.tab_DBConfig)
        self.lineEdit_SQLAccount_DBConfig.setGeometry(QtCore.QRect(520, 80, 91, 21))
        self.lineEdit_SQLAccount_DBConfig.setObjectName("lineEdit_SQLAccount_DBConfig")
        self.pushButton_StartService_DBConfig = QtWidgets.QPushButton(self.tab_DBConfig)
        self.pushButton_StartService_DBConfig.setGeometry(QtCore.QRect(610, 110, 91, 23))
        self.pushButton_StartService_DBConfig.setObjectName("pushButton_StartService_DBConfig")
        self.lineEdit_SQLPWD_DBConfig = QtWidgets.QLineEdit(self.tab_DBConfig)
        self.lineEdit_SQLPWD_DBConfig.setGeometry(QtCore.QRect(630, 80, 113, 20))
        self.lineEdit_SQLPWD_DBConfig.setObjectName("lineEdit_SQLPWD_DBConfig")
        self.label_SQLPWD_DBConfig = QtWidgets.QLabel(self.tab_DBConfig)
        self.label_SQLPWD_DBConfig.setGeometry(QtCore.QRect(630, 60, 71, 16))
        self.label_SQLPWD_DBConfig.setObjectName("label_SQLPWD_DBConfig")
        self.label_Radis_DBConfig = QtWidgets.QLabel(self.tab_DBConfig)
        self.label_Radis_DBConfig.setGeometry(QtCore.QRect(420, 150, 71, 16))
        self.label_Radis_DBConfig.setObjectName("label_Radis_DBConfig")
        self.lineEdit_Radis_DBConfig = QtWidgets.QLineEdit(self.tab_DBConfig)
        self.lineEdit_Radis_DBConfig.setGeometry(QtCore.QRect(420, 170, 221, 20))
        self.lineEdit_Radis_DBConfig.setObjectName("lineEdit_Radis_DBConfig")
        self.pushButton_ChangeRadis_DBConfig = QtWidgets.QPushButton(self.tab_DBConfig)
        self.pushButton_ChangeRadis_DBConfig.setGeometry(QtCore.QRect(500, 200, 101, 21))
        self.pushButton_ChangeRadis_DBConfig.setObjectName("pushButton_ChangeRadis_DBConfig")
        self.pushButton_GetRadis_DBConfig = QtWidgets.QPushButton(self.tab_DBConfig)
        self.pushButton_GetRadis_DBConfig.setGeometry(QtCore.QRect(420, 200, 75, 23))
        self.pushButton_GetRadis_DBConfig.setObjectName("pushButton_GetRadis_DBConfig")
        self.pushButton_StopService_DBConfig = QtWidgets.QPushButton(self.tab_DBConfig)
        self.pushButton_StopService_DBConfig.setGeometry(QtCore.QRect(710, 110, 75, 23))
        self.pushButton_StopService_DBConfig.setObjectName("pushButton_StopService_DBConfig")
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
        self.pushButton_StartService_ServerSSL = QtWidgets.QPushButton(self.tab_Server_SSL)
        self.pushButton_StartService_ServerSSL.setGeometry(QtCore.QRect(630, 100, 91, 23))
        self.pushButton_StartService_ServerSSL.setObjectName("pushButton_StartService_ServerSSL")
        self.pushButton_Change_ServerSSL = QtWidgets.QPushButton(self.tab_Server_SSL)
        self.pushButton_Change_ServerSSL.setGeometry(QtCore.QRect(540, 100, 75, 23))
        self.pushButton_Change_ServerSSL.setCheckable(False)
        self.pushButton_Change_ServerSSL.setObjectName("pushButton_Change_ServerSSL")
        self.pushButton_Query_ServerSSL = QtWidgets.QPushButton(self.tab_Server_SSL)
        self.pushButton_Query_ServerSSL.setGeometry(QtCore.QRect(430, 100, 101, 21))
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
        self.checkBox_Enabled_ServerSSL.setGeometry(QtCore.QRect(430, 70, 73, 21))
        self.checkBox_Enabled_ServerSSL.setObjectName("checkBox_Enabled_ServerSSL")
        self.pushButton_StopService_ServerSSL = QtWidgets.QPushButton(self.tab_Server_SSL)
        self.pushButton_StopService_ServerSSL.setGeometry(QtCore.QRect(730, 100, 75, 23))
        self.pushButton_StopService_ServerSSL.setObjectName("pushButton_StopService_ServerSSL")
        self.tabWidget.addTab(self.tab_Server_SSL, "")
        self.tab_Probe_SSL = QtWidgets.QWidget()
        self.tab_Probe_SSL.setObjectName("tab_Probe_SSL")
        self.label_ProbeIP_ProbeSSl = QtWidgets.QLabel(self.tab_Probe_SSL)
        self.label_ProbeIP_ProbeSSl.setGeometry(QtCore.QRect(10, 70, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(False)
        font.setWeight(50)
        self.label_ProbeIP_ProbeSSl.setFont(font)
        self.label_ProbeIP_ProbeSSl.setObjectName("label_ProbeIP_ProbeSSl")
        self.label_SSHAccount_ProbeSSl = QtWidgets.QLabel(self.tab_Probe_SSL)
        self.label_SSHAccount_ProbeSSl.setGeometry(QtCore.QRect(10, 110, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(False)
        font.setWeight(50)
        self.label_SSHAccount_ProbeSSl.setFont(font)
        self.label_SSHAccount_ProbeSSl.setObjectName("label_SSHAccount_ProbeSSl")
        self.label_Password_ProbeSSl = QtWidgets.QLabel(self.tab_Probe_SSL)
        self.label_Password_ProbeSSl.setGeometry(QtCore.QRect(10, 150, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(False)
        font.setWeight(50)
        self.label_Password_ProbeSSl.setFont(font)
        self.label_Password_ProbeSSl.setObjectName("label_Password_ProbeSSl")
        self.label_Config_ProbeSSL = QtWidgets.QLabel(self.tab_Probe_SSL)
        self.label_Config_ProbeSSL.setGeometry(QtCore.QRect(120, 30, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_Config_ProbeSSL.setFont(font)
        self.label_Config_ProbeSSL.setObjectName("label_Config_ProbeSSL")
        self.label_Oprator_ProbeSSL = QtWidgets.QLabel(self.tab_Probe_SSL)
        self.label_Oprator_ProbeSSL.setGeometry(QtCore.QRect(430, 30, 47, 12))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_Oprator_ProbeSSL.setFont(font)
        self.label_Oprator_ProbeSSL.setObjectName("label_Oprator_ProbeSSL")
        self.lineEdit_ProbeIP_ProbeSSL = QtWidgets.QLineEdit(self.tab_Probe_SSL)
        self.lineEdit_ProbeIP_ProbeSSL.setGeometry(QtCore.QRect(120, 70, 201, 31))
        self.lineEdit_ProbeIP_ProbeSSL.setObjectName("lineEdit_ProbeIP_ProbeSSL")
        self.lineEdit_SSHAccount_ProbeSSL = QtWidgets.QLineEdit(self.tab_Probe_SSL)
        self.lineEdit_SSHAccount_ProbeSSL.setGeometry(QtCore.QRect(120, 110, 201, 31))
        self.lineEdit_SSHAccount_ProbeSSL.setObjectName("lineEdit_SSHAccount_ProbeSSL")
        self.lineEdit_SSHPassword_ProbeSSL = QtWidgets.QLineEdit(self.tab_Probe_SSL)
        self.lineEdit_SSHPassword_ProbeSSL.setGeometry(QtCore.QRect(120, 150, 201, 31))
        self.lineEdit_SSHPassword_ProbeSSL.setObjectName("lineEdit_SSHPassword_ProbeSSL")
        self.lineEdit_Port_ProbeSSL = QtWidgets.QLineEdit(self.tab_Probe_SSL)
        self.lineEdit_Port_ProbeSSL.setGeometry(QtCore.QRect(120, 190, 201, 31))
        self.lineEdit_Port_ProbeSSL.setObjectName("lineEdit_Port_ProbeSSL")
        self.label_Port_ProbeSSl = QtWidgets.QLabel(self.tab_Probe_SSL)
        self.label_Port_ProbeSSl.setGeometry(QtCore.QRect(10, 190, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(False)
        font.setWeight(50)
        self.label_Port_ProbeSSl.setFont(font)
        self.label_Port_ProbeSSl.setObjectName("label_Port_ProbeSSl")
        self.checkBox_Enabled_ProbeSSL = QtWidgets.QCheckBox(self.tab_Probe_SSL)
        self.checkBox_Enabled_ProbeSSL.setGeometry(QtCore.QRect(430, 60, 73, 21))
        self.checkBox_Enabled_ProbeSSL.setObjectName("checkBox_Enabled_ProbeSSL")
        self.pushButton_Change_ProbeSSL = QtWidgets.QPushButton(self.tab_Probe_SSL)
        self.pushButton_Change_ProbeSSL.setGeometry(QtCore.QRect(540, 130, 75, 23))
        self.pushButton_Change_ProbeSSL.setCheckable(False)
        self.pushButton_Change_ProbeSSL.setObjectName("pushButton_Change_ProbeSSL")
        self.pushButton_Query_ProbeSSL = QtWidgets.QPushButton(self.tab_Probe_SSL)
        self.pushButton_Query_ProbeSSL.setGeometry(QtCore.QRect(430, 130, 101, 21))
        self.pushButton_Query_ProbeSSL.setObjectName("pushButton_Query_ProbeSSL")
        self.pushButton_Reboot_ProbeSSL = QtWidgets.QPushButton(self.tab_Probe_SSL)
        self.pushButton_Reboot_ProbeSSL.setGeometry(QtCore.QRect(620, 130, 75, 23))
        self.pushButton_Reboot_ProbeSSL.setObjectName("pushButton_Reboot_ProbeSSL")
        self.lineEdit_ExpireDay_ProbeSSL = QtWidgets.QLineEdit(self.tab_Probe_SSL)
        self.lineEdit_ExpireDay_ProbeSSL.setGeometry(QtCore.QRect(530, 90, 31, 21))
        self.lineEdit_ExpireDay_ProbeSSL.setObjectName("lineEdit_ExpireDay_ProbeSSL")
        self.label_ExpireDay_ProbeSSl = QtWidgets.QLabel(self.tab_Probe_SSL)
        self.label_ExpireDay_ProbeSSl.setGeometry(QtCore.QRect(430, 90, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(False)
        font.setWeight(50)
        self.label_ExpireDay_ProbeSSl.setFont(font)
        self.label_ExpireDay_ProbeSSl.setObjectName("label_ExpireDay_ProbeSSl")
        self.tabWidget.addTab(self.tab_Probe_SSL, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_ServerURL_ImportIPRange = QtWidgets.QLabel(self.tab)
        self.label_ServerURL_ImportIPRange.setGeometry(QtCore.QRect(10, 60, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_ServerURL_ImportIPRange.setFont(font)
        self.label_ServerURL_ImportIPRange.setObjectName("label_ServerURL_ImportIPRange")
        self.lineEdit_ServerURL_ImportIPRange = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_ServerURL_ImportIPRange.setGeometry(QtCore.QRect(80, 60, 201, 31))
        self.lineEdit_ServerURL_ImportIPRange.setObjectName("lineEdit_ServerURL_ImportIPRange")
        self.label_Account_ImportIPRange = QtWidgets.QLabel(self.tab)
        self.label_Account_ImportIPRange.setGeometry(QtCore.QRect(10, 100, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_Account_ImportIPRange.setFont(font)
        self.label_Account_ImportIPRange.setObjectName("label_Account_ImportIPRange")
        self.lineEdit_Account_ImportIPRange = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_Account_ImportIPRange.setGeometry(QtCore.QRect(80, 100, 201, 31))
        self.lineEdit_Account_ImportIPRange.setObjectName("lineEdit_Account_ImportIPRange")
        self.label_Pasword_ImportIPRange = QtWidgets.QLabel(self.tab)
        self.label_Pasword_ImportIPRange.setGeometry(QtCore.QRect(10, 140, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_Pasword_ImportIPRange.setFont(font)
        self.label_Pasword_ImportIPRange.setObjectName("label_Pasword_ImportIPRange")
        self.lineEdit_Password_ImportIPRange = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_Password_ImportIPRange.setGeometry(QtCore.QRect(80, 140, 201, 31))
        self.lineEdit_Password_ImportIPRange.setObjectName("lineEdit_Password_ImportIPRange")
        self.lineEdit_FilePath_ImportIPRange = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_FilePath_ImportIPRange.setGeometry(QtCore.QRect(80, 180, 201, 31))
        self.lineEdit_FilePath_ImportIPRange.setObjectName("lineEdit_FilePath_ImportIPRange")
        self.label_FilePath_ImportIPRange = QtWidgets.QLabel(self.tab)
        self.label_FilePath_ImportIPRange.setGeometry(QtCore.QRect(10, 180, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_FilePath_ImportIPRange.setFont(font)
        self.label_FilePath_ImportIPRange.setObjectName("label_FilePath_ImportIPRange")
        self.pushButton_ImportRange_ImportIPRange = QtWidgets.QPushButton(self.tab)
        self.pushButton_ImportRange_ImportIPRange.setGeometry(QtCore.QRect(290, 190, 75, 23))
        self.pushButton_ImportRange_ImportIPRange.setObjectName("pushButton_ImportRange_ImportIPRange")
        self.pushButton_ImportDHCP_ImportIPRange = QtWidgets.QPushButton(self.tab)
        self.pushButton_ImportDHCP_ImportIPRange.setGeometry(QtCore.QRect(370, 190, 75, 23))
        self.pushButton_ImportDHCP_ImportIPRange.setObjectName("pushButton_ImportDHCP_ImportIPRange")
        self.pushButton_DownloadSample_ImportIPRange = QtWidgets.QPushButton(self.tab)
        self.pushButton_DownloadSample_ImportIPRange.setGeometry(QtCore.QRect(290, 60, 101, 21))
        self.pushButton_DownloadSample_ImportIPRange.setObjectName("pushButton_DownloadSample_ImportIPRange")
        self.tabWidget.addTab(self.tab, "")
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
        self.pushButton_StartService_DBConfig.setText(_translate("MainWindow", "Start Service"))
        self.label_SQLPWD_DBConfig.setText(_translate("MainWindow", "SQL Password"))
        self.label_Radis_DBConfig.setText(_translate("MainWindow", "Radis Config"))
        self.lineEdit_Radis_DBConfig.setText(_translate("MainWindow", "192.168.10.20:6379,password=111aaaBBB"))
        self.pushButton_ChangeRadis_DBConfig.setText(_translate("MainWindow", "Change Radis IP"))
        self.pushButton_GetRadis_DBConfig.setText(_translate("MainWindow", "Get Radis IP"))
        self.pushButton_StopService_DBConfig.setText(_translate("MainWindow", "StopService"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_DBConfig), _translate("MainWindow", "DBConfig"))
        self.label_ConfigPath_ServerSSL.setText(_translate("MainWindow", "ConfigPath"))
        self.lineEdit_ConfigPath_ServerSSL_Web.setText(_translate("MainWindow", "C:/PIXIS/Web/Config/PixisWebSetting.cfg"))
        self.label_Web_ServerSSL.setText(_translate("MainWindow", "Web"))
        self.label_CoreService_ServerSSL.setText(_translate("MainWindow", "CoreService"))
        self.lineEdit_ConfigPath_ServerSSL_CoreService.setText(_translate("MainWindow", "C:/PIXIS/CoreService/Config/CoreServiceSetting.cfg"))
        self.pushButton_StartService_ServerSSL.setText(_translate("MainWindow", "Start Service"))
        self.pushButton_Change_ServerSSL.setText(_translate("MainWindow", "Change"))
        self.pushButton_Query_ServerSSL.setText(_translate("MainWindow", "Query Value"))
        self.label_Oprator_ServerSSL.setText(_translate("MainWindow", "Oprator"))
        self.checkBox_Enabled_ServerSSL.setText(_translate("MainWindow", "Enable"))
        self.pushButton_StopService_ServerSSL.setText(_translate("MainWindow", "StopService"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Server_SSL), _translate("MainWindow", "En/Disable Server SSL"))
        self.label_ProbeIP_ProbeSSl.setText(_translate("MainWindow", "Probe IP"))
        self.label_SSHAccount_ProbeSSl.setText(_translate("MainWindow", "SSH Account"))
        self.label_Password_ProbeSSl.setText(_translate("MainWindow", "SSH Password"))
        self.label_Config_ProbeSSL.setText(_translate("MainWindow", "Config"))
        self.label_Oprator_ProbeSSL.setText(_translate("MainWindow", "Oprator"))
        self.lineEdit_SSHAccount_ProbeSSL.setText(_translate("MainWindow", "root"))
        self.lineEdit_SSHPassword_ProbeSSL.setText(_translate("MainWindow", "1111"))
        self.lineEdit_Port_ProbeSSL.setText(_translate("MainWindow", "0,1"))
        self.label_Port_ProbeSSl.setText(_translate("MainWindow", "Port"))
        self.checkBox_Enabled_ProbeSSL.setText(_translate("MainWindow", "Enable"))
        self.pushButton_Change_ProbeSSL.setText(_translate("MainWindow", "Change"))
        self.pushButton_Query_ProbeSSL.setText(_translate("MainWindow", "Query Value"))
        self.pushButton_Reboot_ProbeSSL.setText(_translate("MainWindow", "Reboot"))
        self.lineEdit_ExpireDay_ProbeSSL.setText(_translate("MainWindow", "14"))
        self.label_ExpireDay_ProbeSSl.setText(_translate("MainWindow", "Log Expire Day"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Probe_SSL), _translate("MainWindow", "En/Disable Probe SSL"))
        self.label_ServerURL_ImportIPRange.setText(_translate("MainWindow", "ServerURL"))
        self.lineEdit_ServerURL_ImportIPRange.setText(_translate("MainWindow", "https://192.168.22.180:8001"))
        self.label_Account_ImportIPRange.setText(_translate("MainWindow", "Account"))
        self.lineEdit_Account_ImportIPRange.setText(_translate("MainWindow", "admin"))
        self.label_Pasword_ImportIPRange.setText(_translate("MainWindow", "Password"))
        self.lineEdit_Password_ImportIPRange.setText(_translate("MainWindow", "admin"))
        self.lineEdit_FilePath_ImportIPRange.setText(_translate("MainWindow", "IPRange.csv"))
        self.label_FilePath_ImportIPRange.setText(_translate("MainWindow", "FilePath"))
        self.pushButton_ImportRange_ImportIPRange.setText(_translate("MainWindow", "ImportRange"))
        self.pushButton_ImportDHCP_ImportIPRange.setText(_translate("MainWindow", "ImportDHCP"))
        self.pushButton_DownloadSample_ImportIPRange.setText(_translate("MainWindow", "DownloadSample"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "ImportIPRange"))
