# -*- coding:utf8 -*-
import urllib
import time
from webutil.html_downloader import HTMLLocalDownloader
from eb_extractor.taobao_extractor.list_extract.list_extractor import TbListExtractor


def get(keyword, page):
    urls = get_url(keyword, page)
    # print urls
    results = []
    for url in urls:
        headers = dict()
        headers["cookie"] = ""
        headers["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36"
        request_param = {"url": url, "headers": headers, "data": ""}
        html = HTMLLocalDownloader().get(request_param=request_param)
        le = TbListExtractor()
        rs = le.extractor(html["result"])
        results.extend(rs)
        if page == 1 and len(rs) != 35:
            break
    for i in range(0, len(results)):
        if page == 1:
            results[i]["rank"] = i
        else:
            results[i]["rank"] = (page - 2) * 41 + 47 + i
        # print results[i]

    return results


def get_url(keyword, page):
    urls = []
    unix_time = str(int(time.time() * 1000))
    data_value = (page - 1) * 44
    ss = (page - 2) * 44
    keyword = urllib.quote(keyword)
    apiurl = ""
    if ss < 0:
        ss = 0
        apiurl = "https://s.taobao.com/api?_ksTS={0}_302&callback=jsonp303&ajax=true&m=customized&rn=e54827016f39420ab98dbbaae15edf95&q={1}&imgfile=&js=1&style=grid&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20161116&ie=utf8&s=36&bcoffset=-1".format(
            unix_time, keyword)
    products_url = '''https://s.taobao.com/search?data-key=s&data-value={0}&ajax=true&_ksTS={1}_1181&callback=jsonp1182&q={2}&imgfile=&js=1&style=grid&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20161116&ie=utf8&bcoffset=0&ntoffset=6&p4ppushleft=1%2C48&s={3}''' \
        .format(data_value, unix_time, keyword, ss)
    urls.append(products_url)
    if apiurl != "":
        urls.append(apiurl)
    return urls


def main():
    print len(get("牛仔裤", 1))


if __name__ == '__main__':
    main()
