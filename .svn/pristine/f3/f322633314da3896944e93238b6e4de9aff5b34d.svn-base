# -*- coding:utf8 -*-
from store.store_mysql import StoreMysql
from spider import config

class OtherTaskServer(object):
    def __init__(self):
        self.db = StoreMysql(**config.TAOBAO_DB)

    def get(self, table):
        taskList = []
        self.db.query("DELETE FROM eb_result_taobao WHERE nid is null")
        db_datas = self.db.query("select result_id,user_id,nid from {0} WHERE collect_count IS NULL GROUP BY nid order by result_id limit 4000".format(table))
        for db_data in db_datas:
            # print str(db_data[0])+''
            taskList.append(Task(db_data[0],db_data[1],db_data[2]))
        return taskList


class Task(object):
    def __init__(self, result_id, user_id=None, nid=None):
        self.result_id = result_id
        self.user_id = user_id
        self.nid = nid


def main():
    print OtherTaskServer().get("m_eb_result")


if __name__ == '__main__':
    main()