# -*- coding: utf-8 -*-
from eb_extractor.taoxi_comm_extractor.total_sell_extractor import TotalSellExtractor
from webutil.html_downloader import HTMLLocalDownloader


class TotalSellGet:
    def __init__(self):
        self.api_format_url = '''https://ald.taobao.com/recommend.htm?refer=&callback=jsonp&recommendItemIds={0}&needCount=1&appID=03130&istmall'''

    def get(self, product_id):
        curl = self.api_format_url.format(product_id)
        hd = HTMLLocalDownloader()
        headers = dict()
        headers["cookie"] = ""
        headers["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36"
        request_param = {"url": curl, "headers": headers, "data": ""}
        htmlresult = hd.get(request_param)
        te = TotalSellExtractor()
        result = te.extractor(htmlresult["result"])
        return result


def main():
    ts = TotalSellGet()
    print ts.get("16905959832")


if __name__ == '__main__':
    main()