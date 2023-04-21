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
from small_game_zhuangbeilan_ui import Ui_Form_zhuangbeilan

class zhuangbeilan(QtGui.QWidget,Ui_Form_zhuangbeilan):
    def __init__(self, parent=None):
        super(zhuangbeilan, self).__init__(parent)
        self.setupUi(self)
        self.playerid=''
        self.weapon_id=0  #记录当前选中装备的id号
        self.weapon_level=0 #记录当前选中装备的等级限制
        self.list_wuqi=[]
        self.list_fangju=[]
        self.current_index=0
        self.connect(self.tuichu, QtCore.SIGNAL("clicked()"), self, QtCore.SLOT("close()"))
        self.connect(self.leixing, QtCore.SIGNAL("currentIndexChanged(int)"), lambda: self.show_list())
        self.connect(self.zhuangbei_list, QtCore.SIGNAL("currentIndexChanged(int)"), lambda: self.show_naijiu())
        self.connect(self.zhuangbei_list, QtCore.SIGNAL("currentIndexChanged(int)"), lambda: self.show_texiao())
        # self.connect(self.leixing, QtCore.SIGNAL("currentIndexChanged(int)"), lambda: self.show_naijiu())
        self.connect(self.maichu, QtCore.SIGNAL("clicked()"), lambda: self.jianmai_zhuangbei())
        self.connect(self.zhuangbei, QtCore.SIGNAL("clicked()"), lambda: self.equip_zhuangbei())
        self.connect(self.zhuangbei_list, QtCore.SIGNAL("currentIndexChanged(int)"), lambda: self.set_zhuangbei_button())

    def get_player_items(self, player_id=''):
        self.playerid=player_id
        self.list_wuqi=[]
        self.list_fangju=[]
        db=pymysql.connect('localhost','root','','small_game',charset='utf8')
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT id,name,equiped,level,naijiu,effect from bag_weapon  where player_id='%s' and name in (select name from weapon_info where weapon_info.leixing=1)" %self.playerid)
        wname=cursor.fetchall()
        length=len(wname)
        for i in range(length):
            self.list_wuqi.append(wname[i])
        cursor.execute("SELECT id,name,equiped,level,naijiu,effect from bag_weapon  where player_id='%s' and name in (select name from weapon_info where weapon_info.leixing=2)" %self.playerid)
        fname=cursor.fetchall()
        db.close()
        length=len(fname)
        for i in range(length):
            self.list_fangju.append(fname[i])
        # print self.list_wuqi,self.list_fangju
        self.weapon_id=self.list_wuqi[0]['id']
        return self.list_wuqi,self.list_fangju

    def show_list(self):
        current_select=self.leixing.currentText()
        length=len(self.list_wuqi)
        wname=[]
        for i in range(length):
            wname.append("level"+str(self.list_wuqi[i]['level'])+":"+self.list_wuqi[i]['name'])
        length=len(self.list_fangju)
        fname=[]
        for i in range(length):
            fname.append("level"+str(self.list_wuqi[i]['level'])+":"+self.list_fangju[i]['name'])
        if current_select==u"武器":
            self.zhuangbei_list.clear()
            self.zhuangbei_list.addItems(wname)
        elif current_select==u"防具":
            self.zhuangbei_list.clear()
            self.zhuangbei_list.addItems(fname)

    def show_naijiu(self):
        current_select=self.leixing.currentText()
        if self.zhuangbei_list.currentIndex() !='':
            self.current_index=self.zhuangbei_list.currentIndex()
            current_naijiu=0
            if current_select==u"武器":
                self.weapon_id=self.list_wuqi[self.current_index]['id']
                self.weapon_level=self.list_wuqi[self.current_index]['level']
                current_naijiu=self.list_wuqi[self.current_index]['naijiu']
            elif current_select==u"防具":
                self.weapon_id=self.list_fangju[self.current_index]['id']
                self.weapon_level=self.list_fangju[self.current_index]['level']
                current_naijiu=self.list_fangju[self.current_index]['naijiu']
            self.naijiu.setText(str(current_naijiu))
        else:
            print("Get zhuangbei list index failed!")

    def show_texiao(self):
        current_select=self.leixing.currentText()
        if current_select==u"武器":
            current_effect=self.list_wuqi[self.current_index]['effect']
        elif current_select==u"防具":
            current_effect=self.list_fangju[self.current_index]['effect']
        if current_effect=='' or current_effect==None:
            self.fumoxiaoguo.setText(u"无附魔")
        else:
            self.fumoxiaoguo.setText(current_effect)

    def set_zhuangbei_button(self):
        current_select=self.leixing.currentText()
        if current_select==u"武器":
            if self.list_wuqi[self.current_index]['equiped']==1:
                self.zhuangbei.setText(u"已装备")
                self.zhuangbei.setDisabled(True)
            else:
                self.zhuangbei.setText(u"装备")
                self.zhuangbei.setEnabled(True)
        elif current_select==u"防具":
            if self.list_fangju[self.current_index]['equiped']==1:
                self.zhuangbei.setText(u"已装备")
                self.zhuangbei.setDisabled(True)
            else:
                self.zhuangbei.setText(u"装备")
                self.zhuangbei.setEnabled(True)

    def jianmai_zhuangbei(self):
        choose=QtGui.QMessageBox.question(self,u'卖出装备',u'是否要将装备以100金币价格卖出？',QtGui.QMessageBox.Yes,QtGui.QMessageBox.No)
        if choose==QtGui.QMessageBox.Yes:
            db=pymysql.connect('localhost','root','','small_game',charset='utf8')
            cursor = db.cursor(pymysql.cursors.DictCursor)
            cursor.execute("DELETE FROM bag_weapon where id=%s" %self.weapon_id)
            cursor.execute("SELECT gold from player_info where id='%s'" %self.playerid)
            pgold=cursor.fetchall()
            current_gold=pgold[0]['gold']
            current_gold+=100
            cursor.execute("UPDATE player_info set gold=%s where id='%s'" %(current_gold, self.playerid))
            db.commit()
            db.close()
            current_select=self.leixing.currentText()
            if current_select==u"武器":
                del self.list_wuqi[self.current_index]
            elif current_select==u"防具":
                del self.list_fangju[self.current_index]
            # self.get_player_items(self.playerid)
            self.show_list()
            self.show_naijiu()
            self.show_texiao()

    def equip_zhuangbei(self):
        db=pymysql.connect('localhost','root','','small_game',charset='utf8')
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT level from player_info where id='%s'" %self.playerid)
        plv=cursor.fetchall()
        player_level=plv[0]['level']
        if player_level < (10*self.weapon_level+10):
            QtGui.QMessageBox.information(self,u'消息',u'该装备需%s级以上才能使用！' %(10*self.weapon_level))
            db.close()
            return False
        current_select=self.leixing.currentText()
        change_id=0
        if current_select==u"武器":
            length=len(self.list_wuqi)
            for i in range(length):
                if self.list_wuqi[i]['equiped']==1:
                    self.list_wuqi[i]['equiped']=0
                    change_id=self.list_wuqi[i]['id']
                    break
            for i in range(length):
                if self.list_wuqi[i]['id']==self.weapon_id:
                    self.list_wuqi[i]['equiped']=1
                    break
        elif current_select==u"防具":
            length=len(self.list_fangju)
            for i in range(length):
                if self.list_fangju[i]['equiped']==1:
                    self.list_fangju[i]['equiped']=0
                    change_id=self.list_fangju[i]['id']
                    break
            for i in range(length):
                if self.list_fangju[i]['id']==self.weapon_id:
                    self.list_fangju[i]['equiped']=1
                    break
        if change_id!=0:  #=0说明之前并没有装备过装备
            cursor.execute("UPDATE bag_weapon SET equiped=0 where id=%s" %change_id)
        cursor.execute("UPDATE bag_weapon SET equiped=1 where id=%s" %self.weapon_id)
        self.zhuangbei.setText(u"已装备")
        self.zhuangbei.setDisabled(True)
        db.commit()
        db.close()
