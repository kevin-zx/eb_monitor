# -*- coding: utf-8 -*-

import csv
#
# result = urllib2.quote("测试")
# print result
# print time.mktime(datetime.datetime.now().timetuple())
# print str(int(time.time()*1000))
# a = {"t": "1", "b": "2", "c": "3", "e": "4", "a": "a"}
# v = {"t": "1",  "c": "3", "e": "4", "a": "a"}
# csv_file = open("test.csv", "wb")
# writer = csv.DictWriter(csv_file, fieldnames=a.keys())
# writer.writerow(dict(zip(a.keys(), a.keys())))
# writer.writerow(a)
# writer.writerow(v)
# csv_file.close()
# b = {"t": "1", "b": "2", "c": "3"}
# print a.keys()
# print a.values()
# print b.keys()
# print b.values()

# import re
# a = "小狗<span class=H>吸尘器家用</span>超静音小型强力除螨仪大吸力大功率无耗<span class=H>吸尘器家用</span>材机D-9005"
# reObject = re.compile("H>.+?<")
# b = reObject.findall(a)
# print len(b)
# reObject = re.search("H>.+?<", a)
# print reObject.find
# print reObject.group(0)
# print reObject.group(1)
import time
import datetime
# print  datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S');

a = 5
b = 4
c = 2
d = 0b1001
print d
# print -~d
print a & b
print a | c
