#!/usr/bin/python
# -*- coding: UTF-8 -*-

import csv
import os
import time


class csv_read_write():
    def __init__(self):
        self.file_path = os.getcwd()
        self.file_name = "cnhuahpict12_2021-10-15.csv"
        self.file_name_full = os.path.join(self.file_path, self.file_name)
        self.csv_list = []
        self.Date = []
        self.Hour = []
        self.ModelName = []
        self.Total = []
        self.Pass = []
        self.Total1 = []
        self.Pass1 = []

    def csv_read(self):
        '''read out all data in csv file, and return
            input: self.file_path, self.file_name
            output: self.csv_file
        '''
        with open(self.file_name_full, "r") as csvFile:
            #readcsv = csv.reader(csvFile,delimiter='')
            readcsv = csv.reader(csvFile)
            for row in readcsv:
                self.csv_list.append(row)

        #print("self.csv_list length is %d", len(self.csv_list))
        return self.csv_list

    def format_csv_date(self):

        i = 0
        for row in self.csv_list:
            if i != 0:
                self.Date.append(row[0])
                self.Hour.append(int(row[1]))
                self.ModelName.append(row[2])
                self.Total.append(int(row[3]))
                self.Pass.append(int(row[4]))
                self.Total1.append(int(row[5]))
                self.Pass1.append(int(row[6]))
            i = 2

        # remove header
        # self.Date.pop(0)
        # self.Hour.pop(0)
        # self.ModelName.pop(0)
        # self.Total.pop(0)
        # self.Pass.pop(0)
        # self.Total1.pop(0)
        # self.Pass1.pop(0)

    def calculate_efficiency(self):
        self.efficiency = 0.65
        pass

    def csv_write(self):
        pass


if __name__ == '__main__':
    c1 = csv_read_write()
    c1.csv_read()
    t = c1.csv_list
    for i in t:
        # print(i)
        pass

    print("=======================")
    c1.format_csv_date()
    print(c1.Date)
    print(c1.ModelName)
    print(c1.Hour)
    print(c1.Total)
    print(c1.Pass)
    print(c1.Total1)
    print(c1.Pass1)
