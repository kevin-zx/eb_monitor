# -*- coding:utf8 -*-
from store.store_mysql import StoreMysql
from spider import config
from sub_group import SubGroup


def store(tmp_ar, tmp_key, main_wd):
    sg = SubGroup(keyword=tmp_key,main_word=main_wd)
    for s in tmp_arr:
        sg.append(s)
    sg.set_score()


st = StoreMysql(**config.TAOBAO_DB)
data = st.query("SELECT keyword,sub_keyword,main_word,CHAR_LENGTH(sub_keyword) l FROM keyword_match_info_score ORDER BY keyword,l desc")
tmp_keyword = data[0][0]
tmp_arr = []
tmp_m = data[0][2]
for d in data:
    keyword = d[0]
    sub = d[1]
    main_word = d[2]
    if tmp_keyword == keyword:
        tmp_arr.append(sub)
    else:
        store(tmp_arr, tmp_keyword, tmp_m)
        tmp_keyword = keyword
        tmp_arr = [sub]
        tmp_m = main_word

store(tmp_arr,tmp_keyword, tmp_m)
st.close()

