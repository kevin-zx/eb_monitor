# -*- coding:utf8 -*-
from store.store_mysql import StoreMysql
from spider import config


class OtherResultStore(object):
    def __init__(self):
        # self.db = StoreMysql(host="127.0.0.1", user="root", db="eb_monitor")
        self.db = StoreMysql(**config.TAOBAO_DB)

    def store(self, results, table):
        for result in results:
            sql = self.db.getupdatesql(table=table,data=result,field="nid")+"AND `collect_count` is null"
            self.db.do(sql)
