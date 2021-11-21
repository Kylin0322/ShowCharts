#!/usr/bin/python
# -*- coding: UTF-8 -*-
import configparser
import os

G_config_path = ""
G_config_file_name = "report_config.ini"


class config():

    def __init__(self) -> None:
        self.c1 = configparser.ConfigParser()

    def create_config_file(self, Config_File_Name):
        '''create configration file on root path'''
        self.c1 = configparser.ConfigParser()
        self.c1['Path'] = {}
        self.c1['Path']['error_log'] = r'\log'
        self.c1['Path']['data_path'] = r'C:\TestLogSummary\UPH'
        self.c1['Path']['data_filename'] = ''
        self.c1['Path']['data_file_extension'] = '.cvs'
        self.c1['Path']['data_file_type'] = 'cvs'

        self.c1['Setting'] = {}
        self.c1['Setting']['S1'] = ""
        self.c1['Setting']['chart_FPY'] = '1'  # 打开关闭图标
        self.c1['Setting']['chart_Efficiency'] = '1'
        self.c1['Setting']['chart_UPH'] = '1'

        self.c1['AutoUpgrade'] = {}
        self.c1['AutoUpgrade']['g_upgrade_flag'] = "No"
        self.c1['AutoUpgrade']['g_upgrade_method'] = "File_Server"  # File_Server file server
        self.c1['AutoUpgrade']['g_upgrade_server'] = r""
        self.c1['AutoUpgrade']['g_upgrade_ftp_address'] = ""
        self.c1['AutoUpgrade']['g_upgrade_ftp_username'] = ""
        self.c1['AutoUpgrade']['g_upgrade_ftp_password'] = ""

        with open(Config_File_Name, 'w') as configfile:
            self.c1.write(configfile, False)

    def remove_remark(self):
        self.c1['Path']['data_file_type'] = self.c1['Path']['data_file_type'].split("#")[0].strip()
        self.c1['AutoUpgrade']['g_upgrade_method'] = self.c1['AutoUpgrade']['g_upgrade_method'].split("#")[0].strip()
        pass

    def get_config_file(self):
        ''' read config data from G_config_file_name, it will create a defalt if file not exist

            input:G_config_file_name
            output:self.c1
        '''
        # check config file exist
        Config_File_Name = os.path.join(os.getcwd(), G_config_file_name)
        if not os.path.isfile(Config_File_Name):
            # make config file if not present
            self.create_config_file(Config_File_Name)

        # make file name and path
        self.c1.read(Config_File_Name)
        self.remove_remark()

    def save_config_file(self):
        '''save current configration to file.
        '''
        # check config file exist
        Config_File_Name = os.path.join(os.getcwd(), G_config_file_name)
        with open(Config_File_Name, 'w') as configfile:
            self.c1.write(configfile, False)

    def add_item_to_config_file(self, section, key, value):
        '''add on item to config file and save to configration to file.

            input:section, key, value,G_config_file_name
            output:file G_config_file_name
        '''
        # check config file exist
        Config_File_Name = os.path.join(os.getcwd(), G_config_file_name)
        #self.c1 = get_config_file()
        self.c1[section][key] = value
        with open(Config_File_Name, 'w') as configfile:
            self.c1.write(configfile, False)

    def list_out_all_in_config(self):
        ''' list out all in config a
            input: Config
            output
        '''
        for i in self.c1:
            print('[' + i + ']')
            for j in self.c1[i]:
                print(j + "=" + self.c1[i].get(j))


if __name__ == '__main__':
    print("---- standard test data -------------")
    # get config file
    config = config()
    config.get_config_file()

    # print config file
    config.list_out_all_in_config()

    # print('---------------- read out key ----------')
    # T = int(config['Setting'].get('G_refresh_time').split(' ')[0])
    # print(T)
    # T = int(config['Setting'].get('G_fail_log_keep_time').split(' ')[0])
    # print(T)

    # save config file
    if config.c1['AutoUpgrade'].get('g_upgrade_flag') == "No":
        config.c1['AutoUpgrade']['g_upgrade_flag'] = "Yes"
    else:
        config.c1['AutoUpgrade']['g_upgrade_flag'] = "No"

    # config.save_config_file()
