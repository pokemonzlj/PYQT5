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
from small_game_shuxing_ui import Ui_Form_shuxingjiadian
from small_game_xinjian import xinjian

class shuxing_jiadian(QtGui.QWidget,Ui_Form_shuxingjiadian):
    def __init__(self, parent=None):
        super(shuxing_jiadian, self).__init__(parent)
        self.playerid=''
        self.shuxingdiana=0
        self.hpa=0
        self.lilianga=0
        self.falia=0
        self.minjiea=0
        self.yilia=0
        self.xingyuna=0
        self.jiqiaoa=0
        self.xinjian1=xinjian()
        self.setupUi(self)
        self.connect(self.tuichu, QtCore.SIGNAL("clicked()"), self, QtCore.SLOT("close()"))
        self.connect(self.hp, QtCore.SIGNAL("valueChanged(int)") ,lambda : self.hp_connect_total_shuxingdian())
        self.connect(self.liliang, QtCore.SIGNAL("valueChanged(int)") ,lambda : self.liliang_connect_total_shuxingdian())
        self.connect(self.fali, QtCore.SIGNAL("valueChanged(int)") ,lambda : self.fali_connect_total_shuxingdian())
        self.connect(self.minjie, QtCore.SIGNAL("valueChanged(int)") ,lambda : self.minjie_connect_total_shuxingdian())
        self.connect(self.jiqiao, QtCore.SIGNAL("valueChanged(int)") ,lambda : self.jiqiao_connect_total_shuxingdian())
        self.connect(self.yili, QtCore.SIGNAL("valueChanged(int)") ,lambda : self.yili_connect_total_shuxingdian())
        self.connect(self.xingyun, QtCore.SIGNAL("valueChanged(int)") ,lambda : self.xingyun_connect_total_shuxingdian())
        self.connect(self.queren, QtCore.SIGNAL("clicked()"), self, QtCore.SLOT("close()"))
        self.connect(self.queren,  QtCore.SIGNAL("clicked()"), lambda :self.baocun_jiadian())
        # self.hp.valueChanged.connect(self.hp_connect_total_shuxingdian)

    def get_player_shuxing(self,playerid=''):
        self.playerid=playerid
        db=pymysql.connect('localhost','root','','small_game',charset='utf8')
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT name,shuxingdian from player_info where id='%s'"%self.playerid)
        pinfo=cursor.fetchall()
        self.namea=pinfo[0]['name']
        self.shuxingdiana=pinfo[0]['shuxingdian']
        cursor.execute("SELECT hp,liliang,fali,minjie,xingyun,jiqiao,yili from player_shuxing where id='%s'"%self.playerid)
        pshuxing=cursor.fetchall()
        db.close()
        self.hpa=pshuxing[0]["hp"]
        self.lilianga=pshuxing[0]["liliang"]
        self.falia=pshuxing[0]["fali"]
        self.minjiea=pshuxing[0]["minjie"]
        self.xingyuna=pshuxing[0]["xingyun"]
        self.jiqiaoa=pshuxing[0]["jiqiao"]
        self.yilia=pshuxing[0]["yili"]
        return self.namea,self.shuxingdiana,self.hpa,self.lilianga,self.falia,self.minjiea,self.xingyuna,self.jiqiaoa,self.yilia

    def set_shuxing_window(self,playid=''):
        name,shuxingdian,hp,liliang,fali,minjie,xingyun,jiqiao,yili=self.get_player_shuxing(playid)
        self.name.setText(name)
        self.shuxingdian.setText(str(shuxingdian))
        self.hp.setValue(hp)
        self.liliang.setValue(liliang)
        self.fali.setValue(fali)
        self.minjie.setValue(minjie)
        self.xingyun.setValue(xingyun)
        self.jiqiao.setValue(jiqiao)
        self.yili.setValue(yili)
        self.set_min_value()

    def set_min_value(self):
        self.hp.setMinimum(self.hpa)
        self.liliang.setMinimum(self.lilianga)
        self.fali.setMinimum(self.falia)
        self.minjie.setMinimum(self.minjiea)
        self.xingyun.setMinimum(self.xingyuna)
        self.jiqiao.setMinimum(self.jiqiaoa)
        self.yili.setMinimum(self.yilia)

    def hp_connect_total_shuxingdian(self):
        '''关联hp项与总属性点的同步关系'''
        value=self.hp.value()
        if value>self.hpa:
            if self.shuxingdiana>0:
                self.shuxingdiana-=1
            else:
                QtGui.QMessageBox.information(self,u'消息',u'已经没有可分配技能点！')
                self.hp.setValue(self.hpa)
                return False
        elif value<self.hpa:
                self.shuxingdiana+=1
        self.shuxingdian.setText(str(self.shuxingdiana))
        self.hpa=value

    def liliang_connect_total_shuxingdian(self):
        '''关联力量项与总属性点的同步关系'''
        value=self.liliang.value()
        if value>self.lilianga:
            if self.shuxingdiana>0:
                self.shuxingdiana-=1
            else:
                QtGui.QMessageBox.information(self,u'消息',u'已经没有可分配技能点！')
                self.liliang.setValue(self.lilianga)
                return False
        elif value<self.lilianga:
                self.shuxingdiana+=1
        self.shuxingdian.setText(str(self.shuxingdiana))
        self.lilianga=value

    def fali_connect_total_shuxingdian(self):
        '''关联法力项与总属性点的同步关系'''
        value=self.fali.value()
        if value>self.falia:
            if self.shuxingdiana>0:
                self.shuxingdiana-=1
            else:
                QtGui.QMessageBox.information(self,u'消息',u'已经没有可分配技能点！')
                self.fali.setValue(self.falia)
                return False
        elif value<self.falia:
                self.shuxingdiana+=1
        self.shuxingdian.setText(str(self.shuxingdiana))
        self.falia=value

    def minjie_connect_total_shuxingdian(self):
        '''关联敏捷项与总属性点的同步关系'''
        value=self.minjie.value()
        if value>self.minjiea:
            if self.shuxingdiana>0:
                self.shuxingdiana-=1
            else:
                QtGui.QMessageBox.information(self,u'消息',u'已经没有可分配技能点！')
                self.minjie.setValue(self.minjiea)
                return False
        elif value<self.minjiea:
                self.shuxingdiana+=1
        self.shuxingdian.setText(str(self.shuxingdiana))
        self.minjiea=value

    def xingyun_connect_total_shuxingdian(self):
        '''关联幸运项与总属性点的同步关系'''
        value=self.xingyun.value()
        if value>self.xingyuna:
            if self.shuxingdiana>0:
                self.shuxingdiana-=1
            else:
                QtGui.QMessageBox.information(self,u'消息',u'已经没有可分配技能点！')
                self.xingyun.setValue(self.xingyuna)
                return False
        elif value<self.xingyuna:
                self.shuxingdiana+=1
        self.shuxingdian.setText(str(self.shuxingdiana))
        self.xingyuna=value

    def jiqiao_connect_total_shuxingdian(self):
        '''关联技巧项与总属性点的同步关系'''
        value=self.jiqiao.value()
        if value>self.jiqiaoa:
            if self.shuxingdiana>0:
                self.shuxingdiana-=1
            else:
                QtGui.QMessageBox.information(self,u'消息',u'已经没有可分配技能点！')
                self.jiqiao.setValue(self.jiqiaoa)
                return False
        elif value<self.jiqiaoa:
                self.shuxingdiana+=1
        self.shuxingdian.setText(str(self.shuxingdiana))
        self.jiqiaoa=value

    def yili_connect_total_shuxingdian(self):
        '''关联毅力项与总属性点的同步关系'''
        value=self.yili.value()
        if value>self.yilia:
            if self.shuxingdiana>0:
                self.shuxingdiana-=1
            else:
                QtGui.QMessageBox.information(self,u'消息',u'已经没有可分配技能点！')
                self.yili.setValue(self.yilia)
                return False
        elif value<self.yilia:
                self.shuxingdiana+=1
        self.shuxingdian.setText(str(self.shuxingdiana))
        self.yilia=value

    def baocun_jiadian(self):
        db=pymysql.connect('localhost','root','','small_game',charset='utf8')
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute("UPDATE player_info SET shuxingdian=%s where id='%s'"%(self.shuxingdiana,self.playerid))
        cursor.execute("UPDATE player_shuxing SET hp=%s,liliang=%s,fali=%s,minjie=%s,xingyun=%s,yili=%s,jiqiao=%s where id='%s'" %(self.hpa,self.lilianga,self.falia,self.minjiea,self.xingyuna,self.yilia,self.jiqiaoa,self.playerid))
        db.commit()
        db.close()
        self.emit(QtCore.SIGNAL("jiadian_close"))

    def baocun_player(self):
        db=pymysql.connect('localhost','root','','small_game',charset='utf8')
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT gold,jingyan,level,xingdongli from player_info where id='%s'"%self.playerid)
        pinfo=cursor.fetchall()
        gold=pinfo[0]['gold']
        jingyan=pinfo[0]['jingyan']
        level=pinfo[0]['level']
        xingdongli=pinfo[0]['xingdongli']
        cursor.execute("SELECT current_hp from player_shuxing where id='%s'"%self.playerid)
        pshuxing=cursor.fetchall()
        current_hp=pshuxing[0]['current_hp']
        db.close()
        sudu,wugong,wufang,fagong,fafang,baoji,renxing,shanbi,mingzhong=self.xinjian1.transfer_shuxing(self.lilianga,self.falia,self.minjiea,self.xingyuna,self.jiqiaoa,self.yilia)
        return self.namea,level,gold,jingyan,xingdongli,current_hp,self.hpa,sudu,wugong,wufang,fagong,fafang,baoji,renxing,shanbi,mingzhong

if __name__ == '__main__':
    app=QtGui.QApplication(sys.argv)
    test=shuxing_jiadian()
    test.show()
    sys.exit(app.exec_())