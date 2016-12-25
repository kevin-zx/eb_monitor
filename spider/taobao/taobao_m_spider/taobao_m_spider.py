# -*- coding: utf8 -*-
import urllib
import time
from webutil.html_downloader import HTMLLocalDownloader
from eb_extractor.taobao_extractor.m_list_extractor.m_list_extractor import TbMListExtractor


def get(keyword, page):
    keyword = urllib.quote(keyword)
    url = "https://s.m.taobao.com/search?event_submit_do_new_search_auction=1&_input_charset=utf-8&topSearch=1&atype=b&searchfrom=1&action=home%3Aredirect_app_action&from=1&q={0}&sst=1&n=20&buying=buyitnow&m=api4h5&abtest=8&wlsort=8&style=list&closeModues=nav%2Cselecthot%2Conesearch&page={1}"\
        .format(keyword, page)
    # print url
    hd = HTMLLocalDownloader()
    headers = dict()
    headers["cookie"] = ""
    headers["user-agent"] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36"
    request_param = {"url": url, "headers": headers, "data": ""}
    html_result = hd.get(request_param)
    html = html_result['result']
    # print html
    results = TbMListExtractor().extractor(html)
    for i in range(0, len(results)):
        results[i]["rank"] = (page -1) * 20 + i
    return results


def main():
    print get("海尔床洁宝除螨仪吸尘器zb403f", 1)

if __name__ == '__main__':
    main()