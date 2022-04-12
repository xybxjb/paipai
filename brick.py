import sys
import time
import redis
import json
import StringIO
import random
import base64
import xlrd
import csv


#####读配表生成配置文件
def reloadConfig():
    config = {}
    file_path = "./brick.xlsx"
    excel = xlrd.open_workbook(file_path,encoding_override="utf-8")
    all_sheet = excel.sheets()
    for sheet in all_sheet:
        if sheet.name == u"brick_reward":
            row = 4
            while row < sheet.nrows:
                val = sheet.row_values(row)
                sp = val[13].split(':')
                config[int(val[1])] = int(sp[1])
                row = row + 1
    return config

def main():
    config = reloadConfig()
    file_path = "./brick_user_level.xlsx"
    excel = xlrd.open_workbook(file_path,encoding_override="utf-8")
    all_sheet = excel.sheets()
    for sheet in all_sheet:
        if sheet.name == u"Sheet2":
            row = 1
            while row < sheet.nrows:
                val = sheet.row_values(row)
                award = config[int(val[1])] * 0.25 * int(val[2])
                print int(val[1]), award
                row = row + 1


if __name__ == "__main__":
    main()