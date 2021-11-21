#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import time
import re
import uuid
import rsa
import verify_licence_file


Timestr = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
computer_name = os.environ['COMPUTERNAME'].lower()
EndYear = 2028
MAC = uuid.uuid1().hex[-12:].upper()
Pubkey = """
-----BEGIN RSA PUBLIC KEY-----
MIGJAoGBAIYzzMx15iLuytmIC8Ya1CmYpPCpM6GdFpJwvEhFdFr7wVqAppUvrPmO
kV4L2KtMtOW1HK0JlrJqNBAKxd8rSoUceNn3RDLib88/SnMy8VefOhreZu4cZeCq
d5zY3YzdXmb1tZT6dtPxg2j0TF44iKenAWhQnBdjMajO7zEWII+RAgMBAAE=
-----END RSA PUBLIC KEY-----
"""
# rint(Timestr)
# print(computer_name)
# print(EndYear)
# print(MAC)


def register(T="Time"):
    '''register check, 
       Input: Time,ComputerName, licence

    '''
    # print(T)
    T = T.lower()
    if T.lower()[0] == "t":
        year = int(Timestr[0:4])
        print("register until %s" % EndYear)
        if year < EndYear:
            return True
        else:
            with open('debuglog.log', mode='a') as f1:
                f1.writelines(mm)
            exit("register fail")
            os._exit("register fail")

    if T.lower()[0] == "c":
        print("register by %s" % computer_name)
        if "huahp" in computer_name:
            return True
        else:
            with open('debuglog.log', mode='a') as f1:
                f1.writelines(mm)
            exit("register fail")
            os._exit("register fail")

    if T.lower()[0] == "l":
        print("register by licence.txt on %s" % computer_name)
        if verify_licence_file.signature_license_verify() == True:
            return True
        else:
            mm = "register fail\n"
            with open('debuglog.log', mode='a') as f1:
                f1.writelines(mm)
            exit("register fail")
            os._exit("register fail")


if __name__ == '__main__':
    print("---- standard test data -------------")

    #print('register("Time"):', register("Time"))
    #print('register("ComputerName"):', register("ComputerName"))
    print('register("licence"):', register("licence"))

    print("---- standard test data -------------")
