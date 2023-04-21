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
from small_game_xinjian_ui import Ui_Form_xinjian

class xinjian(QtGui.QWidget,Ui_Form_xinjian):
    # playerid=QtCore.SIGNAL(str)
    def __init__(self, parent=None):
        super(xinjian, self).__init__(parent)
        self.setupUi(self)
        self.id=''
        # self.connect(self.shuru, QtCore.SIGNAL('clicked()'), lambda: self.input_name())
        self.connect(self.zhudongfenpei, QtCore.SIGNAL("clicked()"), lambda: self.zhudong_fenpei())
        self.connect(self.suijifenpei, QtCore.SIGNAL("clicked()"), lambda: self.suiji_fenpei())
        self.connect(self.zhudongfenpei, QtCore.SIGNAL("clicked()"), self, QtCore.SLOT("close()"))
        self.connect(self.suijifenpei, QtCore.SIGNAL("clicked()"), self, QtCore.SLOT("close()"))
        self.name.clear()
        self.connect(self.qvxiao, QtCore.SIGNAL("clicked()"), self, QtCore.SLOT("close()"))

    # def input_name(self):
    #     name,ok=QtGui.QInputDialog.getText(self, u'角色名',u'请输入角色名：',QtGui.QLineEdit.Normal,self.name.text())
    #     if ok and len(name)!=0:
    #         self.name.setText(name)

    def create_id(self):
        nowtime=datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        letters = string.ascii_letters
        return nowtime+''.join(random.choice(letters) for i in range(3))

    def zhudong_fenpei(self):
        '''保留10点属性点之间生成角色'''
        self.id=self.create_id()
        name=self.name.text()
        if name=="":
            QtGui.QMessageBox.warning(self,u'警告',u'未输入角色名字,将用玩家id作为名字！',QtGui.QMessageBox.Ok)
            name=self.id
        # hp=10
        # shuxingdian=10
        db=pymysql.connect('localhost','root','','small_game',charset='utf8')
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute("INSERT INTO player_info(id,name,gold,jingyan,level,xingdongli,shuxingdian) VALUES ('%s','%s',1000,0,1,200,10)"%(self.id,name))
        cursor.execute("INSERT INTO player_shuxing(id,current_hp,hp,liliang,fali,minjie,xingyun,jiqiao,yili) VALUES ('%s',10,10,0,0,0,0,0,0)" %self.id)
        db.commit()
        # return hp,shuxingdian
        db.close()
        self.emit(QtCore.SIGNAL('playerid'),self.id)
        self.emit(QtCore.SIGNAL('close()'))

    def suiji_fenpei(self):
        '''随机分配13点属性点'''
        self.id=self.create_id()
        name=self.name.text()
        if name=="":
            QtGui.QMessageBox.warning(self,u'警告',u'未输入角色名字,将用玩家id作为名字！',QtGui.QMessageBox.Ok)
            name=self.id
        hp=10
        shuxingdian=13
        liliang=0
        fali=0
        minjie=0
        jiqiao=0
        xingyun=0
        yili=0
        list=[]
        for i in range(7):
            maxnum=shuxingdian//2
            if maxnum<shuxingdian:
                maxnum+=1
            if i==6:
                list.append(shuxingdian)
                break
            a=random.randint(0,maxnum)
            list.append(a)
            shuxingdian=shuxingdian-a
        random.shuffle(list)  #将数列重新排序
        hp+=list[0]
        current_hp=hp
        liliang+=list[1]
        fali+=list[2]
        minjie+=list[3]
        jiqiao+=list[4]
        xingyun+=list[5]
        yili+=list[6]
        db=pymysql.connect('localhost','root','','small_game',charset='utf8')
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute("INSERT INTO player_info(id,name,gold,jingyan,level,xingdongli,shuxingdian) VALUES ('%s','%s',1000,0,1,200,0)"%(self.id,name))
        cursor.execute("INSERT INTO player_shuxing(id,current_hp,hp,liliang,fali,minjie,xingyun,jiqiao,yili) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s')" %(self.id,current_hp,hp,liliang,fali,minjie,xingyun,jiqiao,yili))
        db.commit()
        # return hp,shuxingdian
        db.close()
        # self.status_signal.emit('close')
        self.emit(QtCore.SIGNAL('playerid'), self.id)#
        self.emit(QtCore.SIGNAL('close()'))

        # return hp,liliang,fali,minjie,jiqiao,xingyun,yili


   #  def select_zhiye(self):
   #      list=[u'战士',u'法师']
   #      occupation,ok=QtGui.QInputDialog.getItem(self,u'职业',u'请选择职业：',list,0,False)
   # #      getItem()函数原型如下：
   # # (QString, bool ok) getItem (QWidget, QString, QString, QStringList, int current = 0, bool editable = True, Qt.WindowFlags flags = 0)
   # #  此函数的第一个参数为标准输入对话框的父窗窗口，
   # #  第二个参数为标准输入对话框的标题名，
   # #  第三个参数为标准输入对话框的标签提示，
   # #  第四个参数指定标准输入对话框中QComboBox控件显示的可选条目，为一个QStringList对象，
   # #  第五个参数current为标准条目选择对话框弹出时QComboBox控件中默认显示的条目序号，
   # #  第六个参数editable指定QComboBox控件中显示的文字是否可编辑，
   # #  最后一个参数指明标准输入对话框的窗体标识。
   #      if ok:
   #          self.zhiye.setText(occupation)

    def transfer_shuxing(self,liliang,fali,minjie,xingyun,jiqiao,yili):
        '''把人物属性转化成面板属性'''
        wugong=liliang
        wufang=liliang
        fagong=fali
        fafang=fali
        sudu=minjie
        baoji=liliang*0.1+fali*0.1+jiqiao*0.4
        renxing=xingyun*0.4+yili*0.6
        shanbi=minjie*0.4+xingyun*0.6
        mingzhong=jiqiao*0.7+yili*0.4
        return sudu,wugong,wufang,fagong,fafang,baoji,renxing,shanbi,mingzhong

    def calculate_shuxing(self):
        if self.id !='':
            db=pymysql.connect('localhost','root','','small_game',charset='utf8')
            cursor = db.cursor(pymysql.cursors.DictCursor)  #让fetchall函数返回字典，而不是元组
            cursor.execute("Select * from player_info where id = '%s'"%self.id)
            info=cursor.fetchall()  #[{u'name': u'20201121150143EIL', u'gold': 1000, u'level': 0, u'jingyan': 0.0, u'xingdongli': 200, u'id': u'20201121150143EIL', u'shuxingdian': 0}]
            name=info[0]['name']
            gold=info[0]['gold']
            jingyan=info[0]['jingyan']
            shuxingdian=info[0]['shuxingdian']
            level=info[0]['level']
            xingdongli=info[0]['xingdongli']
            cursor.execute("Select * from player_shuxing where id = '%s'"%self.id)
            shuxing=cursor.fetchall()
            hp=shuxing[0]['hp']
            current_hp=hp
            liliang=shuxing[0]['liliang']
            fali=shuxing[0]['fali']
            minjie=shuxing[0]['minjie']
            xingyun=shuxing[0]['xingyun']
            jiqiao=shuxing[0]['jiqiao']
            yili=shuxing[0]['yili']
            sudu,wugong,wufang,fagong,fafang,baoji,renxing,shanbi,mingzhong=self.transfer_shuxing(liliang,fali,minjie,xingyun,jiqiao,yili)
            return name,level,gold,jingyan,xingdongli,current_hp,hp,sudu,wugong,wufang,fagong,fafang,baoji,renxing,shanbi,mingzhong
        else:
            QtGui.QMessageBox.information(self,u'警告',u'未选中任何角色!')
            return False

if __name__ == '__main__':
    app=QtGui.QApplication(sys.argv)
    test=xinjian()
    test.show()
    sys.exit(app.exec_())