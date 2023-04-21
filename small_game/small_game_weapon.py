#-*-coding:utf-8-*-

from __future__ import division
import os
import sys
import random
import string
import pymysql
import datetime
import math
from PyQt4 import QtCore,QtGui
from small_game_weapon_ui import Ui_Form_wuqidian

class wuqidian(QtGui.QWidget,Ui_Form_wuqidian):
    def __init__(self, parent=None):
        super(wuqidian, self).__init__(parent)
        self.setupUi(self)
        self.playerid=''
        self.pgold=0
        self.plevel=1
        self.current_weapon_price=0
        self.current_weapon_level=1
        self.connect(self.tuichu, QtCore.SIGNAL("clicked()"), self, QtCore.SLOT("close()"))
        self.connect(self.leixing, QtCore.SIGNAL("currentIndexChanged(int)"), lambda :self.change_mingcheng())
        self.connect(self.mingcheng, QtCore.SIGNAL("currentIndexChanged(int)"), lambda: self.display_price())
        self.connect(self.mingcheng, QtCore.SIGNAL("currentIndexChanged(int)"), lambda: self.display_shuxing())
        self.connect(self.pinzhi, QtCore.SIGNAL("currentIndexChanged(int)"), lambda: self.display_shuxing())
        self.connect(self.goumai,QtCore.SIGNAL("clicked()"), lambda: self.buy_weapon())

    def change_mingcheng(self):
        '''根据选择武器或防具切换名称的列表'''
        db=pymysql.connect('localhost','root','','small_game',charset='utf8')
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT name from weapon_info where leixing=1 and pinzhi=1")
        wname=cursor.fetchall()
        length=len(wname)
        list_wuqi=[]
        for i in range(length):
            list_wuqi.append(wname[i]['name'])
        # list_wuqi=wname[0]['name']
        cursor.execute("SELECT name from weapon_info where leixing=2 and pinzhi=1")
        fname=cursor.fetchall()
        length=len(wname)
        list_fangju=[]
        for i in range(length):
            list_fangju.append(fname[i]['name'])
        current_select=self.leixing.currentText()
        if current_select==u"武器":
            self.mingcheng.clear()
            self.mingcheng.addItems(list_wuqi)
        elif current_select==u"防具":
            self.mingcheng.clear()
            self.mingcheng.addItems(list_fangju)
        db.close()

    def display_gold(self,playerid=''):
        self.playerid=playerid
        if self.playerid !='':
            db=pymysql.connect('localhost','root','','small_game',charset='utf8')
            cursor = db.cursor(pymysql.cursors.DictCursor)
            cursor.execute("SELECT gold,level from player_info where id='%s'"%self.playerid)
            pinfo=cursor.fetchall()
            self.pgold=pinfo[0]['gold']
            self.plevel=pinfo[0]['level']
            self.gold.setText(str(self.pgold))
            db.close()
        else:
            return False

    def display_price(self):
        item=self.mingcheng.currentText()
        print("Current item is %s"%item)
        if item=='':
            return False
        db=pymysql.connect('localhost','root','','small_game',charset='utf8')
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT price from weapon_info where name='%s'"%item)
        wprice=cursor.fetchall()
        w_price=wprice[0]['price']
        self.current_weapon_price=w_price
        self.jiage.setText(str(w_price))
        db.close()

    def display_shuxing(self):
        wlevel=self.pinzhi.currentIndex()
        item=self.mingcheng.currentText()
        if item=='':
            return False
        db=pymysql.connect('localhost','root','','small_game',charset='utf8')
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT wugong,wufang,fagong,fafang,wugong_chengzhang,wufang_chengzhang,fagong_chengzhang,fafang_chengzhang from weapon_shuxing where name='%s'"%item)
        wshuxing=cursor.fetchall()
        db.close()
        wugong=wshuxing[0]['wugong']
        wufang=wshuxing[0]['wufang']
        fagong=wshuxing[0]['fagong']
        fafang=wshuxing[0]['fafang']
        wugong_chengzhang=wshuxing[0]['wugong_chengzhang']
        wufang_chengzhang=wshuxing[0]['wufang_chengzhang']
        fagong_chengzhang=wshuxing[0]['fagong_chengzhang']
        fafang_chengzhang=wshuxing[0]['fafang_chengzhang']
        display_wugong=wugong+wlevel*wugong_chengzhang
        display_wufang=wufang+wlevel*wufang_chengzhang
        display_fagong=fagong+wlevel*fagong_chengzhang
        display_fafang=fafang+wlevel*fafang_chengzhang
        self.wugong.setText(str(display_wugong))
        self.wufang.setText(str(display_wufang))
        self.fagong.setText(str(display_fagong))
        self.fafang.setText(str(display_fafang))

    def buy_weapon(self):
        if self.pgold-self.current_weapon_price<0:
            QtGui.QMessageBox.information(self,u'消息',u'钱不够，无法购买！')
            return False
        else:
            self.pgold=self.pgold-self.current_weapon_price
            self.gold.setText(str(self.pgold))
            db=pymysql.connect('localhost','root','','small_game',charset='utf8')
            cursor = db.cursor(pymysql.cursors.DictCursor)
            cursor.execute("UPDATE player_info set gold=%s where id='%s'" %(self.pgold,self.playerid))
            self.current_weapon_level=self.pinzhi.currentIndex()
            current_name=self.mingcheng.currentText()
            cursor.execute("INSERT INTO bag_weapon(player_id,name,naijiu,level) VALUES('%s','%s',20,%s)" %(self.playerid,current_name,self.current_weapon_level))
            db.commit()
            db.close()


if __name__ == '__main__':
    app=QtGui.QApplication(sys.argv)
    test=wuqidian()
    test.show()
    sys.exit(app.exec_())
    # test=xuanze_juese()
    # test.get_all_account()