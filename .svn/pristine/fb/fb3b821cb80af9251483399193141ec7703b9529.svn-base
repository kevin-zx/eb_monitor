# -*- coding:utf-8 -*-
from pylab import *
import numpy as np
import pandas as pd
# from pylab import sort
def load_2d_data(file_path, delimiter=","):
    row_data = np.loadtxt(fname=file_path, delimiter=delimiter)
    final_data = [];
    first_d = [];
    sec_d = [];
    for d in row_data:
        if len(d) == 2:
            first_d.append(d[0])
            sec_d.append(d[1])
    # print type(sec_d[0])
    final_data.append(first_d)
    final_data.append(sec_d)
    return final_data

def guess(x, y):

    x = x[:]
    y = y[:]
    if np.any(np.diff(x) < 0):
        data = {"x": x, "y": y}
        frame = pd.DataFrame(data)
        frame = frame.sort(["x", "y"])
        x = frame.icol(0).tolist()
        y = frame.icol(1).tolist()
        # print x
    n = len(x)
    q = n/4
    # print x
    # print y
    if np.any(np.diff(np.diff(x)) > 1/(n**2) ):
        idx = (np.diff(x) < (np.spacing(1)**0.7))
        tx = []
        ty = []
        for i in range(0, len(idx)):
            if not idx[i]:
                tx.append(x[i])
                ty.append(y[i])

        tx.append(x[-1])
        ty.append(y[-1])
        x = tx
        y = ty
        n = len(x)
        if n < 2:
            start = rand(2, 1)
            return start
        q = n/4
        sid = np.sign(y)
        x1 = np.linspace(min(x), max(x), n)
        x1[-1] = x1[-1] - np.spacing(x1[-1])
        id = np.digitize(x1,x)
        for i in range(len(id)):
            if id[i] == n:
                id[i] = n -1
        y = np.log(np.abs(y)+np.spacing(1))

        b = []
        a = []
        cindx = 0
        for i in id:
            b.append((y[i] - y[i-1])/(x[i] - x[i-1]))
            a.append(y[i-1] - b[cindx]*x[i-1])
            cindx += 1
        sidm = np.matrix(sid)
        am = np.matrix(a)
        bm = np.matrix(b)
        x1m = np.matrix(x1)
        y = multiply(sidm,np.exp(am + multiply(bm, x1m)) ).tolist()[0]
        x = x1
        s = np.zeros((4,1))
        for i in range(0,4):
            for j in range(i*q+1,(i+1)*q+1,1):
                s[i] += y[j-1]
        tmp2 =2*(s[1]**2 - s[0]*s[2])

        while(tmp2 == 0 ):
            q = (q - 1)
            if q < 1:
                start = [0,0,0,0]
                return start
            for i in range(0,4):
                for j in range((i*q+1),(i+1)*q+1):
                    s[i] += y[j - 1]
            tmp2 = 2 * (s[1] ** 2 - s[0] * s[2])
        # print 1
        a, b = np, prod(s)
        # print b
        # print
        tmp = np.sqrt((s[0] ** 2) * (s[3] ** 2) - 6 * b - 3 * (s[1] ** 2) * (s[2] ** 2) + 4 * s[0] * s[2] ** 3 + 4 * (s[1] ** 3) * s[
            3])
        tmp1 = s[0]*s[3]-s[1]*s[2]
        tmp2 = 2*(s[1]**2 - s[0]*s[2])
        # print tmp1
        # print tmp2

        z1 = ((tmp - tmp1)/tmp2)[0]
        z2 = ((tmp + tmp1)/tmp2)[0]
        mx = np.mean(np.diff(x))
        if mx <= 0:
            s[1] = 1
            s[3] = 1
        else:
            s[1] = np.real(np.log((z1+0j)**(float(1)/float(q))))/mx
            s[3] = np.real(np.log((z2+0j)**(float(1)/float(q))))/mx
        exs1 = np.array(exp(s[1] * x))
        exs3 = np.array(exp(s[3] * x))
        exarr = np.array([exs1, exs3])
        texarr = exarr.T
        import scipy.optimize.nnls as nnls
        # spart = nnls(texarr, np.array(y))
        spart = np.linalg.lstsq(texarr, np.array(y))[0]
        # print np.linalg.lstsq(texarr, np.array(y))[0]
        # print spart
        s[0] = spart[0]
        s[2] = spart[1]
        return [s[0][0],s[1][0],s[2][0],s[3][0]]


def main():
    data = load_2d_data("data/month_sales.txt", "	")
    # data = load_2d_data("data/data.txt", "	")
    guess(data[1],data[0])
    # print np.zeros_like()

    # print np.zeros((3,1))
if __name__ == '__main__':
    main()
