# -*- coding: utf-8 -*-
import spider.taobao.taobao_spider.taobao_list_spider as tlg
from store.store_mysql import StoreMysql
import datetime
from spider import config
import time


class ResultStoreShop(object):
    def __init__(self):
        self.db = StoreMysql(**config.TAOBAO_DB)

    def store(self, results, device, complete_num):
        if len(results) <= 0:
            return
        s = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # keyword_id = results[0]["keyword_id"];
        # print len(results)
        for result in results:
            result["insert_date"] = s
            result["device"] = device
            result["create_date"] = time.strftime('%Y-%m-%d', time.localtime(time.time()))
            # print time.strftime('%Y-%m-%d', time.localtime(time.time()))
            self.db.save(table="eb_shop_result", data=result, mapping_fields={})
        # self.db.close()
        # self.db.do("update keyword_task set complete_info=complete_info|{0} where id = {1}".format(complete_num,keyword_id))
        # self.db.update(table="keyword_info_new", data={"last_query_date": s, "keyword_id": keyword_id},
        #                field="keyword_id")


def main():
    results = tlg.get("牛仔裤", 1)
    re = ResultStoreShop()
    re.store(results)
    pass


if __name__ == '__main__':
    main()
