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
from small_game_xuanzejuese_ui import Ui_Form_xuanzejuese
from small_game_xinjian import xinjian

class xuanze_juese(QtGui.QWidget,Ui_Form_xuanzejuese):
    def __init__(self, parent=None):
        super(xuanze_juese, self).__init__(parent)
        self.setupUi(self)
        self.xinjian1=xinjian()
        self.player_id=''
        self.current_place=0
        self.all_players=self.get_all_account()
        self.shangyige.setDisabled(True)
        self.connect(self.xiayige, QtCore.SIGNAL("clicked()"), lambda:self.display_juese_xiayige())
        self.connect(self.shangyige,QtCore.SIGNAL("clicked()"), lambda:self.display_juese_shangyige())
        self.connect(self.xuanze, QtCore.SIGNAL("clicked()"), self, QtCore.SLOT("close()"))   #点击选择后关闭选择界面
        self.connect(self.shanchu, QtCore.SIGNAL("clicked()"),lambda :self.delete_juese())
        #self.connect(self.xuanze, QtCore.SIGNAL("clicked()"), lambda:QtCore.QCoreApplication.instance().exit(0))

    def get_all_account(self):
        db=pymysql.connect('localhost','root','','small_game',charset='utf8')
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute("select * from player_info join player_shuxing where player_info.id=player_shuxing.id")
        all_player_info=cursor.fetchall()
        db.close()
        # list_lens=len(all_player_info)
        return all_player_info

    def get_player_info(self,pid=''):
        list_lens=len(self.all_players)
        for i in range(list_lens):
            if pid in self.all_players[i].values():
                name=self.all_players[i]['name']
                level=self.all_players[i]['level']
                gold=self.all_players[i]['gold']
                current_hp=self.all_players[i]['current_hp']
                hp=self.all_players[i]['hp']
                liliang=self.all_players[i]['liliang']
                fali=self.all_players[i]['fali']
                minjie=self.all_players[i]['minjie']
                jiqiao=self.all_players[i]['jiqiao']
                xingyun=self.all_players[i]['xingyun']
                yili=self.all_players[i]['yili']
                return name,level,gold,current_hp,hp,liliang,fali,minjie,jiqiao,xingyun,yili
        print("Can not find player with id: %s"%pid)

    def display_player(self,pid=''):
        name,level,gold,current_hp,hp,liliang,fali,minjie,jiqiao,xingyun,yili=self.get_player_info(pid)
        self.name.setText(name)
        self.level.setText(str(level))
        self.gold.setText(str(gold))
        self.hp.setText(str(current_hp)+'/'+str(hp))
        self.level.setText(str(level))
        self.liliang.setText(str(liliang))
        self.fali.setText(str(fali))
        self.minjie.setText(str(minjie))
        self.jiqiao.setText(str(jiqiao))
        self.xingyun.setText(str(xingyun))
        self.yili.setText(str(yili))

    def delete_player(self,pid=''):
        db=pymysql.connect('localhost','root','','small_game',charset='utf8')
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute("DELETE from player_info where id='%s'"%pid)
        cursor.execute("DELETE from player_shuxing where id='%s'"%pid)
        db.commit()
        db.close()
        print("Delete player id:%s data in SQL."%pid)
        list_lens=len(self.all_players)
        for i in range(list_lens):
            if pid in self.all_players[i].values():
                del self.all_players[i]
                print("Delete player id:%s data in current players list."%pid)
                return True

    def delete_juese(self):
        text=QtGui.QMessageBox.warning(self,u'警告',u'确定要删除角色吗？',QtGui.QMessageBox.Ok|QtGui.QMessageBox.No)
        if text==QtGui.QMessageBox.Ok:
            list_lens=len(self.all_players)
            pid=self.all_players[self.current_place]['id']
            self.delete_player(pid)
            if self.current_place==list_lens-1:
                self.display_juese_shangyige()
            else:
                self.current_place-=1
                self.display_juese_xiayige()
        else:
            return

    def display_juese_xiayige(self):
        list_lens=len(self.all_players)
        if self.current_place==list_lens-1: #如果到最后一个了
            self.xiayige.setDisabled(True)
            return False
        self.current_place+=1
        pid=self.all_players[self.current_place]['id']
        self.display_player(pid)
        if self.current_place>0:  #适配显示第一个的时候
            self.shangyige.setEnabled(True)
        if self.current_place==list_lens-1: #如果到最后一个了
            self.xiayige.setDisabled(True)
            return False

    def display_juese_shangyige(self):
        if self.current_place<=0:
            self.shangyige.setDisabled(True)
            return False
        self.current_place-=1
        pid=self.all_players[self.current_place]['id']
        self.display_player(pid)
        self.xiayige.setEnabled(True)
        if self.current_place<=0:
            self.shangyige.setDisabled(True)
            return False

    def xuanze_player(self):
        pid=self.all_players[self.current_place]['id']
        self.player_id=pid
        name,level,gold,current_hp,hp,liliang,fali,minjie,jiqiao,xingyun,yili=self.get_player_info(pid)
        sudu,wugong,wufang,fagong,fafang,baoji,renxing,shanbi,mingzhong=self.xinjian1.transfer_shuxing(liliang,fali,minjie,xingyun,jiqiao,yili)
        jingyan=self.all_players[self.current_place]['jingyan']
        xingdongli=self.all_players[self.current_place]['xingdongli']
        self.emit(QtCore.SIGNAL('loadplayerid'), self.player_id)
        # self.emit(QtCore.SIGNAL('close()'))
        return name,level,gold,jingyan,xingdongli,current_hp,hp,sudu,wugong,wufang,fagong,fafang,baoji,renxing,shanbi,mingzhong

if __name__ == '__main__':
    app=QtGui.QApplication(sys.argv)
    test=xuanze_juese()
    test.show()
    sys.exit(app.exec_())