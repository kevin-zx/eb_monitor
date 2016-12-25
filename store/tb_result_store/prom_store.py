# -*- coding: utf-8 -*-
from store.store_mysql import StoreMysql
import datetime
from spider import config

class PromStore(object):
    def __init__(self):
        self.db = StoreMysql(**config.TAOBAO_DB)
        # self.db = StoreMysql(host="127.0.0.1", user="root", db="eb_monitor")

    def store(self, proms, nid):
        s = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        for prom in proms:
            prom["nid"] = nid
            prom["insert_date"] = s
            self.db.save(table="promotion", data=prom)