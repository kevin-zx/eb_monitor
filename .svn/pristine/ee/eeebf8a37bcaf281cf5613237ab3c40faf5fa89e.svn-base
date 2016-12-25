# -*- coding: utf8 -*-
import threading
import time

import spider.taobao.taobao_spider.taobao_list_spider as taobao_list_spider
from lancher.task_server.taobao_task_server import TaobaoTaskServer
from store.tb_result_store.result_store import ResultStore
from spider.taobao.taobao_m_spider.taobao_m_spider import TbMListExtractor


class TaobaoLancher(object):
    def __init__(self):
        self.ts = TaobaoTaskServer()
        self.task_list = []
        self.device = 1
        self.complete_num = 0b000001
        self.uncomplete_num = 0b111110

    def get_all(self):
        self.task_list = self.ts.get(complete_num=self.complete_num)

        for task in self.task_list:
            while True:
                if threading.activeCount() < 4:
                    t = threading.Thread(target=self.exec_task, args=(task,));
                    t.start()
                    break
                else:
                    time.sleep(2)
        self.ts.reset_complete_info(self.uncomplete_num)

    def exec_task(self, task):
        rs1 = ResultStore()
        results = []
        for page in range(1, 6):
            print "id:{0} keyword:{1} page:{2}".format(task.keyword_id, task.keyword,page)
            rs = taobao_list_spider.get(str(task.keyword), page=page)

            if len(rs) == 0:
                break
            for r in rs:
                r["keyword_id"] = task.keyword_id
                if r["comment_count"] == "":
                    r["comment_count"] = 0
            results.extend(rs)
        rs1.store(results, device=self.device, complete_num=self.complete_num)


def main():
    tbl = TaobaoLancher()
    tbl.get_all()

if __name__ == '__main__':
    main()