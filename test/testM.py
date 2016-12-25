# -*- coding: utf-8 -*-

import csv

from eb_extractor.keyword_data_extractor import keyword_data_extractor
from spider.keyword_data import keyword_data_downloader
from store.store_mysql import StoreMysql
import sys
import datetime
from spider import config
# sys.set
reload(sys)
sys.setdefaultencoding("utf-8")


def expand_word(root_keyword, category, device):
    db = StoreMysql(**config.TAOBAO_DB)
    s = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cookie = "cna=udetDhAG+kMCATrS6eojPUd7; thw=cn; miid=8500937081866481993; ali_apache_id=10.103.188.156.1474443514900.823590.3; ali_ab=58.210.233.234.1472787076757.6; _cc_=W5iHLLyFfA%3D%3D; tg=0; _m_user_unitinfo_=unit|unsz; hng=CN%7Czh-cn%7CCNY; mt=ci=0_0&cyk=1_0; _m_unitapi_v_=1482385378664; _tb_token_=7731a38ae888e; linezing_session=huYLTnZDSH9LtKWwtMOqVjlc_148238676668855xb_5; _m_h5_tk=c0a92a14d6f151f972abb6d41b66461a_1482393253804; _m_h5_tk_enc=31f30fad1b0459f3fb07cdb296876c5a; x=1973353526; uc3=sg2=AiBidGoL%2FoFBQbTaaGEp6lDcR1Gii4LYDTDtQ9dTyv8%3D&nk2=&id2=&lg2=; uss=AnIswMYlFSKsB7QJe74tRE8fwoGng%2BZ%2FXy1VRQG9baa1uVZHJUWd1%2FpxtOc%3D; tracknick=; sn=lexy%E8%8E%B1%E5%85%8B%E5%AE%98%E6%96%B9%E6%97%97%E8%88%B0%E5%BA%97%3A%E9%97%BB%E9%81%93; skt=179ed0180fe2363f; _euacm_ac_l_uid_=2837068987; _euacm_ac_c_uid_=1973353526; _euacm_ac_rs_uid_=1973353526; _euacm_ac_v_md_=s; v=0; cookie2=3c34c380c07e0936775847c1d44753b5; unb=2837068987; t=b1927f421039a5707bf1951a146a60f2; _euacm_ac_rs_sid_=108524048; JSESSIONID=E305712BA0002AD9AE1321FA0B999936; uc1=cookie14=UoW%2FX97p3E2RKQ%3D%3D&lng=zh_CN; apush3d4d6ec9cf7304ca812e16cff06199f9=%7B%22ts%22%3A1482394638951%2C%22parentId%22%3A1482394628940%7D; isg=AufnzOpnc6WJf_jdYzHk0YeVdhvmp56qkFEWvblVenaeqARqwD70n2PurB_M; l=AioqichSuJrrvleYzSzeNrRY-prN4q72"
    start_date = "2016-12-12"
    end_date = "2016-12-18"
    json_str = keyword_data_downloader.get(keyword=root_keyword, cookie=cookie, start_date=start_date, end_date=end_date, device=device)["result"]
    print json_str
    json_data = keyword_data_extractor.extractor(json_str)

    dir_path = "{0}/{1}_{2}_{3}.csv".format("data", root_keyword, device, start_date)

    result_csv_file = open(unicode(dir_path), "wb")
    fieldnames = json_data[1].keys()
    fieldnames.append("main_keyword")
    fieldnames.append("start_date")
    fieldnames.append("end_date")
    fieldnames.append("device")
    fieldnames.append("category")
    writer = csv.DictWriter(f=result_csv_file, fieldnames=fieldnames)
    writer.writerow(dict(zip(fieldnames, fieldnames)))
    for json_item in json_data:
        json_item["main_keyword"] = root_keyword
        json_item["start_date"] = start_date
        json_item["end_date"] = end_date
        json_item["device"] = device
        json_item["category"] = category
        json_item["insert_date"] = s
        # writer.writerow(json_item)
        db.save(table="keyword_info_new", data=json_item)
    result_csv_file.close()

    pass



def main():
    datas = []
    data = {"category": "吸尘器",
            "keywords":["吸尘机", "吸尘器", "洗尘器"]}
    datas.append(data)
    data = {"category": "除螨仪",
            "keywords": ["除螨仪","除螨机","除螨吸尘器"]}
    datas.append(data)
    data = {"category": "扫地机",
            "keywords": ["扫地机", "扫地机器人", "扫地神器", "扫地电动"]}
    datas.append(data)
    data = {"category": "挂烫熨斗",
            "keywords": ["挂烫机", "挂烫熨斗", "蒸汽挂烫机", "蒸汽挂烫熨斗"]}
    datas.append(data)
    for data in datas:
        for keyword in data["keywords"]:
            expand_word(keyword, data["category"], 0)
            expand_word(keyword, data["category"], 1)
            expand_word(keyword, data["category"], 2)

if __name__ == '__main__':
    main()
