# -*- coding:utf-8 -*-
from store.store_mysql import StoreMysql
from spider import config
import numpy as np
import jieba
def f2():
    st = StoreMysql(**config.TAOBAO_DB)
    f = open(name="data/keyword_task.txt", mode="r")
    tmpkeyword = ""
    tmp_sub_data = []
    while True:
        line = f.readline()
        data = line.split(",")
        keyword = data[0]
        if tmpkeyword != keyword:
            for s in tmp_sub_data:
                if len(s) > 0:
                    tmpkeyword = tmpkeyword.strip()
                    re = {"sub_keyword": s, "keyword": tmpkeyword}
                    st.save("keyword_match_info", re)
                tmp_sub_data = []
            tmpkeyword = keyword
        subkeys = jieba.cut(data[0],cut_all=True)
        for sub in subkeys:
            sub = sub.strip()
            if sub not in tmp_sub_data:
                tmp_sub_data.append(sub)
        if len(line) <= 0:
            break
    f.close()

def f():
    st = StoreMysql(**config.TAOBAO_DB)
    f = open(name="data/redword.txt",mode="r")
    tmpkeyword = ""
    tmp_sub_data = []
    while True:
        line = f.readline()
        data = line.split(",")
        keyword = data[1]
        if tmpkeyword != keyword:
            for s in tmp_sub_data:
                if len(s) > 0:
                    re = {"sub_keyword": s, "keyword": tmpkeyword}
                    st.save("keyword_match_info", re)
                tmp_sub_data = []
            tmpkeyword = keyword
        subkeys = data[0].split("&")
        for sub in subkeys:
            sub = sub.strip()
            if sub not in tmp_sub_data and len(sub)>0 and sub != " " :
                tmp_sub_data.append(sub)
        if len(line) <= 0:
            break
    f.close()


def main():
    # f2()
    f()

if __name__ == '__main__':
    main()