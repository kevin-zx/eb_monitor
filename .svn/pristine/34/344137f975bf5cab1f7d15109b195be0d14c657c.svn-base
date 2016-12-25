# -*- coding: utf8 -*-
import threading
import time
# from Queue import Queue
# from Queue import Empty

# import spider.taobao.taobao_spider.taobao_list_spider as taobao_list_spider
# from lancher.task_server.taobao_task_server import TaobaoTaskServer

# import spider.taobao.taobaoshop_task_spider.taobaoshop_list_spider as taobaoshop_list_spider
# from taobaoshop_task_spider import taobaoshop_list_spider
from spider.taobao.taobaoshop_task_spider import taobaoshop_list_spider
from spider.taobao.taobaoshop_task_spider.taobaoshop_task import TaobaoTaskShopServer
# from store.tb_result_store.result_store import ResultStore

from store.tb_result_store.shoplist_store import ResultStoreShop
# from spider.taobao.taobao_m_spider.taobao_m_spider import TbMListExtractor

class TaobaoShoplist(object):
    def __init__(self):
        # self.ts = TaobaoTaskServer()
        self.ts = TaobaoTaskShopServer()
        self.task_list = []
        self.device = 1
        self.complete_num=0b000001
        self.uncomplete_num=0b111110

        # self.store_queue = Queue()
        # self.device = 2
        # self.complete_num = 0b000010
        # self.uncomplete_num = 0b111101

    def get_all(self):
        while True:
            self.task_list = self.ts.get(complete_num=self.complete_num)
            # print len(self.task_list)
            tasklistlen = len(self.task_list)
            if  tasklistlen > 0:
                for task in self.task_list:
                    while True:
                        # print threading.activeCount()
                        if threading.activeCount() < 8:
                            t = threading.Thread(target=self.exec_task, args=(task,));
                            # t.setDaemon(True)
                            t.start()
                            tasklistlen -= 1
                            break
                        else:
                            time.sleep(0.2)
                # tasklistlen > 0 also sleep 3000
                time.sleep(3000)
            else:
                time.sleep(3000)
                    # time.sleep(20)
                # self.ts.reset_complete_info(self.uncomplete_num)

    def exec_task(self, task):

        rs1 = ResultStoreShop()
        results = []
        # for page in range(1, 6):
        # print "id:{0} shop_url:{1}".format(task.shop_id, task.shop_url)
        rs,maxPage = taobaoshop_list_spider.get(str(task.shop_url), page=1,user_id=str(task.user_id))

        for r in rs:
            r["shop_id"] = task.shop_id
            # if r["comment_count"] == "":
            r["comment_count"] = 0
        results.extend(rs)
        rs1.store(results, device=self.device, complete_num=self.complete_num)
        maxp = int(maxPage)
        print maxp
        if(maxp > 1):
            for page in range(2, maxp):
                # empty  results
                results = []
                rs, maxp = taobaoshop_list_spider.get(str(task.shop_url), page=page, user_id=str(task.user_id))
                for r in rs:
                    r["shop_id"] = task.shop_id
                    # if r["comment_count"] == "":
                    r["comment_count"] = 0
                results.extend(rs)
                rs1.store(results, device=self.device, complete_num=self.complete_num)


def main():
    tbl = TaobaoShoplist()
    tbl.get_all()

if __name__ == '__main__':
    main()