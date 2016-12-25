# -*- coding:utf8 -*-
from store.store_mysql import StoreMysql
import datetime
from spider import config

class TaobaoTaskServer(object):
    def __init__(self):
        # self.db = StoreMysql(host="127.0.0.1", user="root", db="eb_monitor")
        self.db = StoreMysql(**config.TAOBAO_DB)

    def get(self, complete_num):
        s = datetime.datetime.now().strftime('%Y-%m-%d')
        task_list = []
        print "select id,keyword from keyword_task WHERE complete_info&{0} = 0 AND monitor_status=1".format(complete_num)
        db_datas = self.db.query("select id,keyword from keyword_task WHERE complete_info&{0} = 0 AND monitor_status=1".format(complete_num))

        for db_data in db_datas:
            task = Task(keyword_id=db_data[0], keyword=db_data[1])
            task_list.append(task)
        self.db.close()
        return task_list

    def reset_complete_info(self, complete_num):
        self.db.do("update keyword_task set complete_info=complete_info&{0}".format(complete_num))


class Task(object):
    def __init__(self, keyword_id, keyword):
        self.keyword_id = keyword_id
        self.keyword = keyword


def main():
    ts = TaobaoTaskServer()
    print ts.reset_complete_info(0b000010)
    pass

if __name__ == '__main__':
    main()
