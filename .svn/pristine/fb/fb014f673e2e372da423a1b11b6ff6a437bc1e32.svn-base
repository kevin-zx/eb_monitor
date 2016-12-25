# -*- coding: utf-8 -*-

import urllib
from webutil.html_downloader import HTMLLocalDownloader
import time


def get(keyword, cookie, start_date, end_date,  device=0):
    """
    :param keyword:拓词的主要关键词
    :param cookie: 登录cookie
    :param start_date: 开始时间
    :param end_date: 结束时间
    # :param recent: 获取的天数
    :param device: 设备id 0：所有终端 1：PC 2：移动
    :return: json str
    """
    recent = "7"
    keyword = urllib.quote(keyword)
    unix_time = str(int(time.time() * 1000))
    # url = "https://sycm.taobao.com/mq/searchword/relatedWord.json?dateRange="+start_date+"%7C"+end_date+"&dateType=recent" + recent + "&device="+device+"&keyword=" + keyword + "&token=b126a3794&_=" + unix_time

    # print url
    url = "https://sycm.taobao.com/mq/searchword/relatedWord.json?dateRange={0}%7C{1}&dateType=recent{2}&device={3}&keyword={4}&token=b126a3794&_={5}".format(start_date, end_date, recent, device, keyword, unix_time)
    print url
    headers = dict()
    headers["cookie"] = cookie
    headers["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36"
    request_param = {"url": url, "headers": headers, "data": ""}
    html_downloader = HTMLLocalDownloader()

    json_data = html_downloader.get(request_param)
    # print json_data
    return json_data
