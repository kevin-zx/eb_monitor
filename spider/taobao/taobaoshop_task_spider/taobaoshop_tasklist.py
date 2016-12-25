# -*- coding:utf8 -*-
import threading
import time

from lancher.task_server.other_task_server import OtherTaskServer
from spider.taobao.taoxi_spider_util.dsr_and_collect_get import DsrAndCollectGet
from spider.taobao.taoxi_spider_util.product_info_get import ProductInfoGet
from spider.taobao.taoxi_spider_util.total_sell_get import TotalSellGet
from store.tb_result_store.other_result_store import OtherResultStore
from store.tb_result_store.prom_store import PromStore


class TaobaoOtherInfoShop(object):
    def __init__(self):
        self.ts = OtherTaskServer()
        self.dsrcg = DsrAndCollectGet()
        self.prdctget = ProductInfoGet()
        self.totalg = TotalSellGet()

    def getall(self):
        while True:
            tasklist = self.ts.get(table="eb_shop_result")
            # if len(tasklist) == 0:
            #     tasklist = self.ts.get(table="m_eb_result")
            if len(tasklist) > 0:
                for task in tasklist:
                    while True:
                        # print threading.activeCount()
                        if threading.activeCount() < 30:
                            t = threading.Thread(target=self.exec_task, args=(task,));
                            t.setDaemon(True)
                            t.start()
                            break
                        else:
                            time.sleep(0.1)
            else:
                time.sleep(30)

    def exec_task(self, task):
        rs = OtherResultStore()
        ps = PromStore()
        result = dict()
        # result["result_id"] = task.result_id
        # a.endswith()
        if task.result_id % 100 == 0:
            print task.result_id
        result["nid"] = task.nid
        data = self.dsrcg.get(task.nid, task.user_id)
        if len(data) > 1:
            result['delivery_score'] = data["c"]
            result["delivery_score_lv"] = data["c_UFB"]
            result["delivery_score_de"] = data["c_g"]
            result['service_score'] = data["s"]
            result["service_score_lv"] = data["s_UFB"]
            result["service_score_de"] = data["s_g"]
            result['description_score'] = data["m"]
            result["description_score_lv"] = data["m_UFB"]
            result["description_score_de"] = data["m_g"]
        result['collect_count'] = data["collect_count"]

        data1, proms = self.prdctget.get(task.nid)
        # print proms
        ps.store(proms, task.nid)
        result["start_time"] = data1["start_time"]
        result["month_sales"] = data1.get("month_sales","0")
        data2 = self.totalg.get(task.nid)
        result["total_sales"] = data2["total_sales"]
        result["pic_url"] = data2["pic_url"]

        rs.store(results=[result], table="eb_shop_result")
        # rs.store(results=[result], table="eb_result")


def main():
    to = TaobaoOtherInfo()
    to.getall()


if __name__ == '__main__':
    main()