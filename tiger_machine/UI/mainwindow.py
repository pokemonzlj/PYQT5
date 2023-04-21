# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(755, 590)
        MainWindow.setMinimumSize(QtCore.QSize(755, 590))
        MainWindow.setMaximumSize(QtCore.QSize(755, 590))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(72, 72, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(8, 196, 248))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 72, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(8, 196, 248))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 72, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(8, 196, 248))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(8, 196, 248))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.start_play_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_play_button.setGeometry(QtCore.QRect(640, 500, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.start_play_button.setFont(font)
        self.start_play_button.setObjectName("start_play_button")
        self.pic1 = QtWidgets.QLabel(self.centralwidget)
        self.pic1.setGeometry(QtCore.QRect(100, 60, 120, 120))
        self.pic1.setText("")
        self.pic1.setObjectName("pic1")
        self.pic2 = QtWidgets.QLabel(self.centralwidget)
        self.pic2.setGeometry(QtCore.QRect(100, 180, 120, 120))
        self.pic2.setText("")
        self.pic2.setObjectName("pic2")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(220, 50, 20, 381))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(360, 50, 20, 381))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.pic3 = QtWidgets.QLabel(self.centralwidget)
        self.pic3.setGeometry(QtCore.QRect(100, 300, 120, 120))
        self.pic3.setText("")
        self.pic3.setObjectName("pic3")
        self.pic4 = QtWidgets.QLabel(self.centralwidget)
        self.pic4.setGeometry(QtCore.QRect(240, 60, 120, 120))
        self.pic4.setText("")
        self.pic4.setObjectName("pic4")
        self.pic5 = QtWidgets.QLabel(self.centralwidget)
        self.pic5.setGeometry(QtCore.QRect(240, 180, 120, 120))
        self.pic5.setText("")
        self.pic5.setObjectName("pic5")
        self.pic6 = QtWidgets.QLabel(self.centralwidget)
        self.pic6.setGeometry(QtCore.QRect(240, 300, 120, 120))
        self.pic6.setText("")
        self.pic6.setObjectName("pic6")
        self.pic7 = QtWidgets.QLabel(self.centralwidget)
        self.pic7.setGeometry(QtCore.QRect(380, 60, 120, 120))
        self.pic7.setText("")
        self.pic7.setObjectName("pic7")
        self.pic8 = QtWidgets.QLabel(self.centralwidget)
        self.pic8.setGeometry(QtCore.QRect(380, 180, 120, 120))
        self.pic8.setText("")
        self.pic8.setObjectName("pic8")
        self.pic9 = QtWidgets.QLabel(self.centralwidget)
        self.pic9.setGeometry(QtCore.QRect(380, 300, 120, 120))
        self.pic9.setText("")
        self.pic9.setObjectName("pic9")
        self.score = QtWidgets.QTextEdit(self.centralwidget)
        self.score.setEnabled(True)
        self.score.setGeometry(QtCore.QRect(650, 10, 91, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.score.sizePolicy().hasHeightForWidth())
        self.score.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(131, 131, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(189, 189, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(131, 131, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(189, 189, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.score.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.score.setFont(font)
        self.score.setAcceptDrops(True)
        self.score.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.score.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.score.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.score.setReadOnly(True)
        self.score.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.score.setObjectName("score")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(583, 9, 61, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.use_money_amount = QtWidgets.QSpinBox(self.centralwidget)
        self.use_money_amount.setGeometry(QtCore.QRect(520, 510, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.use_money_amount.setFont(font)
        self.use_money_amount.setMinimum(1)
        self.use_money_amount.setMaximum(20)
        self.use_money_amount.setObjectName("use_money_amount")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(450, 510, 61, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(200, 10, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Roman")
        font.setPointSize(16)
        font.setItalic(True)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(80, 50, 20, 381))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(500, 50, 20, 381))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(570, 130, 101, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(570, 190, 101, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(570, 250, 121, 16))
        self.label_6.setObjectName("label_6")
        self.play_recorder = QtWidgets.QTextEdit(self.centralwidget)
        self.play_recorder.setEnabled(True)
        self.play_recorder.setGeometry(QtCore.QRect(30, 460, 381, 101))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        self.play_recorder.setFont(font)
        self.play_recorder.setReadOnly(True)
        self.play_recorder.setMarkdown("")
        self.play_recorder.setObjectName("play_recorder")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(30, 440, 91, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(570, 280, 121, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(570, 310, 91, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(570, 220, 101, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(570, 160, 101, 16))
        self.label_11.setObjectName("label_11")
        self.recharge_button = QtWidgets.QPushButton(self.centralwidget)
        self.recharge_button.setGeometry(QtCore.QRect(500, 10, 75, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(156, 0, 234))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(156, 0, 234))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.recharge_button.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.recharge_button.setFont(font)
        self.recharge_button.setObjectName("recharge_button")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(540, 100, 191, 20))
        self.label_12.setObjectName("label_12")
        self.huangou = QtWidgets.QPushButton(self.centralwidget)
        self.huangou.setGeometry(QtCore.QRect(570, 340, 121, 91))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(240, 78, 14))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 121, 17))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 78, 14))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 121, 17))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 78, 14))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.huangou.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.huangou.setFont(font)
        self.huangou.setObjectName("huangou")
        self.wangzheng_same3_money = QtWidgets.QLabel(self.centralwidget)
        self.wangzheng_same3_money.setGeometry(QtCore.QRect(660, 160, 54, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.wangzheng_same3_money.setFont(font)
        self.wangzheng_same3_money.setObjectName("wangzheng_same3_money")
        self.wangzheng_renyi9_money = QtWidgets.QLabel(self.centralwidget)
        self.wangzheng_renyi9_money.setGeometry(QtCore.QRect(660, 190, 54, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.wangzheng_renyi9_money.setFont(font)
        self.wangzheng_renyi9_money.setObjectName("wangzheng_renyi9_money")
        self.wangzheng_same9_money = QtWidgets.QLabel(self.centralwidget)
        self.wangzheng_same9_money.setGeometry(QtCore.QRect(660, 220, 54, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.wangzheng_same9_money.setFont(font)
        self.wangzheng_same9_money.setObjectName("wangzheng_same9_money")
        self.kfc_danpin3_money = QtWidgets.QLabel(self.centralwidget)
        self.kfc_danpin3_money.setGeometry(QtCore.QRect(683, 250, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.kfc_danpin3_money.setFont(font)
        self.kfc_danpin3_money.setObjectName("kfc_danpin3_money")
        self.kfc_taocan3_money = QtWidgets.QLabel(self.centralwidget)
        self.kfc_taocan3_money.setGeometry(QtCore.QRect(683, 280, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.kfc_taocan3_money.setFont(font)
        self.kfc_taocan3_money.setObjectName("kfc_taocan3_money")
        self.kfc_same9_money = QtWidgets.QLabel(self.centralwidget)
        self.kfc_same9_money.setGeometry(QtCore.QRect(653, 310, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.kfc_same9_money.setFont(font)
        self.kfc_same9_money.setObjectName("kfc_same9_money")
        self.wangzheng_renyi3_money = QtWidgets.QLabel(self.centralwidget)
        self.wangzheng_renyi3_money.setGeometry(QtCore.QRect(660, 130, 54, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.wangzheng_renyi3_money.setFont(font)
        self.wangzheng_renyi3_money.setObjectName("wangzheng_renyi3_money")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.start_play_button.setText(_translate("MainWindow", "开始"))
        self.score.setMarkdown(_translate("MainWindow", "**9999**\n"
"\n"
""))
        self.score.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:13pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:8px; margin-bottom:8px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">9999</p></body></html>"))
        self.label.setText(_translate("MainWindow", "剩余金额："))
        self.label_2.setText(_translate("MainWindow", "投注金额："))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600; color:#e60000;\">王政KFC老虎机</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#5500ff;\">任意王政*3=</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#5500ff;\">任意王政*9=</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#5500ff;\">同款KFC单品*3=</span></p></body></html>"))
        self.play_recorder.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Agency FB\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p>游玩记录：</p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#5500ff;\">同款KFC套餐*3=</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#5500ff;\">同款KFC*9=</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#5500ff;\">同款王政*9=</span></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#5500ff;\">同款王政*3=</span></p></body></html>"))
        self.recharge_button.setText(_translate("MainWindow", "点我充值"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#4700d4;\">任意横、纵、对角线满足：</span></p></body></html>"))
        self.huangou.setText(_translate("MainWindow", "KFC套餐换购"))
        self.wangzheng_same3_money.setText(_translate("MainWindow", "1"))
        self.wangzheng_renyi9_money.setText(_translate("MainWindow", "1"))
        self.wangzheng_same9_money.setText(_translate("MainWindow", "1"))
        self.kfc_danpin3_money.setText(_translate("MainWindow", "1"))
        self.kfc_taocan3_money.setText(_translate("MainWindow", "1"))
        self.kfc_same9_money.setText(_translate("MainWindow", "1"))
        self.wangzheng_renyi3_money.setText(_translate("MainWindow", "1"))