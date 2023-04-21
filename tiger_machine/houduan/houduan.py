import random
import sys
import os
import configparser
libpath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if not libpath in sys.path:
    sys.path.append(libpath)

class analyse():
    def __init__(self):
        self.site_dict = {}
        self.money_rate = {}
        self.player_info = {}
        self.config_path = self.base_path('config.ini')
        self.pic_path = self.base_path('pic/')

    def read_config(self, *args):
        '''根据需要的信息，获取配置文件中的站点对应的税率，折扣名+对应折扣，积分配置，返回对应的字典'''
        # path=os.path.dirname(os.path.abspath(__file__))
        # config_path=path+'/config.ini'
        # print(config_path)
        config_path = self.config_path
        config=configparser.ConfigParser()
        config.read(config_path, encoding='utf-8')
        # need_return=[]
        sections= config.sections()  #拿到所有的section
        if len(config)>0:
            for section in sections:
                section=section.lower()
                if section in args:
                    print("Find %s items, output!" % section)
                    print(config.items(section))
                    item=dict(config.items(section))
                    # site_list = config.items('site')
                    # self.site_dict = dict(site_list)
                    # need_return.append(item)
                else:
                    print("Can not find section named:%s" % section)
            return_len=len(item)
            print("Totally find %s dicts keys, return them!"%return_len)
            # print(item)
            return item
        else:
            print("配置文件为空！")
            return False

    def base_path(self, path):
        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
            # print(application_path)
        elif __file__:
            application_path = os.path.dirname(__file__)
            # application_path = os.path.dirname(os.path.abspath(__file__))
            # print(application_path)
        # print(os.path.join('D:\pythonscrip\work_tool/tiger_machine\houduan', 'pic/'))
        #如果有一个组件是一个绝对路径，则在它之前的所有组件均会被舍弃,所以拼接的地址本身就不能带/
        # print(os.path.join(application_path, path))
        target_path=os.path.join(application_path, path)
        if not os.path.exists(target_path):
            target_path=os.path.join(application_path, 'houduan', path)
        return target_path

class houduan(analyse):
    def __init__(self):
        super().__init__()
        self.current_money = 100
        self.charge_time = 0
        self.total_pic_type={}
        self.pic_list=[]
        self.pic_match_type={} # 存储所有图片名称和其对应的类型的字典
        self.match_pic_type()
        self.get_all_rate()
        self.get_player_info()
        # self.config_path = self.base_path('/config.ini')
        # self.pic_path = self.base_path('/pic/')

    def get_total_pic_type(self):
        """获取所有的图片类型字典"""
        self.total_pic_type=self.read_config('pic_type')
        return self.total_pic_type

    def get_player_info(self):
        """获取用户信息，剩余金币和充值次数"""
        self.player_info = self.read_config('player')
        for key in self.player_info.keys():
            if self.player_info[key].isdigit():
                self.player_info[key] = int(self.player_info[key])
        # print(self.player_info)
        self.current_money = self.player_info['current_money']
        self.charge_time = self.player_info['charge_time']
        return self.player_info

    def get_all_rate(self):
        """获取所有条件的中奖倍率字典,将字典的值的str类型转成int"""
        self.money_rate = self.read_config('rate')
        for key in self.money_rate.keys():
            if self.money_rate[key].isdigit():
                self.money_rate[key] = int(self.money_rate[key])
        # print(self.money_rate)
        return self.money_rate

    def get_all_pic_file_name(self):
        # path = os.path.dirname(os.path.abspath(__file__))
        # path=path+'/pic'
        path = self.pic_path
        files=os.listdir(path)
        pic_list = []
        for f in files:
            if '.jpg' in f or '.png' in f or '.jpeg' in f or '.gif' in f:
                pic_list.append(f)
        return pic_list

    def match_pic_type(self):
        """将所有的图片做一次类型匹配，输出成字典"""
        self.pic_list=self.get_all_pic_file_name()
        self.get_total_pic_type()
        for pic in self.pic_list:
            pic_name = pic.split('.')[0]
            if pic_name in self.total_pic_type['wangzheng']:
                self.pic_match_type[pic]='wangzheng'
            elif pic_name in self.total_pic_type['kfc_taocan']:
                self.pic_match_type[pic]='kfc_taocan'
            else:
                self.pic_match_type[pic] = 'kfc_danpin'
        print(self.pic_match_type)
        return self.pic_match_type

    def get_pic_type(self, pic=''):
        """获取某张图片的类型"""
        # path = os.path.dirname(os.path.abspath(__file__))
        # path = path + '/pic/'
        path = self.pic_path
        pic = pic.replace(path, '')
        return self.pic_match_type[pic]

    def random_pic(self):
        """随机选择一张照片返回"""
        pic_list=self.pic_list
        # print(pic_list)
        # path = os.path.dirname(os.path.abspath(__file__))
        # path = path + '/pic/'
        path = self.pic_path
        # print(path+random.choice(pic_list))
        return path+random.choice(pic_list)

    def set_money_in_config(self, money=100):
        """把当前金币设置到config中"""
        # path = os.path.dirname(os.path.abspath(__file__))
        # config_path = path + '/config.ini'
        config_path = self.config_path
        config = configparser.ConfigParser()
        config.read(config_path, encoding='utf-8')
        config.set('player', 'current_money', str(money))
        config.write(open(config_path, 'r+'))

    def set_charge_time_in_config(self, times=0):
        """把已充值次数设置到config中"""
        # path = os.path.dirname(os.path.abspath(__file__))
        # config_path = path + '/config.ini'
        config_path = self.config_path
        config = configparser.ConfigParser()
        config.read(config_path, encoding='utf-8')
        config.set('player', 'charge_time', str(times))
        config.write(open(config_path, 'r+'))



if __name__=="__main__":
    test=houduan()
    test.get_player_info()