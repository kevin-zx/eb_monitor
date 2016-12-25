# -*- coding:utf-8 -*-
# https://ald.taobao.com/recommend.htm?refer=&callback=jsonp&recommendItemIds=16905959832&needCount=1&appID=03130&istmall
from eb_extractor.extractor import Extractor
import json
from webutil.html_downloader import HTMLLocalDownloader


class TotalSellExtractor(Extractor):
    def extractor(self, html_data):
        result = {"pic_url": "", "tatol_sales": "0"}
        # print html_data
        jsonstr = self.get_jsonstr_from_html(html_data)
        # print jsonstr
        jsondata = json.loads(jsonstr)

        item_list = jsondata.get("itemList")
        if item_list is not None and len(item_list) > 0:
            result["pic_url"] = item_list[0].get("img","")
            result["total_sales"] = item_list[0].get("sellNum", "0")
        return result


def main():
    url = '''https://ald.taobao.com/recommend.htm?refer=&callback=jsonp&recommendItemIds=41799734995&needCount=1&appID=03130&istmall'''
    hd = HTMLLocalDownloader()
    headers = dict()
    headers["cookie"] = ""
    # headers["referer"] = "https://detail.tmall.com/item.htm"
    headers[
        "user-agent"] = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36"
    request_param = {"url": url, "headers": headers, "data": ""}
    html = hd.get(request_param)["result"]
    print html

    ts = TotalSellExtractor()
    print ts.extractor(html)

if __name__ == '__main__':
    main()