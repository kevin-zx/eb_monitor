# -*- coding:utf8 -*-
from store.store_mysql import StoreMysql
from spider import config

class TaobaoMTaskServer(object):
    def __init__(self):
        # self.db = StoreMysql(host="127.0.0.1", user="root", db="eb_monitor")
        self.db = StoreMysql(**config.TAOBAO_DB)

    def get(self):
        task_list = []
        db_datas = self.db.query("select keyword_id,keyword from keyword_info_m WHERE last_query_date < '{0}'")
        for db_data in db_datas:
            task = Task(keyword_id=db_data[0], keyword=db_data[1])
            task_list.append(task)
        self.db.close()
        return task_list


class Task(object):
    def __init__(self, keyword_id, keyword):
        self.keyword_id = keyword_id
        self.keyword = keyword


def main():
    ts = TaobaoMTaskServer()
    print len(ts.get())
    pass

if __name__ == '__main__':
    main()
