import os
import re
import sys
import time
from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets
# pip install PyQtWebEngine
# from PyQt5.QtWebEngineWidgets import QWebEngineView
# from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from UI.mainwindow import Ui_MainWindow
from houduan.houduan import houduan
from UI.huangou_window import Ui_WEBview


class qianduan(QMainWindow, Ui_MainWindow, houduan):
    def __init__(self, parent=None):
        super(qianduan, self).__init__(parent)
        self.setupUi(self)
        houduan.__init__(self)
        self.huangou_window = huangou_window
        self.set_default_pic()
        self.set_money_display()
        self.use_money = 1
        self.current_pic1 = ''
        self.current_pic2 = ''
        self.current_pic3 = ''
        self.current_pic4 = ''
        self.current_pic5 = ''
        self.current_pic6 = ''
        self.current_pic7 = ''
        self.current_pic8 = ''
        self.current_pic9 = ''
        self.score.setText(str(self.current_money))
        self.start_play_button.clicked.connect(lambda: self.start_play())
        self.recharge_button.clicked.connect(lambda: self.charge())
        self.huangou.clicked.connect(lambda: self.open_webview())

    def set_pic(self):
        """为9个位置的图片设置一轮图片显示"""
        if self.current_pic1:
            self.pic1.setPixmap(QtGui.QPixmap(self.current_pic1))
        if self.current_pic2:
            self.pic2.setPixmap(QtGui.QPixmap(self.current_pic2))
        if self.current_pic3:
            self.pic3.setPixmap(QtGui.QPixmap(self.current_pic3))
        if self.current_pic4:
            self.pic4.setPixmap(QtGui.QPixmap(self.current_pic4))
        if self.current_pic5:
            self.pic5.setPixmap(QtGui.QPixmap(self.current_pic5))
        if self.current_pic6:
            self.pic6.setPixmap(QtGui.QPixmap(self.current_pic6))
        if self.current_pic7:
            self.pic7.setPixmap(QtGui.QPixmap(self.current_pic7))
        if self.current_pic8:
            self.pic8.setPixmap(QtGui.QPixmap(self.current_pic8))
        if self.current_pic9:
            self.pic9.setPixmap(QtGui.QPixmap(self.current_pic9))

    def set_default_pic(self):
        # for i in range(9):
        self.current_pic1 = self.random_pic()
        self.pic1.setPixmap(QtGui.QPixmap(self.current_pic1))
        self.current_pic2 = self.random_pic()
        self.pic2.setPixmap(QtGui.QPixmap(self.current_pic2))
        self.current_pic3 = self.random_pic()
        self.pic3.setPixmap(QtGui.QPixmap(self.current_pic3))
        self.current_pic4 = self.random_pic()
        self.pic4.setPixmap(QtGui.QPixmap(self.current_pic4))
        self.current_pic5 = self.random_pic()
        self.pic5.setPixmap(QtGui.QPixmap(self.current_pic5))
        self.current_pic6 = self.random_pic()
        self.pic6.setPixmap(QtGui.QPixmap(self.current_pic6))
        self.current_pic7 = self.random_pic()
        self.pic7.setPixmap(QtGui.QPixmap(self.current_pic7))
        self.current_pic8 = self.random_pic()
        self.pic8.setPixmap(QtGui.QPixmap(self.current_pic8))
        self.current_pic9 = self.random_pic()
        self.pic9.setPixmap(QtGui.QPixmap(self.current_pic9))

    def set_money_display(self):
        """设置倍率金额的显示"""
        self.wangzheng_same3_money.setText(str(self.money_rate['wangzheng_same3']))
        self.wangzheng_renyi9_money.setText(str(self.money_rate['wangzheng_renyi9']))
        self.wangzheng_renyi3_money.setText(str(self.money_rate['wangzheng_renyi3']))
        self.wangzheng_same9_money.setText(str(self.money_rate['wangzheng_same9']))
        self.kfc_danpin3_money.setText(str(self.money_rate['kfc_danpin3']))
        self.kfc_taocan3_money.setText(str(self.money_rate['kfc_taocan3']))
        self.kfc_same9_money.setText(str(self.money_rate['kfc_same9']))

    def one_move_line1(self):
        """替换一轮图片的动作"""
        new_pic3 = self.random_pic()
        self.current_pic1 = self.current_pic2
        self.current_pic2 = self.current_pic3
        self.current_pic3 = new_pic3
        # self.set_pic()
        # QApplication.processEvents()

    def one_move_line2(self):
        new_pic6 = self.random_pic()
        self.current_pic4 = self.current_pic5
        self.current_pic5 = self.current_pic6
        self.current_pic6 = new_pic6
        # self.set_pic()
        # QApplication.processEvents()

    def one_move_line3(self):
        new_pic9 = self.random_pic()
        self.current_pic7 = self.current_pic8
        self.current_pic8 = self.current_pic9
        self.current_pic9 = new_pic9
        # self.set_pic()
        # QApplication.processEvents()

    def whole_move(self, times=10):
        """一轮完整的滚动，times控制单次运行的次数"""
        for i in range(times):
            self.one_move_line1()
            self.one_move_line2()
            self.one_move_line3()
            self.set_pic()
            time.sleep(0.1)
            QApplication.processEvents()
        for i in range(10):
            if i%4 == 0:
                self.one_move_line1()
            self.one_move_line2()
            self.one_move_line3()
            self.set_pic()
            time.sleep(0.1)
            QApplication.processEvents()
        for i in range(6):
            self.one_move_line2()
            self.one_move_line3()
            self.set_pic()
            time.sleep(0.1)
            QApplication.processEvents()
        for i in range(10):
            if i%4 == 0:
                self.one_move_line2()
            self.one_move_line3()
            self.set_pic()
            time.sleep(0.1)
            QApplication.processEvents()
        for i in range(6):
            self.one_move_line3()
            self.set_pic()
            time.sleep(0.1)
            QApplication.processEvents()
        for i in range(10):
            if i % 4 == 0:
                self.one_move_line3()
            self.set_pic()
            time.sleep(0.1)
            QApplication.processEvents()

    def deduction_money(self):
        """用于点击开始前扣除余额"""
        use_money = self.use_money_amount.text()
        self.use_money = int(use_money)
        if self.current_money >= self.use_money:
            self.current_money -= self.use_money
            self.score.setText(str(self.current_money))
            return True
        else:
            QtWidgets.QMessageBox.information(self, u'通知', u'您的余额不足，请充值！')
            return False


    def calculate_reward(self, use_money=1):
        xiaofei = ("消费%s代币," % use_money)
        rate = 0  # 最后的总结算倍率
        if self.get_pic_type(self.current_pic1) == self.get_pic_type(self.current_pic2) == self.get_pic_type(
                self.current_pic3):
            if self.get_pic_type(self.current_pic1) == 'wangzheng':
                if self.current_pic1 == self.current_pic2 == self.current_pic3:
                    rate += self.money_rate['wangzheng_same3']
                else:
                    rate += self.money_rate['wangzheng_renyi3']
            elif self.get_pic_type(self.current_pic1) == 'kfc_danpin':
                if self.current_pic1 == self.current_pic2 == self.current_pic3:
                    rate += self.money_rate['kfc_danpin3']
            elif self.get_pic_type(self.current_pic1) == 'kfc_taocan':
                if self.current_pic1 == self.current_pic2 == self.current_pic3:
                    rate += self.money_rate['kfc_taocan3']
        if self.get_pic_type(self.current_pic1) == self.get_pic_type(self.current_pic4) == self.get_pic_type(
                self.current_pic7):
            if self.get_pic_type(self.current_pic1) == 'wangzheng':
                if self.current_pic1 == self.current_pic4 == self.current_pic7:
                    rate += self.money_rate['wangzheng_same3']
                else:
                    rate += self.money_rate['wangzheng_renyi3']
            elif self.get_pic_type(self.current_pic1) == 'kfc_danpin':
                if self.current_pic1 == self.current_pic4 == self.current_pic7:
                    rate += self.money_rate['kfc_danpin3']
            elif self.get_pic_type(self.current_pic1) == 'kfc_taocan':
                if self.current_pic1 == self.current_pic4 == self.current_pic7:
                    rate += self.money_rate['kfc_taocan3']
        if self.get_pic_type(self.current_pic1) == self.get_pic_type(self.current_pic5) == self.get_pic_type(
                self.current_pic9):
            if self.get_pic_type(self.current_pic1) == 'wangzheng':
                if self.current_pic1 == self.current_pic5 == self.current_pic9:
                    rate += self.money_rate['wangzheng_same3']
                else:
                    rate += self.money_rate['wangzheng_renyi3']
            elif self.get_pic_type(self.current_pic1) == 'kfc_danpin':
                if self.current_pic1 == self.current_pic5 == self.current_pic9:
                    rate += self.money_rate['kfc_danpin3']
            elif self.get_pic_type(self.current_pic1) == 'kfc_taocan':
                if self.current_pic1 == self.current_pic5 == self.current_pic9:
                    rate += self.money_rate['kfc_taocan3']
        if self.get_pic_type(self.current_pic4) == self.get_pic_type(self.current_pic5) == self.get_pic_type(
                self.current_pic6):
            if self.get_pic_type(self.current_pic4) == 'wangzheng':
                if self.current_pic4 == self.current_pic5 == self.current_pic6:
                    rate += self.money_rate['wangzheng_same3']
                else:
                    rate += self.money_rate['wangzheng_renyi3']
            elif self.get_pic_type(self.current_pic4) == 'kfc_danpin':
                if self.current_pic4 == self.current_pic5 == self.current_pic6:
                    rate += self.money_rate['kfc_danpin3']
            elif self.get_pic_type(self.current_pic4) == 'kfc_taocan':
                if self.current_pic4 == self.current_pic5 == self.current_pic6:
                    rate += self.money_rate['kfc_taocan3']
        if self.get_pic_type(self.current_pic7) == self.get_pic_type(self.current_pic8) == self.get_pic_type(
                self.current_pic9):
            if self.get_pic_type(self.current_pic7) == 'wangzheng':
                if self.current_pic7 == self.current_pic8 == self.current_pic9:
                    rate += self.money_rate['wangzheng_same3']
                else:
                    rate += self.money_rate['wangzheng_renyi3']
            elif self.get_pic_type(self.current_pic7) == 'kfc_danpin':
                if self.current_pic7 == self.current_pic8 == self.current_pic9:
                    rate += self.money_rate['kfc_danpin3']
            elif self.get_pic_type(self.current_pic7) == 'kfc_taocan':
                if self.current_pic7 == self.current_pic8 == self.current_pic9:
                    rate += self.money_rate['kfc_taocan3']
        if self.get_pic_type(self.current_pic2) == self.get_pic_type(self.current_pic5) == self.get_pic_type(
                self.current_pic8):
            if self.get_pic_type(self.current_pic2) == 'wangzheng':
                if self.current_pic2 == self.current_pic5 == self.current_pic8:
                    rate += self.money_rate['wangzheng_same3']
                else:
                    rate += self.money_rate['wangzheng_renyi3']
            elif self.get_pic_type(self.current_pic2) == 'kfc_danpin':
                if self.current_pic2 == self.current_pic5 == self.current_pic8:
                    rate += self.money_rate['kfc_danpin3']
            elif self.get_pic_type(self.current_pic2) == 'kfc_taocan':
                if self.current_pic2 == self.current_pic5 == self.current_pic8:
                    rate += self.money_rate['kfc_taocan3']
        if self.get_pic_type(self.current_pic3) == self.get_pic_type(self.current_pic6) == self.get_pic_type(
                self.current_pic9):
            if self.get_pic_type(self.current_pic3) == 'wangzheng':
                if self.current_pic3 == self.current_pic6 == self.current_pic9:
                    rate += self.money_rate['wangzheng_same3']
                else:
                    rate += self.money_rate['wangzheng_renyi3']
            elif self.get_pic_type(self.current_pic3) == 'kfc_danpin':
                if self.current_pic3 == self.current_pic6 == self.current_pic9:
                    rate += self.money_rate['kfc_danpin3']
            elif self.get_pic_type(self.current_pic3) == 'kfc_taocan':
                if self.current_pic3 == self.current_pic6 == self.current_pic9:
                    rate += self.money_rate['kfc_taocan3']
        if self.get_pic_type(self.current_pic3) == self.get_pic_type(self.current_pic5) == self.get_pic_type(
                self.current_pic7):
            if self.get_pic_type(self.current_pic3) == 'wangzheng':
                if self.current_pic3 == self.current_pic5 == self.current_pic7:
                    rate += self.money_rate['wangzheng_same3']
                else:
                    rate += self.money_rate['wangzheng_renyi3']
            elif self.get_pic_type(self.current_pic3) == 'kfc_danpin':
                if self.current_pic3 == self.current_pic5 == self.current_pic7:
                    rate += self.money_rate['kfc_danpin3']
            elif self.get_pic_type(self.current_pic3) == 'kfc_taocan':
                if self.current_pic3 == self.current_pic5 == self.current_pic7:
                    rate += self.money_rate['kfc_taocan3']
        if self.get_pic_type(self.current_pic1) == self.get_pic_type(self.current_pic2) == self.get_pic_type(
                self.current_pic3) == self.get_pic_type(self.current_pic4) == self.get_pic_type(
            self.current_pic5) == self.get_pic_type(self.current_pic6) == self.get_pic_type(
            self.current_pic7) == self.get_pic_type(self.current_pic8) == self.get_pic_type(
            self.current_pic9):
            if self.get_pic_type(self.current_pic1) == 'wangzheng':
                if self.current_pic1 == self.current_pic2 == self.current_pic3 == self.current_pic4 == \
                        self.current_pic5 == self.current_pic6 == self.current_pic7 == self.current_pic8 == self.current_pic9:
                    rate = self.money_rate['wangzheng_same9']
                else:
                    rate = self.money_rate['wangzheng_renyi9']
            else:
                if self.current_pic1 == self.current_pic2 == self.current_pic3 == self.current_pic4 == \
                        self.current_pic5 == self.current_pic6 == self.current_pic7 == self.current_pic8 == self.current_pic9:
                    rate = self.money_rate['kfc_same9']
        if rate == 0:
            result = xiaofei + "很可惜未中奖."
        else:
            get_money = rate * use_money
            self.current_money += get_money
            self.score.setText(str(self.current_money))
            result = xiaofei + "中得%s代币." % get_money
        self.set_money_in_config(self.current_money)
        return result

    def start_play(self):
        """用于点击开始完整的逻辑判断"""
        self.start_play_button.setDisabled(True)
        result = self.deduction_money()
        if result:
            self.whole_move(20)
            play_result = self.calculate_reward(self.use_money)
            self.play_recorder.append(play_result)
        self.start_play_button.setEnabled(True)

    def charge(self):
        """充值接口，暂时直接恢复到100，只限3次"""
        if self.charge_time<3:
            if self.current_money < 50:
                self.current_money = 100
                self.score.setText(str(self.current_money))
                self.set_money_in_config(self.current_money)
                self.charge_time += 1
                self.set_charge_time_in_config(self.charge_time)
                QtWidgets.QMessageBox.information(self, u'通知', u'您的余额恢复至100,剩余可充值次数:%s！' %(3-self.charge_time))
                return True
            else:
                QtWidgets.QMessageBox.information(self, u'通知', u'您的余额高于50，剩余免费可充值次数:%s，不建议您充值！'%(3-self.charge_time))
                return False
        QtWidgets.QMessageBox.warning(self, u'通知', u'您的充值次数已用尽，请联系黄挺增加次数！')
        return False

    def open_webview(self):
        # browser=QWebEngineView()
        # print(1111111111111)
        # browser.load(QUrl("https://www.aosom.com"))
        # self.setCentralWidget(browser)
        # web_layout = QtWidgets.QLayout
        QtWidgets.QMessageBox.warning(self, u'告知', u'王政正在与KFC商业洽谈中，更多好礼马上到来！')
        # self.huangou_window.show()

class huangou_window(QWidget, Ui_WEBview):
    def __init__(self, parent=None):
        super(huangou_window, self).__init__(parent)
        self.setupUi(self)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    test = qianduan()
    test.show()
    sys.exit(app.exec_())
