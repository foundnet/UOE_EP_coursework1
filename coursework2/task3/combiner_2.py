#!/usr/bin/python

import sys

cur_ids = ""
cur_cnt = 0
cur_uid = ""

for line in sys.stdin:
    str_uid,str_cnt,str_ids = line.split("\t",2)
    str_uid = str_uid.strip()
    str_cnt = str_cnt.strip()
    str_ids = str_ids.strip()
    
    if str_uid == "" or str_ids == "":
        continue
    if str_uid != cur_uid:
        if cur_uid != "":
            print cur_uid + "\t" + str(cur_cnt) + "\t" + cur_ids
        cur_uid = str_uid
        cur_cnt = int(str_cnt)
        cur_ids = str_ids
    else :
        cur_cnt = cur_cnt + int(str_cnt)
        cur_ids = cur_ids + ", " + str_ids

if cur_uid != "":
    print cur_uid + "\t" + str(cur_cnt) + "\t" + cur_ids
 
