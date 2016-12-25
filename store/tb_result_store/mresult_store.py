# -*- coding: utf-8 -*-
import spider.taobao.taobao_spider.taobao_list_spider as tlg
from store.store_mysql import StoreMysql
import datetime
from spider import config

class MResultStore(object):
    def __init__(self):
        self.db = StoreMysql(**config.TAOBAO_DB)

    def store(self, results):
        s = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        keyword_id = results[0]["keyword_id"];
        for result in results:
            result["insert_date"] = s
            self.db.save(table="m_eb_result", data=result, mapping_fields={})
        self.db.update(table="keyword_info_m", data={"last_query_date": s, "keyword_id": keyword_id}, field="keyword_id")


def main():
    results = tlg.get("牛仔裤", 1)
    re = MResultStore()
    re.store(results)
    pass


if __name__ == '__main__':
    main()
