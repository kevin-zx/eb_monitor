# -*- coding:utf8 -*-
import threading
import time

from lancher.task_server.other_task_server import OtherTaskServer
from spider.taobao.taoxi_spider_util.dsr_and_collect_get import DsrAndCollectGet
from spider.taobao.taoxi_spider_util.product_info_get import ProductInfoGet
from spider.taobao.taoxi_spider_util.total_sell_get import TotalSellGet
# from store.tb_result_store.other_result_store import OtherResultStore

from store.tb_result_store.shop_result_store import shopResultStore
from store.tb_result_store.prom_store import PromStore
from store.tb_result_store.shopservice_store import shopServiceStore

# from spider.taobao.taobaoshop_task_spider.taobaoshop_tasklist import TaobaoTaskServer

class TaobaoOtherInfo(object):
    def __init__(self):
        self.ts = OtherTaskServer()
        # self.ts = TaobaoTaskServer()
        self.dsrcg = DsrAndCollectGet()
        self.prdctget = ProductInfoGet()
        self.totalg = TotalSellGet()
        self.shopService = shopServiceStore()

    def getall(self):
        while True:
            tasklist = self.ts.get(table="eb_shop_result")
            # if len(tasklist) == 0:
            #     tasklist = self.ts.get(table="m_eb_result")
            if len(tasklist) > 0:
                for task in tasklist:
                    while True:
                        # print threading.activeCount()
                        if threading.activeCount() < 50:
                            t = threading.Thread(target=self.exec_task, args=(task,));
                            # t.setDaemon(True)
                            t.start()
                            break
                        else:
                            time.sleep(0.2)
                time.sleep(3000)
            else:
                time.sleep(3000)

    def exec_task(self, task):
        rs = shopResultStore()
        ps = PromStore()
        # print task.nid
        shopService = shopServiceStore()
        result = dict()

        # if task.result_id % 100 == 0:
        # print task.result_id
        result["nid"] = task.nid
        data = self.dsrcg.get(task.nid, task.user_id)
        # print len(data)
        if len(data) > 1:
            result['delivery_score'] = data["delivery_score"]
            result["delivery_score_lv"] = data["delivery_score_lv"]
            result["delivery_score_de"] = data["delivery_score_de"]
            result['service_score'] = data["service_score"]
            result["service_score_lv"] = data["service_score_lv"]
            result["service_score_de"] = data["service_score_de"]
            result['description_score'] = data["description_score"]
            result["description_score_lv"] = data["description_score_lv"]
            result["description_score_de"] = data["description_score_de"]
        result['collect_count'] = data["collect_count"]
        # result, promotion_list, product_promiselist
        data1, proms,product_promiselist = self.prdctget.get(task.nid)
        # ps.store(proms, task.nid)
        # shop promise
        shopService.store(product_promiselist,task.nid)
        result["repayment"] = data1["repayment"]
        result["start_time"] = data1["start_time"]
        result["month_sales"] = data1.get("month_sales","0")

        if '00' in data1["view_fee"]:
            result["view_fee"] = 0.00
        else:
            result["view_fee"] = float(data1["view_fee"])
        # print float(data1["view_fee"])
        # result["view_fee"] = float(data1["view_fee"])
        data2 = self.totalg.get(task.nid)
        result["total_sales"] = data2["total_sales"]
        result["pic_url"] = data2["pic_url"]

        # result["result_id"] = task.result_id
        rs.store(results=[result], table="eb_shop_result")


def main():
    to = TaobaoOtherInfo()
    to.getall()


if __name__ == '__main__':
    main()