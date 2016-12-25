# -*- coding:utf-8 -*-
import time
from webutil.html_downloader import HTMLLocalDownloader
from eb_extractor.taoxi_comm_extractor.commentextractor import CommentExtractor


class CommentCountGet:
    def __init__(self):
        self.api_format_url = "https://rate.taobao.com/detailCount.do?_ksTS={0}_99&callback=jsonp100&itemId={1}"

    def get(self, product_id):
        unix_time = str(int(time.time() * 1000))
        c_url = self.api_format_url.format(unix_time, product_id)
        headers = dict()
        headers["cookie"] = ""
        headers[
            "user-agent"] = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36"
        request_param = {"url": c_url, "headers": headers, "data": ""}
        ce = CommentExtractor()
        return ce.extractor(HTMLLocalDownloader().get(request_param)["result"])


def main():
    print CommentCountGet().get("21821291261")

if __name__ == '__main__':
    main()
