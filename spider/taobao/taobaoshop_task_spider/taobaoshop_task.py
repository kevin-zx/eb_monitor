# -*- coding:utf8 -*-
from store.store_mysql import StoreMysql
from spider import config
import datetime
import time

class TaobaoTaskShopServer(object):
    def __init__(self):
        # self.db = StoreMysql(host="127.0.0.1", user="root", db="eb_monitor")
        self.db = StoreMysql(**config.TAOBAO_DB)

    def get(self, complete_num):
        s = datetime.datetime.now().strftime('%Y-%m-%d')
        task_list = []
        # db_datas = self.db.query("select id,shop_url from shop_monitor WHERE complete_info&{0} = 0 AND monitor_status=1".format(complete_num))
        db_datas = self.db.query("select id,shop_url,user_id from shop_monitor where querytype = 0")
        # print "select id,keyword from keyword_task WHERE complete_info&{0} = 0 AND monitor_status=1".format(complete_num)
        for db_data in db_datas:
            # task = Task(keyword_id=db_data[0], keyword=db_data[1])
            task = Task(shop_id=db_data[0], shop_url=db_data[1],user_id=db_data[2])
            task_list.append(task)
        # self.db.close()

        # "update shop_monitor set search_update_time = {0}   where id > 0".format(str(search_updatetime))
        search_updatetime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        self.db.query("update shop_monitor set search_update_time = '%s'   where id > 0" %(str(search_updatetime)))
        # print "update shop_monitor set search_update_time = '%s'   where id > 0" %(str(search_updatetime))
        return task_list

    def reset_complete_info(self, complete_num):
        self.db.do("update keyword_task set complete_info=complete_info&{0}".format(complete_num))


class Task(object):
    def __init__(self, shop_id, shop_url,user_id):
        self.shop_id = shop_id
        self.shop_url = shop_url
        self.user_id = user_id

def main():
    ts = TaobaoTaskShopServer()
    print ts.reset_complete_info(0b000010)
    pass

if __name__ == '__main__':
    main()
