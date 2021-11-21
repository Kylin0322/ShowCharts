
import os


def get_file_list(folder):
    ''' Get file list in path and reture with list, The list will sorted by modify date
        Input:folder
        Output:list[]
    '''
    list1 = []
    if os.path.isdir(folder):
        # Get all files in folder
        for row in os.listdir(folder):
            if os.path.isfile(os.path.join(folder, row)):
                list1.append(row)

        # 将文件按照最后修改时间顺序升序排列
        # os.path.getmtime() 获取文件最后修改时间
        # os.path.getctime() 获取文件最后创建时间
        list1 = sorted(list1, reverse=False, key=lambda x: os.path.getmtime(os.path.join(folder, x)))
        # ist1 = sorted(list1,reverse=True, key=lambda x: os.path.getmtime(os.path.join(folder, x)))
        return list1
    else:
        return ''


def get_file_contants(file_name):
    ''' Open file and return file contax as strin max size is 2048 Byte
        Input:file_name
        Output:reutren a str(list)
    '''
    try:
        file_obj = open(file_name, "r")
        str = file_obj.readlines()
        file_obj.close
        return str
    except IOError:
        return ""


def file_list_filiter(f_list, act1="remove", str1=""):
    '''从文件名的List中移除/或者保留，包含制定字符串的文件名
        input: f_list, act1, str1
        output: temp_list
    '''
    temp_list =[]
    if not str1 == "":
        if "remove" in act1:
            for i in f_list:
                if not str1 in i:
                    print("append file:",i)
                    temp_list.append(i)

        if "keep" in act1:
            for i in f_list:
                if str1 in i:
                    print("append file:",i)
                    temp_list.append(i)
        
    return temp_list

