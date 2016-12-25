# -*- coding: utf8 -*-
import threading
import time

import spider.taobao.taobao_m_spider.taobao_m_spider as taobao_m_list_spider
from lancher.task_server.taobao_task_server import TaobaoTaskServer
from store.tb_result_store.result_store import ResultStore


class TaobaomLancher(object):
    def __init__(self):
        self.ts = TaobaoTaskServer()
        self.task_list = []
        # self.c
        # self.rs = MResultServer()
        self.device = 2
        self.complete_num = 0b000010
        self.uncomplete_num = 0b111101

    def get_all(self):
        self.task_list = self.ts.get(complete_num=self.complete_num)
        print len(self.task_list)
        for task in self.task_list:
            while True:
                if threading.activeCount() < 4:
                    t = threading.Thread(target=self.exec_task, args=(task,));
                    # t.setDaemon(True)
                    t.start()
                    break
                else:
                    time.sleep(2)
        self.ts.reset_complete_info(self.uncomplete_num)

    def exec_task(self, task):
        rs1 = ResultStore()
        results = []
        # print str(task.keyword)
        print task.keyword_id
        for page in range(1, 11):
            # print page
            rs = taobao_m_list_spider.get(str(task.keyword), page=page)
            if len(rs) == 0:
                break
            for r in rs:
                r["keyword_id"] = task.keyword_id
            results.extend(rs)
        if len(results)>0:
            # rs1.store(results)
            rs1.store(results, device=self.device, complete_num=self.complete_num)
        else:
            results.append({"keyword_id":task.keyword_id})
            rs1.store(results, device=self.device, complete_num=self.complete_num)



def main():
    tbl = TaobaomLancher()
    tbl.get_all()

if __name__ == '__main__':
    main()