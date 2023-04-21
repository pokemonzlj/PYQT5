# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'small_game_xinjian_ui.ui'
#
# Created: Fri Dec 04 17:54:40 2020
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

class Ui_Form_xinjian(object):
    def setupUi(self, Form_xinjian):
        Form_xinjian.setObjectName(_fromUtf8("Form_xinjian"))
        Form_xinjian.resize(380, 240)
        Form_xinjian.setMinimumSize(QtCore.QSize(380, 240))
        Form_xinjian.setMaximumSize(QtCore.QSize(380, 240))
        self.label = QtGui.QLabel(Form_xinjian)
        self.label.setGeometry(QtCore.QRect(20, 50, 101, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.name = QtGui.QLineEdit(Form_xinjian)
        self.name.setGeometry(QtCore.QRect(130, 50, 131, 31))
        self.name.setReadOnly(False)
        self.name.setObjectName(_fromUtf8("name"))
        self.zhudongfenpei = QtGui.QPushButton(Form_xinjian)
        self.zhudongfenpei.setGeometry(QtCore.QRect(140, 180, 91, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.zhudongfenpei.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.zhudongfenpei.setFont(font)
        self.zhudongfenpei.setObjectName(_fromUtf8("zhudongfenpei"))
        self.qvxiao = QtGui.QPushButton(Form_xinjian)
        self.qvxiao.setGeometry(QtCore.QRect(260, 180, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.qvxiao.setFont(font)
        self.qvxiao.setObjectName(_fromUtf8("qvxiao"))
        self.label_2 = QtGui.QLabel(Form_xinjian)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 351, 91))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.touxiang = QtGui.QLabel(Form_xinjian)
        self.touxiang.setGeometry(QtCore.QRect(190, 110, 71, 71))
        self.touxiang.setText(_fromUtf8(""))
        self.touxiang.setObjectName(_fromUtf8("touxiang"))
        self.suijifenpei = QtGui.QPushButton(Form_xinjian)
        self.suijifenpei.setGeometry(QtCore.QRect(20, 180, 91, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.suijifenpei.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.suijifenpei.setFont(font)
        self.suijifenpei.setObjectName(_fromUtf8("suijifenpei"))

        self.retranslateUi(Form_xinjian)
        QtCore.QMetaObject.connectSlotsByName(Form_xinjian)

    def retranslateUi(self, Form_xinjian):
        Form_xinjian.setWindowTitle(_translate("Form_xinjian", "Form", None))
        self.label.setText(_translate("Form_xinjian", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">输入角色名：</span></p></body></html>", None))
        self.zhudongfenpei.setText(_translate("Form_xinjian", "主动分配", None))
        self.qvxiao.setText(_translate("Form_xinjian", "取消", None))
        self.label_2.setText(_translate("Form_xinjian", "<html><head/><body><p><span style=\" font-size:12pt; color:#f10000;\">1.初始属性为10点HP,10点属性点供分配</span></p><p><span style=\" font-size:12pt; color:#f10000;\">2.选择随机分配增加3点属性点，随机分配属性点</span></p></body></html>", None))
        self.suijifenpei.setText(_translate("Form_xinjian", "随机分配", None))

