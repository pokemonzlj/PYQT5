# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'huangou_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WEBview(object):
    def setupUi(self, WEBview):
        WEBview.setObjectName("WEBview")
        WEBview.setWindowModality(QtCore.Qt.NonModal)
        WEBview.resize(1112, 720)
        self.textBrowser = QtWidgets.QTextBrowser(WEBview)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 256, 192))
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(WEBview)
        QtCore.QMetaObject.connectSlotsByName(WEBview)

    def retranslateUi(self, WEBview):
        _translate = QtCore.QCoreApplication.translate
        WEBview.setWindowTitle(_translate("WEBview", "Form"))
        self.textBrowser.setHtml(_translate("WEBview", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#d42013;\">王政正在合作洽谈中！</span></p></body></html>"))