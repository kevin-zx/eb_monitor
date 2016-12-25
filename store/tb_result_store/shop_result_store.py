# -*- coding:utf8 -*-
from store.store_mysql import StoreMysql
from spider import config

class shopResultStore(object):
    def __init__(self):
        # self.db = StoreMysql(host="127.0.0.1", user="root", db="eb_monitor")
        self.db = StoreMysql(**config.TAOBAO_DB)

    def store(self, results, table):

        try:
            print len(results)
            for result in results:
                nid = result["nid"]
                sql = self.db.getupdatesql(table=table,data=result,field="nid")+"AND `collect_count` is null"
                # print sql
                self.db.do(sql)
        except Exception,e:
            print results
            print e
