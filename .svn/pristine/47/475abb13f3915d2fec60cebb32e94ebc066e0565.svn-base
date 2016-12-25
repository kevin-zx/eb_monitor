# -*- coding:utf-8 -*-
import numpy as np
from store.store_mysql import StoreMysql
from spider import config
import matplotlib.pyplot as plt


def fund(x, a, b, c, d,scale = 1):
    print scale
    return (a*np.exp(b*x) + c*np.exp(d*x))*scale

st = StoreMysql(**config.TAOBAO_DB)
data = st.query("select * from fit_args_copy where distance > 0.4")
print data

# print "count".
for d in data:
    print d[1]
    print "avg_price:{0} count:{1}".format(d[7], d[8])
    # range(start=0, step=1, stop=100)
    d1 = st.query("select * from fit_args_t_copy where keyword = '{0}'".format(d[1],"utf-8"))[0]
    plt.clf()
    try:
        diff = fund(np.array([0, 100]), d[2], d[3], d[4], d[5])
        diff2 = fund(np.array([0, 100]), d1[2], d1[3], d1[4], d1[5], d1[6])
        print "diff1:{0}".format(diff[0] - diff[1])
        print "diff2:{0}".format(diff2[0] - diff2[1])
        plt.plot(range(0,  100), fund(np.array(range(0,  100)), d[2], d[3], d[4], d[5]), "r-")
        if len(d1) > 0 :
            plt.plot(range(0, 100), fund(np.array(range(0, 100)), d1[2], d1[3], d1[4], d1[5], d1[6]), "b-")
    except:
        continue
    plt.show()
# print range(0,  200)
