# -*- coding: utf-8 -*-
from eb_extractor.taoxi_comm_extractor.dsrandcollectionextractor import DsrAndCollectionExtractor
import time
from webutil.html_downloader import HTMLLocalDownloader


class DsrAndCollectGet(object):
    def __init__(self):
        self.api_format_url = "https://count.taobao.com/counter3?_ksTS={0}_217&callback=jsonp218&keys=SM_368_dsr-{1},ICCP_1_{2}"
        pass

    def get(self, product_id, seller_id):
        unix_time = str(int(time.time() * 1000))
        c_url = self.api_format_url.format(unix_time, seller_id, product_id)
        headers = dict()
        headers["cookie"] = ""
        headers[
            "user-agent"] = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36"
        request_param = {"url": c_url, "headers": headers, "data": ""}
        hd = HTMLLocalDownloader()
        de = DsrAndCollectionExtractor()
        return de.extractor(hd.get(request_param)["result"])


def main():
    dg = DsrAndCollectGet()
    # productid ,userid
    print dg.get("539740166463", "2999179976")

if __name__ == '__main__':
    main()