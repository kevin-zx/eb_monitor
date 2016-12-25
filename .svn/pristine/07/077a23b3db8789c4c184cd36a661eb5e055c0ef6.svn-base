# -*- coding:utf8 -*-
from store.store_mysql import StoreMysql
from spider import config
import jieba


class Match:
    def __init__(self):
        self.db = StoreMysql(**config.TAOBAO_DB)
        self.match_threshold = 0.77
        pass

    def get_match_keyword_from_db(self, title, cats=["吸尘","洗尘"]):
        """
        根据title得出匹配哪些关键词
        :param title:商品的title
        :param cats:宝贝所在关键词类目 （tips:现在靠的是like main_word 的做法，是一个临时的解决方法，需要修复）
        :return:匹配关键词的数组和匹配度
        """
        datas = jieba.cut(title, cut_all=True)
        datas_str = "("
        for d in datas:
            datas_str += "lower('{0}'),".format(d)
        datas_str = datas_str[0:-1]+")"
        cats_str = "AND("
        for c in cats:
            cats_str += "main_word like '%{0}%' OR ".format(c)
        cats_str = "{0})".format(cats_str[0: -3])
        matched_keywords = self.db.query("SELECT * FROM "
                                         "( SELECT keyword,sum(score) sc "
                                         "from keyword_match_info_score  "
                                         "WHERE "
                                         "sub_keyword IN {0} "
                                         "{2} "
                                         "GROUP BY keyword ORDER BY sc desc) as c "
                                         "where sc > {1}".format(datas_str, self.match_threshold, cats_str))
        return matched_keywords


def main():
    m = Match()
    print m.get_match_keyword_from_db(u"小狗吸尘器家用超静音手持式除螨小型强力地毯式大功率D-526正品")
    # datas = jieba.cut(u"莱克吸尘器家用VC-PD501-3无线充电手持无绳便捷无耗材强力吸尘器", cut_all=True)
    # for d in datas:
    #     print d
    # pass

if __name__ == '__main__':
    main()