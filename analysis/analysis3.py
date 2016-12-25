# -*- coding:utf8 -*-
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from store.store_mysql import StoreMysql
from spider import config
import threading
import time
import sys
import traceback
import csv


def load_2d_data(file_path, delimiter=","):
    row_data = np.loadtxt(fname=file_path, delimiter=delimiter)
    final_data = [];
    first_d = [];
    sec_d = [];
    for d in row_data:
        if len(d) == 2:
            first_d.append(d[0])
            sec_d.append(d[1])
    print type(sec_d[0])
    final_data.append(first_d)
    final_data.append(sec_d)
    return final_data


def plot_2d_line(data, xlabel,ylabel):
    plt.plot(data[0],data[1],"b-")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()


def fund(x, a, b, c, d):
    return a*np.exp(b*x) + c*np.exp(d*x)


def fit():
    # from scipy.optimize import curve_fit
    data = load_2d_data("data/data.txt", "	")
    import guess_start
    p0 = guess_start.guess(data[1],data[0])
    popt, pcov = curve_fit(fund, data[1], data[0],
                           p0=p0,
                           maxfev=1000000)
    plt.plot(data[1], data[0])
    # plt.ylabel("description_score")
    # plt.xlabel("rank")
    # print popt
    # popt = pcov[3]
    perr = np.sqrt(np.diag(pcov))
    print sum(perr)
    print fund(np.array(data[0]),popt[0],popt[1],popt[2],popt[3])
    data[1].sort()
    plt.plot(data[1],fund(np.array(data[1]),popt[0],popt[1],popt[2],popt[3]),"r-")
    plt.show()
    pass


def db_fit():
    st = StoreMysql(**config.TAOBAO_DB)
    data = st.query("SELECT keyword,count(1) c FROM eb_result_taobao LEFT JOIN keyword_task ON eb_result_taobao.keyword_id = keyword_task.id WHERE device = 2 GROUP BY keyword")
    for d in data:
        # if d[1] >= 600:
        keyword = d[0]
        print keyword
        db_curve_fit(keyword,d[1])


def db_curve_fit(keyword,count):
    if "/" in keyword or "\\" in keyword:
        return
    st = StoreMysql(**config.TAOBAO_DB)
    data1 = st.query(
        "SELECT rank,AVG(month_sales) FROM tmp_m where keyword = '{0}' group by rank".format(keyword))
    # csv.writer("d1/{0},{1}".format(keyword,"csv"))
    csvfile = file(unicode("d1/{0}.{1}".format(keyword,"csv"),"utf-8"), 'wb')
    writer = csv.writer(csvfile)
    # for dn in data1:
    writer.writerows(data1)
    csvfile.close()


def curv_f(d1, d2):
    end = 199
    distance = 0
    loop_count = 0
    bestend = 199
    import guess_start
    p0 = guess_start.guess(d1, d2)
    while True:
        loop_count += 1
        if end < 199:
            return curve_fit(fund, d1[0:bestend], d2[0:bestend],p0=p0,maxfev=100000)
        popt, pcov = curve_fit(fund, d1[0: end], d2[0: end],
                               p0,
                               maxfev=100000)

        perr = np.sqrt(np.diag(pcov))
        if np.isinf(sum(perr)) or np.isnan(sum(perr)):
            end = (end - 10)
            continue
        if distance == 0:
            distance = sum(perr)

        elif distance - sum(perr) > 10:
            distance = sum(perr)
            bestend = end

        print "第{0}轮: distance={1} end={2} bestdistance={3} bestend={4}".format(loop_count, sum(perr), end, distance, bestend)
        end = (end - 10)


def main():
    # fit()
    db_fit()
    pass

if __name__ == '__main__':
    main()
