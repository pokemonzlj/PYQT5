# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'small_game_shuxing_ui.ui'
#
# Created: Fri Dec 04 17:54:50 2020
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form_shuxingjiadian(object):
    def setupUi(self, Form_shuxingjiadian):
        Form_shuxingjiadian.setObjectName(_fromUtf8("Form_shuxingjiadian"))
        Form_shuxingjiadian.resize(399, 300)
        Form_shuxingjiadian.setMaximumSize(QtCore.QSize(400, 300))
        self.label = QtGui.QLabel(Form_shuxingjiadian)
        self.label.setGeometry(QtCore.QRect(50, 80, 31, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form_shuxingjiadian)
        self.label_2.setGeometry(QtCore.QRect(50, 130, 31, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Form_shuxingjiadian)
        self.label_3.setGeometry(QtCore.QRect(50, 180, 31, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Form_shuxingjiadian)
        self.label_4.setGeometry(QtCore.QRect(210, 80, 31, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Form_shuxingjiadian)
        self.label_5.setGeometry(QtCore.QRect(210, 130, 46, 21))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(Form_shuxingjiadian)
        self.label_6.setGeometry(QtCore.QRect(210, 180, 46, 21))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(Form_shuxingjiadian)
        self.label_7.setGeometry(QtCore.QRect(210, 30, 41, 21))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(Form_shuxingjiadian)
        self.label_8.setGeometry(QtCore.QRect(50, 30, 31, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(Form_shuxingjiadian)
        self.label_9.setGeometry(QtCore.QRect(50, 230, 41, 21))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.name = QtGui.QLineEdit(Form_shuxingjiadian)
        self.name.setGeometry(QtCore.QRect(90, 30, 111, 20))
        self.name.setAlignment(QtCore.Qt.AlignCenter)
        self.name.setReadOnly(True)
        self.name.setObjectName(_fromUtf8("name"))
        self.yili = QtGui.QSpinBox(Form_shuxingjiadian)
        self.yili.setGeometry(QtCore.QRect(90, 230, 42, 22))
        self.yili.setAlignment(QtCore.Qt.AlignCenter)
        self.yili.setReadOnly(False)
        self.yili.setMaximum(1000)
        self.yili.setObjectName(_fromUtf8("yili"))
        self.jiqiao = QtGui.QSpinBox(Form_shuxingjiadian)
        self.jiqiao.setGeometry(QtCore.QRect(90, 180, 42, 22))
        self.jiqiao.setAlignment(QtCore.Qt.AlignCenter)
        self.jiqiao.setReadOnly(False)
        self.jiqiao.setMaximum(1000)
        self.jiqiao.setObjectName(_fromUtf8("jiqiao"))
        self.fali = QtGui.QSpinBox(Form_shuxingjiadian)
        self.fali.setGeometry(QtCore.QRect(90, 130, 42, 22))
        self.fali.setAlignment(QtCore.Qt.AlignCenter)
        self.fali.setReadOnly(False)
        self.fali.setMaximum(1000)
        self.fali.setObjectName(_fromUtf8("fali"))
        self.hp = QtGui.QSpinBox(Form_shuxingjiadian)
        self.hp.setGeometry(QtCore.QRect(90, 80, 42, 22))
        self.hp.setAlignment(QtCore.Qt.AlignCenter)
        self.hp.setReadOnly(False)
        self.hp.setMaximum(1000)
        self.hp.setObjectName(_fromUtf8("hp"))
        self.liliang = QtGui.QSpinBox(Form_shuxingjiadian)
        self.liliang.setGeometry(QtCore.QRect(260, 80, 42, 22))
        self.liliang.setAlignment(QtCore.Qt.AlignCenter)
        self.liliang.setReadOnly(False)
        self.liliang.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.liliang.setMaximum(1000)
        self.liliang.setObjectName(_fromUtf8("liliang"))
        self.minjie = QtGui.QSpinBox(Form_shuxingjiadian)
        self.minjie.setGeometry(QtCore.QRect(260, 130, 42, 22))
        self.minjie.setAlignment(QtCore.Qt.AlignCenter)
        self.minjie.setReadOnly(False)
        self.minjie.setMaximum(1000)
        self.minjie.setObjectName(_fromUtf8("minjie"))
        self.xingyun = QtGui.QSpinBox(Form_shuxingjiadian)
        self.xingyun.setGeometry(QtCore.QRect(260, 180, 42, 22))
        self.xingyun.setAlignment(QtCore.Qt.AlignCenter)
        self.xingyun.setReadOnly(False)
        self.xingyun.setMaximum(1000)
        self.xingyun.setObjectName(_fromUtf8("xingyun"))
        self.queren = QtGui.QPushButton(Form_shuxingjiadian)
        self.queren.setGeometry(QtCore.QRect(220, 240, 75, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(43, 166, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(43, 166, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.queren.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.queren.setFont(font)
        self.queren.setObjectName(_fromUtf8("queren"))
        self.tuichu = QtGui.QPushButton(Form_shuxingjiadian)
        self.tuichu.setGeometry(QtCore.QRect(310, 240, 75, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.tuichu.setFont(font)
        self.tuichu.setObjectName(_fromUtf8("tuichu"))
        self.shuxingdian = QtGui.QLineEdit(Form_shuxingjiadian)
        self.shuxingdian.setGeometry(QtCore.QRect(260, 30, 51, 20))
        self.shuxingdian.setAlignment(QtCore.Qt.AlignCenter)
        self.shuxingdian.setReadOnly(True)
        self.shuxingdian.setObjectName(_fromUtf8("shuxingdian"))

        self.retranslateUi(Form_shuxingjiadian)
        QtCore.QMetaObject.connectSlotsByName(Form_shuxingjiadian)

    def retranslateUi(self, Form_shuxingjiadian):
        Form_shuxingjiadian.setWindowTitle(_translate("Form_shuxingjiadian", "Form", None))
        self.label.setText(_translate("Form_shuxingjiadian", "<html><head/><body><p><span style=\" font-weight:600; color:#b300b3;\">HP</span></p></body></html>", None))
        self.label_2.setText(_translate("Form_shuxingjiadian", "<html><head/><body><p><span style=\" font-weight:600; color:#b300b3;\">法力</span></p></body></html>", None))
        self.label_3.setText(_translate("Form_shuxingjiadian", "<html><head/><body><p><span style=\" font-weight:600; color:#b300b3;\">技巧</span></p></body></html>", None))
        self.label_4.setText(_translate("Form_shuxingjiadian", "<html><head/><body><p><span style=\" font-weight:600; color:#b300b3;\">力量</span></p></body></html>", None))
        self.label_5.setText(_translate("Form_shuxingjiadian", "<html><head/><body><p><span style=\" font-weight:600; color:#b300b3;\">敏捷</span></p></body></html>", None))
        self.label_6.setText(_translate("Form_shuxingjiadian", "<html><head/><body><p><span style=\" font-weight:600; color:#b300b3;\">幸运</span></p></body></html>", None))
        self.label_7.setText(_translate("Form_shuxingjiadian", "<html><head/><body><p><span style=\" font-weight:600; color:#2ba636;\">属性点</span></p></body></html>", None))
        self.label_8.setText(_translate("Form_shuxingjiadian", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">角色</span></p></body></html>", None))
        self.label_9.setText(_translate("Form_shuxingjiadian", "<html><head/><body><p><span style=\" font-weight:600; color:#b300b3;\">毅力</span></p></body></html>", None))
        self.queren.setText(_translate("Form_shuxingjiadian", "确认加点", None))
        self.tuichu.setText(_translate("Form_shuxingjiadian", "退出", None))

