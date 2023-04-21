# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'small_game_zhuangbeilan_ui.ui'
#
# Created: Fri Dec 04 17:54:34 2020
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

class Ui_Form_zhuangbeilan(object):
    def setupUi(self, Form_zhuangbeilan):
        Form_zhuangbeilan.setObjectName(_fromUtf8("Form_zhuangbeilan"))
        Form_zhuangbeilan.resize(400, 300)
        self.label_11 = QtGui.QLabel(Form_zhuangbeilan)
        self.label_11.setGeometry(QtCore.QRect(90, 10, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label = QtGui.QLabel(Form_zhuangbeilan)
        self.label.setGeometry(QtCore.QRect(30, 50, 81, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.leixing = QtGui.QComboBox(Form_zhuangbeilan)
        self.leixing.setGeometry(QtCore.QRect(120, 50, 69, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.leixing.setFont(font)
        self.leixing.setObjectName(_fromUtf8("leixing"))
        self.leixing.addItem(_fromUtf8(""))
        self.leixing.addItem(_fromUtf8(""))
        self.zhuangbei_list = QtGui.QComboBox(Form_zhuangbeilan)
        self.zhuangbei_list.setGeometry(QtCore.QRect(120, 100, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.zhuangbei_list.setFont(font)
        self.zhuangbei_list.setObjectName(_fromUtf8("zhuangbei_list"))
        self.label_2 = QtGui.QLabel(Form_zhuangbeilan)
        self.label_2.setGeometry(QtCore.QRect(40, 100, 61, 31))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Form_zhuangbeilan)
        self.label_3.setGeometry(QtCore.QRect(40, 150, 61, 31))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.fumoxiaoguo = QtGui.QLineEdit(Form_zhuangbeilan)
        self.fumoxiaoguo.setGeometry(QtCore.QRect(120, 150, 251, 31))
        self.fumoxiaoguo.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.fumoxiaoguo.setReadOnly(True)
        self.fumoxiaoguo.setObjectName(_fromUtf8("fumoxiaoguo"))
        self.maichu = QtGui.QPushButton(Form_zhuangbeilan)
        self.maichu.setGeometry(QtCore.QRect(40, 250, 75, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(203, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(203, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.maichu.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.maichu.setFont(font)
        self.maichu.setObjectName(_fromUtf8("maichu"))
        self.zhuangbei = QtGui.QPushButton(Form_zhuangbeilan)
        self.zhuangbei.setGeometry(QtCore.QRect(160, 250, 75, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.zhuangbei.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.zhuangbei.setFont(font)
        self.zhuangbei.setObjectName(_fromUtf8("zhuangbei"))
        self.tuichu = QtGui.QPushButton(Form_zhuangbeilan)
        self.tuichu.setGeometry(QtCore.QRect(280, 250, 75, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.tuichu.setFont(font)
        self.tuichu.setObjectName(_fromUtf8("tuichu"))
        self.label_4 = QtGui.QLabel(Form_zhuangbeilan)
        self.label_4.setGeometry(QtCore.QRect(40, 200, 61, 31))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.naijiu = QtGui.QLineEdit(Form_zhuangbeilan)
        self.naijiu.setGeometry(QtCore.QRect(120, 200, 71, 31))
        self.naijiu.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.naijiu.setReadOnly(True)
        self.naijiu.setObjectName(_fromUtf8("naijiu"))

        self.retranslateUi(Form_zhuangbeilan)
        QtCore.QMetaObject.connectSlotsByName(Form_zhuangbeilan)

    def retranslateUi(self, Form_zhuangbeilan):
        Form_zhuangbeilan.setWindowTitle(_translate("Form_zhuangbeilan", "Form", None))
        self.label_11.setText(_translate("Form_zhuangbeilan", "<html><head/><body><p><span style=\" font-size:16pt; color:#2037cc;\">装     备     栏</span></p></body></html>", None))
        self.label.setText(_translate("Form_zhuangbeilan", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">选择装备类型</span></p></body></html>", None))
        self.leixing.setItemText(0, _translate("Form_zhuangbeilan", "武器", None))
        self.leixing.setItemText(1, _translate("Form_zhuangbeilan", "防具", None))
        self.label_2.setText(_translate("Form_zhuangbeilan", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">选择装备</span></p></body></html>", None))
        self.label_3.setText(_translate("Form_zhuangbeilan", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">附魔效果</span></p></body></html>", None))
        self.maichu.setText(_translate("Form_zhuangbeilan", "贱卖", None))
        self.zhuangbei.setText(_translate("Form_zhuangbeilan", "装备", None))
        self.tuichu.setText(_translate("Form_zhuangbeilan", "退出", None))
        self.label_4.setText(_translate("Form_zhuangbeilan", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">剩余耐久</span></p></body></html>", None))

