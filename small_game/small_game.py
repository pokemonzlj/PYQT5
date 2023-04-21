#-*-coding:utf-8-*-

from __future__ import division
import os
import sys
import linecache
import subprocess
import time
import random
import string
import pymysql
import datetime
import math
from PyQt4 import QtCore,QtGui
from small_game_mainwindow_ui import Ui_Form_main
from small_game_shuxing import shuxing_jiadian
from small_game_xuanzejuese import xuanze_juese
from small_game_xinjian import xinjian
from small_game_weapon import wuqidian
from small_game_zhuangbeilan import zhuangbeilan

reload(sys)
sys.setdefaultencoding('utf8')
#sys.setrecursionlimit(1000000)

class small_game(QtGui.QMainWindow,Ui_Form_main):
    def __init__(self, parent=None):
        super(small_game, self).__init__(parent)
        self.setupUi(self)
        self.xuanze_juese1=xuanze_juese()
        self.xinjian1=xinjian()
        self.shuxing_jiadian1=shuxing_jiadian()
        self.wuqidian1=wuqidian()
        self.zhuangbeilan1=zhuangbeilan()
        self.player_id=''
        self.shanchu.setDisabled(True)  #刚进主界面删除角色置灰
        self.beibao.setDisabled(True)
        self.shuxingjiadian.setDisabled(True)
        self.xuanzezhuangbei.setDisabled(True)
        self.connect(self.duqv, QtCore.SIGNAL("clicked()"), lambda: self.open_xuanzejuese())
        self.connect(self.xuanze_juese1.xuanze, QtCore.SIGNAL("clicked()"), lambda: self.update_mainscreen_by_load())  #在juese类里面调用load_juese，set_text函数会失效
        self.connect(self.shanchu, QtCore.SIGNAL("clicked()"), lambda: self.delete_juese())
        self.connect(self.xinjian, QtCore.SIGNAL("clicked()"), lambda: self.open_xinjian())
        self.connect(self.fuhuoquan, QtCore.SIGNAL("clicked()"), lambda: self.fuhuoquan_huifu())
        self.connect(self.wuqidian, QtCore.SIGNAL("clicked()"), lambda: self.open_wuqidian())
        # self.connect(self.xinjian1, QtCore.SIGNAL("destroyed()"), lambda :self.update_mainscreen())
        # self.connect(self.xinjian1, QtCore.SIGNAL('playerid'), lambda :self.get_id(self.xinjian1.id))
        self.connect(self.xinjian1, QtCore.SIGNAL('playerid'), lambda playerid=self.get_id(): self.get_id(playerid))
        self.connect(self.xinjian1, QtCore.SIGNAL('close()'), lambda:self.update_mainscreen_by_new())
        self.connect(self.xuanze_juese1, QtCore.SIGNAL('loadplayerid'), lambda playerid=self.get_id(): self.get_id(playerid))
        self.connect(self.shuxingjiadian, QtCore.SIGNAL("clicked()"), lambda: self.open_shuxing_jiadian())
        self.connect(self.shuxing_jiadian1, QtCore.SIGNAL('jiadian_close'), lambda: self.update_mainscreen_by_jiadian())
        self.connect(self.xuanzezhuangbei, QtCore.SIGNAL("clicked()"), lambda: self.open_zhuangbeilan())


    # @QtCore.pyqtSlot(str)
    def get_id(self,playerid=''):
        self.player_id=playerid
        print("Set player id to: %s"%playerid)
        return self.player_id

    def open_xuanzejuese(self):
        #self.juese1=juese()    #父类实例化子类 直接用.show()方法闪退， 所以要实例化为父类的全局变量 or 执行exec_() 方法
        self.xuanze_juese1.show()  #show():显示一个非模式对话框。控制权即刻返回给调用函数
        #self.juese1.exec_()  #exec():显示一个模式对话框，并且锁住程序直到用户关闭该对话框为止。函数返回一个DialogCode结果
        self.xuanze_juese1.display_juese_xiayige()

    def open_xinjian(self):
        self.xinjian1.show()

    def open_shuxing_jiadian(self):
        self.shuxing_jiadian1.show()
        self.shuxing_jiadian1.set_shuxing_window(self.player_id)
        # self.emit(QtCore.SIGNAL("nowid"),self.player_id)

    def open_wuqidian(self):
        self.wuqidian1.show()
        self.wuqidian1.display_gold(self.player_id)
        self.wuqidian1.change_mingcheng()

    def open_zhuangbeilan(self):
        self.zhuangbeilan1.show()
        self.zhuangbeilan1.get_player_items(self.player_id)
        self.zhuangbeilan1.show_list()
        self.zhuangbeilan1.show_naijiu()
        self.zhuangbeilan1.show_texiao()
        self.zhuangbeilan1.set_zhuangbei_button()

    def update_mainscreen_by_new(self):
        '''通过新建角色更新主界面'''
        name,level,gold,jingyan,xingdongli,current_hp,hp,sudu,wugong,wufang,fagong,fafang,baoji,renxing,shanbi,mingzhong=self.xinjian1.calculate_shuxing()
        self.update_mainscreen(name,level,gold,jingyan,xingdongli,current_hp,hp,sudu,wugong,wufang,fagong,fafang,baoji,renxing,shanbi,mingzhong)

    def update_mainscreen_by_load(self):
        '''通过加载角色更新主界面'''
        name,level,gold,jingyan,xingdongli,current_hp,hp,sudu,wugong,wufang,fagong,fafang,baoji,renxing,shanbi,mingzhong=self.xuanze_juese1.xuanze_player()
        self.update_mainscreen(name,level,gold,jingyan,xingdongli,current_hp,hp,sudu,wugong,wufang,fagong,fafang,baoji,renxing,shanbi,mingzhong)

    def update_mainscreen_by_jiadian(self):
        '''通过属性加点更新主界面'''
        name,level,gold,jingyan,xingdongli,current_hp,hp,sudu,wugong,wufang,fagong,fafang,baoji,renxing,shanbi,mingzhong=self.shuxing_jiadian1.baocun_player()
        self.update_mainscreen(name,level,gold,jingyan,xingdongli,current_hp,hp,sudu,wugong,wufang,fagong,fafang,baoji,renxing,shanbi,mingzhong)

    def update_mainscreen(self,name,level,gold,jingyan,xingdongli,current_hp,hp,sudu,wugong,wufang,fagong,fafang,baoji,renxing,shanbi,mingzhong):
        '''更新整个界面的参数'''
        print("Update the main windows")
        # name,level,gold,jingyan,xingdongli,hp,sudu,wugong,wufang,fagong,fafang,baoji,renxing,shanbi,mingzhong=self.xinjian1.calculate_shuxing()
        print("Now player id is: %s"%self.player_id)
        self.name.setText(name)
        self.level.setText(str(level))
        self.gold.setText(str(gold))
        now_jingyan=int(100*math.pow(1.1,level))
        self.jingyan.setText(str(jingyan)+'/'+str(now_jingyan))
        # self.gold.setText(gold)
        self.xingdongli.setText(str(xingdongli)+'/200')
        self.current_hp=current_hp
        self.hp.setText(str(self.current_hp)+'/'+str(hp))
        self.sudu.setText(str(sudu))
        self.wugong.setText(str(wugong))
        self.wufang.setText(str(wufang))
        self.fagong.setText(str(fagong))
        self.fafang.setText(str(fafang))
        self.baoji.setText(str(baoji)+'%')
        self.renxing.setText(str(renxing)+'%')
        self.shanbi.setText(str(shanbi)+'%')
        self.mingzhong.setText(str(mingzhong)+'%')
        self.shanchu.setEnabled(True)
        self.beibao.setEnabled(True)
        self.shuxingjiadian.setEnabled(True)
        self.xuanzezhuangbei.setEnabled(True)

        # #self.touxiang.setPixmap(QtGui.QPixmap("%s.ico" %i))
        # self.touxiang.setPixmap(QtGui.QPixmap("touxiang/%s.ico" %i))

    def clear_mainscreen(self):
        '''清空整个界面的数据'''
        self.name.clear()
        self.level.clear()
        self.gold.clear()
        self.jingyan.clear()
        self.xingdongli.clear()
        self.hp.clear()
        self.sudu.clear()
        self.wugong.clear()
        self.wufang.clear()
        self.fagong.clear()
        self.fafang.clear()
        self.baoji.clear()
        self.renxing.clear()
        self.shanbi.clear()
        self.mingzhong.clear()
        self.shijian.clear()

    def delete_juese(self):  #点击删除角色
        text=QtGui.QMessageBox.warning(self,u'警告',u'确定要删除角色吗？',QtGui.QMessageBox.Ok|QtGui.QMessageBox.No)
        #text.setStandardButtons(QtGui.QMessageBox.Ok|QtGui.QMessageBox.Cancel)
        #text.setButtonText(QtGui.QMessageBox.OK,QtCore.QString(u"确 定"))
        #text.setButtonText(QtGui.QMessageBox.Cancel,QtCore.QString(u"算 了"))
        # text=QtGui.QMessageBox.question(self,u'警告',u'确定要删除角色吗？')
        # QYES=text.addButton(u"确定", QtGui.QMessageBox.YesRole)
        # QNO=text.addButton(u"取消", QtGui.QMessageBox.NoRole)
        if text==QtGui.QMessageBox.Ok:
            pid=self.player_id
            db=pymysql.connect('localhost','root','','small_game',charset='utf8')
            cursor = db.cursor(pymysql.cursors.DictCursor)
            cursor.execute("DELETE from player_info where id='%s'"%pid)
            cursor.execute("DELETE from player_shuxing where id='%s'"%pid)
            db.commit()
            db.close()
            print("Delete player id:%s data in SQL."%pid)
            QtGui.QMessageBox.information(self,u'消息',u'角色已被成功删除！')
            self.clear_mainscreen()
            self.shanchu.setDisabled(True)  #删除角色后删除图标置灰
            self.beibao.setDisabled(True)
            self.shuxingjiadian.setDisabled(True)
            self.xuanzezhuangbei.setDisabled(True)
        else:
            return

    def fuhuoquan_huifu(self):
        if self.current_hp>=1:
            QtGui.QMessageBox.information(self,u'消息',u'角色未死亡,不需要复活！')
            return False
        else:
            choose=QtGui.QMessageBox.question(self,u'复活泉',u'是否要花费500金币复活？复活后恢复50%生命。',QtGui.QMessageBox.Yes,QtGui.QMessageBox.No)
            if choose==QtGui.QMessageBox.Yes:
                db=pymysql.connect('localhost','root','','small_game',charset='utf8')
                cursor = db.cursor(pymysql.cursors.DictCursor)
                cursor.execute("SELECT hp from player_shuxing where id='%s'"%self.player_id)
                hp=cursor.fetchall()
                hp_total=hp[0]['hp']
                cursor.execute("SELECT gold from player_info where id='%s'"%self.player_id)
                gold=cursor.fetchall()
                gold_total=gold[0]['gold']
                if gold_total>=500:
                    self.current_hp=hp_total//2
                    gold_total=gold_total-500
                    cursor.execute("update player_info set gold=%s where id='%s'"%(gold_total,self.player_id))
                    cursor.execute("update player_shuxing set current_hp=%s where id='%s'"%(self.current_hp,self.player_id))
                    self.hp.setText(str(self.current_hp)+'/'+str(hp_total))
                    self.gold.setText(str(gold_total))
                    QtGui.QMessageBox.information(self,u'提示',u'恢复成功！')
                else:
                    QtGui.QMessageBox.information(self,u'提示',u'金币不足，无法恢复！')
                db.commit()
                cursor.close()
                db.close()
            else:
                return

    def create_jihuoma(self,changdu=6):
        '''随机生成6位的激活码'''
        field=string.letters+string.digits
        jihuoma=''.join(random.sample(field,changdu))
        return jihuoma



if __name__ == '__main__':
    app=QtGui.QApplication(sys.argv)
    test=small_game()
    test.show()
    sys.exit(app.exec_())
    # test=xuanze_juese()
    # test.get_all_account()


