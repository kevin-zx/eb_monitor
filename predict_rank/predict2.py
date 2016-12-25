# -*- coding:utf-8 -*-
from store.store_mysql import StoreMysql
from spider import config
import numpy as np
# import matplotlib.pyplot as plt
from title_matcher.match import Match

class Prediction:
    def __init__(self):
        self.db = StoreMysql(**config.TAOBAO_DB)
        self.keyword_fit_distance_threshold = 0.4
        self.confidence_bounds = 1000
        pass

    def get_comm_keyword_fit(self, keyword):
        """
        获取根据行业数据和关键词数据进行缩放后的二项指数函数的参数
        :param keyword: 关键词
        :return: 是一个二项指数函数的参数
            函数 f(x) = (a*exp(b*x) + c*exp(d*x))
        """
        keyword_fit = self.db.query(
            "select `a`,`b`,`c`,`d`,`scale` from fit_args_t where keyword = '{0}'".format(keyword))
        if len(keyword_fit) > 0:
            return keyword_fit[0]
        else:
            return None

    def get_keyword_fit(self, keyword):
        """
        获取关键词本身数据fit出来的参数
        :param keyword:关键词
        :return: 是一个二项指数函数的参数
            函数 f(x) = a*exp(b*x) + c*exp(d*x)
        """
        keyword_fit = self.db.query(
            "select `a`,`b`,`c`,`d` from fit_args where distance > {0} and keyword = '{1}'".format(
                self.keyword_fit_distance_threshold, keyword))
        if len(keyword_fit) > 0:
            return keyword_fit[0]
        else:
            return None

    def get_confidence_coefficients(self, keyword_fit_args, comm_fit_args):
        """
        选择自身数据拟合还是行业数据拟合
        目前的经验来看自身数据拟合数据要准确的多
        :param keyword_fit_args:自身数据得出的拟合曲线
        :param comm_fit_args:行业数据得出的拟合曲线
        :return: 两者拟合曲线中的一个
        """
        if keyword_fit_args is None:
            # print "choose comm"
            return comm_fit_args
        else:
            return keyword_fit_args

            # fit_min, fit_max_bounds = self.get_fit_bounds(keyword_fit_args)
            # comm_fit_min, comm_fit_max_bounds = self.get_fit_bounds(comm_fit_args)
            # if comm_fit_min/fit_min > 2 and fit_max_bounds/comm_fit_max_bounds > 2:
            #     return comm_fit_args
            # else:
            #     return keyword_fit_args

    # def get_fit_bounds(self, fit_args):
    #     """
    #     用来选择是使用行业拟合曲线还是自身的拟合曲线
    #     :param fit_args:
    #     :return:
    #     """
    #     a = fit_args[0]
    #     b = fit_args[1]
    #     c = fit_args[2]
    #     d = fit_args[3]
    #     if len(fit_args) > 4:
    #         scale = fit_args[4]
    #     else:
    #         scale = 1
    #     min_rank = fund(0, a, b, c, d, scale)
    #     for i in range(1, 100000):
    #         if fund(i, a, b, c, d, scale) < 1:
    #             break;
    #     return min_rank, i

    def match_cat(self, keyword, cat):
        # print keyword
        # print cat
        sql = "select 1 from cat_data LEFT JOIN keyword_task ON cat_data.keyword_id = keyword_task.id WHERE keyword_task.keyword='{0}' and category='{1}' limit 1".format(
            keyword, cat)
        # print sql
        data = self.db.query(sql)
        # print data
        if len(data) != 0:
            return 0
        else:
            return 100

    def pre(self, keyword, month_sales):
        """
        预测排名
        这里是根据关键词和月销预测
        :param keyword:
        :param month_sales:
        :return:
        预测出的排名
        """
        keyword_fit = self.get_keyword_fit(keyword)
        comm_keyword_fit = self.get_comm_keyword_fit(keyword)
        final_fit = self.get_confidence_coefficients(keyword_fit, comm_keyword_fit)
        # print self.get_confidence_coefficients(comm_keyword_fit)
        # try:
        # plt.clf()
        # if keyword_fit is not None:
        #     plt.plot(range(0, 10000), fund(np.array(range(0, 10000)), keyword_fit[0], keyword_fit[1], keyword_fit[2], keyword_fit[3]), "r-")
        # if len(comm_keyword_fit) > 0:
        #     plt.plot(range(0, 10000), fund(np.array(range(0, 10000)), comm_keyword_fit[0], comm_keyword_fit[1], comm_keyword_fit[2], comm_keyword_fit[3], comm_keyword_fit[4]), "b-")
        # plt.show()
        if len(final_fit) == 4:
            return get_rank_by_fund(month_sales, final_fit[0], final_fit[1], final_fit[2], final_fit[3])
        else:
            return get_rank_by_fund(month_sales, final_fit[0], final_fit[1], final_fit[2], final_fit[3], final_fit[4])


def get_rank_by_fund(month_sale, a, b, c, d, scale=1):
    min_rank = 200
    min_de = -1
    # last_de = 0
    for i in range(0,200):
        de = (fund(i,a,b,c,d,scale)-month_sale)**2
        if min_de == -1:
            min_de = de
            min_rank = i
        elif de< min_de:
            min_de = de
            min_rank = i
        else:
            break
    return min_rank


def fund(x, a, b, c, d, scale=1):
    """
    拟合曲线方程
    是一个二项指数函数
    :param x:输入数据
    :param a:
    :param b:
    :param c:
    :param d:
    :param scale:这个参数是给行业拟合曲线来用的，因为行业拟合曲线是根据行业数据缩放得来的
    所以这个就是缩放值
    :return:
    拟合出的排名
    """
    return (a * np.exp(b * x) + c * np.exp(d * x)) * scale


def fit(title, monthsales, data_nid, category):
    db = StoreMysql(**config.TAOBAO_DB)
    p = Prediction()

    m = Match()
    allkeyword = m.get_match_keyword_from_db(title)
    result = []

    for d in allkeyword:
        result.append([d[0], p.pre(d[0], monthsales), p.pre(d[0], monthsales) * float(1 / d[1])])
    real = db.query(
        "select keyword,AVG(rank),count(1) from eb_result_taobao LEFT JOIN keyword_task ON keyword_id = keyword_task.id where nid = '{0}' AND device = '2' AND eb_result_taobao.insert_date > '2016-12-12 00:00:00' GROUP BY keyword_id;".format(
            data_nid))
    # print "select keyword,AVG(rank),count(1) from eb_result_taobao LEFT JOIN keyword_task ON keyword_id = keyword_task.id where nid = '{0}' GROUP BY keyword_id;".format(
    #         data_nid)
    cal = []
    cal1 = []
    for r in result:
        # print [1]
        # print d[1]
        # print d[0]
        # if real[2] < 2:
        #     continue
        for d in real:
            # print d[2]
            if r[0] == d[0]:
                m = p.match_cat(d[0], category)
                a = m+float(d[1])
                if m == 100:

                    continue
                print "real:{0},p:{1},o:{2},keyword:{3},count:{4}".format(r[1], a, float(d[1]), d[0], d[2])
                    # print r[1]
                    # print a
                    # print float(d[1])
                cal.append((((r[1]) - float(d[1])) ** 2) ** 0.5)
                cal1.append((((r[2]) - float(d[1])) ** 2) ** 0.5)
                break
    if len(cal) == 0:
        return 0, 0, 0
    return sum(cal) / len(cal), sum(cal1) / len(cal), len(cal)


# def main():
#     print get_rank_by_fund(2000, 8862, -0.147, 1112, -0.01936)

def main():
    db = StoreMysql(**config.TAOBAO_DB)
    datas = db.query(
        "SELECT nid,month_sales,COUNT(1) c,raw_title,category FROM eb_result_taobao  WHERE month_sales > 100 and device =2 AND nid='524802820682' GROUP BY nid order by c desc limit 300")
    csvfile = open("result3.csv", "a+")
    for d in datas:
        s, s1, l = fit(title=d[3], monthsales=d[1], data_nid=d[0],category=d[4])
        if l != 0:
            print "{0},{1},{2},{3},{4},{5}\r".format(d[3], d[2], s, l, s1, d[0])
            csvfile.write(unicode("{0},{1},{2},{3},{4},{5}\r".format(d[3], d[2], s, l, s1, d[0]), "utf-8"))
            csvfile.flush()
    csvfile.close()


if __name__ == '__main__':
    main()
