# -*- coding: utf-8 -*-
from store.store_mysql import StoreMysql
import datetime
from spider import config

class shopServiceStore(object):
    def __init__(self):
        self.db = StoreMysql(**config.TAOBAO_DB)
        # self.db = StoreMysql(host="127.0.0.1", user="root", db="eb_monitor")

    def store(self, proms, nid):
        try:
            s = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            # print  len(proms)
            for prom in proms:
                prom["product_id"] = nid
                # prom["insert_date"] = s
                self.db.save(table="shop_servicePromise", data=prom)

        except Exception, e:
            print e
            # print proms
            # print nid

def main():
    proms = []
    product = dict()
    product["descripTion"] ="BAOYOU"
    product["displayText"] = "BAIUOI"
    proms.append(product)
    re = shopServiceStore()
    re.store(proms,121)
    print 11


if __name__ == '__main__':
    main()