# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1326, 790)
        MainWindow.setMinimumSize(QtCore.QSize(301, 371))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(650, 190, 581, 471))
        self.frame_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"border-radius:40px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.admin_info = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.admin_info.sizePolicy().hasHeightForWidth())
        self.admin_info.setSizePolicy(sizePolicy)
        self.admin_info.setStyleSheet("QPushButton:pressed{\n"
"    border-image: url(:/icon/icon/退出,出.png);\n"
"}\n"
"QPushButton:hover{\n"
"    padding-top：5px;\n"
"    padding-left:5px;\n"
"}")
        self.admin_info.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.admin_info.setFrameShadow(QtWidgets.QFrame.Raised)
        self.admin_info.setObjectName("admin_info")
        self.verticalLayout_2.addWidget(self.admin_info)
        self.frame_10 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_10)
        self.stackedWidget.setStyleSheet("QLineEdit{\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    border-bottom: 1px solid black\n"
"}\n"
"QPushButton:pressed{\n"
"    padding-top:5px;\n"
"    padding-left:5px;\n"
"}")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_login = QtWidgets.QWidget()
        self.page_login.setObjectName("page_login")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.page_login)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.lineEdit_login_phone = QtWidgets.QLineEdit(self.page_login)
        self.lineEdit_login_phone.setMinimumSize(QtCore.QSize(0, 50))
        self.lineEdit_login_phone.setObjectName("lineEdit_login_phone")
        self.verticalLayout_6.addWidget(self.lineEdit_login_phone)
        self.lineEdit_login_passwd = QtWidgets.QLineEdit(self.page_login)
        self.lineEdit_login_passwd.setMinimumSize(QtCore.QSize(0, 50))
        self.lineEdit_login_passwd.setStyleSheet("")
        self.lineEdit_login_passwd.setText("")
        self.lineEdit_login_passwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_login_passwd.setObjectName("lineEdit_login_passwd")
        self.verticalLayout_6.addWidget(self.lineEdit_login_passwd)
        self.pushButton_3 = QtWidgets.QPushButton(self.page_login)
        self.pushButton_3.setStyleSheet("font: 12pt \"Algerian\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_6.addWidget(self.pushButton_3)
        self.stackedWidget.addWidget(self.page_login)
        self.page_register = QtWidgets.QWidget()
        self.page_register.setObjectName("page_register")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.page_register)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lineEdit_register_phone = QtWidgets.QLineEdit(self.page_register)
        self.lineEdit_register_phone.setObjectName("lineEdit_register_phone")
        self.verticalLayout_5.addWidget(self.lineEdit_register_phone)
        self.lineEdit_register_passwd = QtWidgets.QLineEdit(self.page_register)
        self.lineEdit_register_passwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_register_passwd.setObjectName("lineEdit_register_passwd")
        self.verticalLayout_5.addWidget(self.lineEdit_register_passwd)
        self.lineEdit_register_passwd2 = QtWidgets.QLineEdit(self.page_register)
        self.lineEdit_register_passwd2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_register_passwd2.setObjectName("lineEdit_register_passwd2")
        self.verticalLayout_5.addWidget(self.lineEdit_register_passwd2)
        self.pushButton_4 = QtWidgets.QPushButton(self.page_register)
        self.pushButton_4.setStyleSheet("font: 10pt \"Algerian\";")
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_5.addWidget(self.pushButton_4)
        self.stackedWidget.addWidget(self.page_register)
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setObjectName("page_7")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.page_7)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 20, 541, 211))
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.stackedWidget.addWidget(self.page_7)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.page_5)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.lineEdit_login_phone_2 = QtWidgets.QLineEdit(self.page_5)
        self.lineEdit_login_phone_2.setMinimumSize(QtCore.QSize(0, 50))
        self.lineEdit_login_phone_2.setObjectName("lineEdit_login_phone_2")
        self.verticalLayout_7.addWidget(self.lineEdit_login_phone_2)
        self.lineEdit_login_passwd_2 = QtWidgets.QLineEdit(self.page_5)
        self.lineEdit_login_passwd_2.setMinimumSize(QtCore.QSize(0, 50))
        self.lineEdit_login_passwd_2.setStyleSheet("")
        self.lineEdit_login_passwd_2.setText("")
        self.lineEdit_login_passwd_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_login_passwd_2.setObjectName("lineEdit_login_passwd_2")
        self.verticalLayout_7.addWidget(self.lineEdit_login_passwd_2)
        self.pushButton_admin_2 = QtWidgets.QPushButton(self.page_5)
        self.pushButton_admin_2.setStyleSheet("font: 12pt \"Algerian\";")
        self.pushButton_admin_2.setObjectName("pushButton_admin_2")
        self.verticalLayout_7.addWidget(self.pushButton_admin_2)
        self.stackedWidget.addWidget(self.page_5)
        self.verticalLayout_4.addWidget(self.stackedWidget)
        self.verticalLayout_2.addWidget(self.frame_10)
        self.frame_9 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_13 = QtWidgets.QFrame(self.frame_9)
        self.frame_13.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"}\n"
"QPushButton:pressed{\n"
"    padding-top：5px;\n"
"    padding-left:5px;\n"
"}")
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_13)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButton_admin = QtWidgets.QPushButton(self.frame_13)
        self.pushButton_admin.setObjectName("pushButton_admin")
        self.horizontalLayout_6.addWidget(self.pushButton_admin)
        self.pushButton_login = QtWidgets.QPushButton(self.frame_13)
        self.pushButton_login.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon/登录.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_login.setIcon(icon)
        self.pushButton_login.setObjectName("pushButton_login")
        self.horizontalLayout_6.addWidget(self.pushButton_login)
        self.pushButton_exit = QtWidgets.QPushButton(self.frame_13)
        self.pushButton_exit.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/icon/退出,出.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_exit.setIcon(icon1)
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.horizontalLayout_6.addWidget(self.pushButton_exit)
        self.pushButton_register = QtWidgets.QPushButton(self.frame_13)
        self.pushButton_register.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/icon/注册.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_register.setIcon(icon2)
        self.pushButton_register.setObjectName("pushButton_register")
        self.horizontalLayout_6.addWidget(self.pushButton_register)
        self.verticalLayout_3.addWidget(self.frame_13)
        self.frame_14 = QtWidgets.QFrame(self.frame_9)
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_14)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.frame_14)
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.stackedWidget_2.addWidget(self.page)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.label_4 = QtWidgets.QLabel(self.page_4)
        self.label_4.setGeometry(QtCore.QRect(210, 10, 171, 16))
        self.label_4.setObjectName("label_4")
        self.stackedWidget_2.addWidget(self.page_4)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.label_3 = QtWidgets.QLabel(self.page_3)
        self.label_3.setGeometry(QtCore.QRect(150, 0, 171, 31))
        self.label_3.setObjectName("label_3")
        self.stackedWidget_2.addWidget(self.page_3)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label_2 = QtWidgets.QLabel(self.page_2)
        self.label_2.setGeometry(QtCore.QRect(200, 10, 131, 16))
        self.label_2.setObjectName("label_2")
        self.stackedWidget_2.addWidget(self.page_2)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.label_5 = QtWidgets.QLabel(self.page_6)
        self.label_5.setGeometry(QtCore.QRect(100, 1, 361, 21))
        self.label_5.setObjectName("label_5")
        self.stackedWidget_2.addWidget(self.page_6)
        self.horizontalLayout_4.addWidget(self.stackedWidget_2)
        self.verticalLayout_3.addWidget(self.frame_14)
        self.verticalLayout_2.addWidget(self.frame_9)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(80, 190, 571, 471))
        self.frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"border-radius:40px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_4 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_3 = QtWidgets.QFrame(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setStyleSheet("border-image: url(:/icon/icon/EC_文档-体育娱乐.png);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout.addWidget(self.frame_3)
        self.frame_6 = QtWidgets.QFrame(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(6)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.frame_6)
        self.label.setStyleSheet("font: 87 12pt \"Arial Black\";\n"
"")
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.horizontalLayout.addWidget(self.frame_6)
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(7)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_7 = QtWidgets.QFrame(self.frame_5)
        self.frame_7.setStyleSheet("border-image: url(:/icon/icon/体育锻炼.png);")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_3.addWidget(self.frame_7)
        self.verticalLayout.addWidget(self.frame_5)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        self.stackedWidget_2.setCurrentIndex(1)
        self.pushButton_exit.clicked.connect(MainWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit_login_phone.setPlaceholderText(_translate("MainWindow", "Phone number"))
        self.lineEdit_login_passwd.setPlaceholderText(_translate("MainWindow", "Password"))
        self.pushButton_3.setText(_translate("MainWindow", "确认"))
        self.lineEdit_register_phone.setPlaceholderText(_translate("MainWindow", "Phone number"))
        self.lineEdit_register_passwd.setPlaceholderText(_translate("MainWindow", "Password"))
        self.lineEdit_register_passwd2.setPlaceholderText(_translate("MainWindow", "Sure Password"))
        self.pushButton_4.setText(_translate("MainWindow", "注册"))
        self.lineEdit_login_phone_2.setPlaceholderText(_translate("MainWindow", "admin_Phone number"))
        self.lineEdit_login_passwd_2.setPlaceholderText(_translate("MainWindow", "Password"))
        self.pushButton_admin_2.setText(_translate("MainWindow", "确认"))
        self.pushButton_admin.setText(_translate("MainWindow", "管理员登入"))
        self.label_4.setText(_translate("MainWindow", "密码不一致或密码不能为空"))
        self.label_3.setText(_translate("MainWindow", "注册成功，请返回登录界面"))
        self.label_2.setText(_translate("MainWindow", "账号密码错误"))
        self.label_5.setText(_translate("MainWindow", "账号已存在或手机号必须为11位！"))
        self.label.setText(_translate("MainWindow", "Stadium reservation system"))
import ress_rc