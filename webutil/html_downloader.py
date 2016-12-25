# -*- coding: utf-8 -*-
# import sys
# import urllib.request
import urllib2
import traceback
import time


class HTMLLocalDownloader:
    def __init__(self):
        pass

    @staticmethod
    def encoding(data):
        types = ['utf-8', 'gb2312', 'gbk', 'gb18030', 'iso-8859-1']
        for t in types:
            try:
                return data.decode(t)
            except Exception, e:
                pass
        return None

    @staticmethod
    def get_from_db(self):
        time.sleep(10)
        return ""
        pass

    def get(self, request_param):
        """
        :param request_param:请求参数
        :return:result
        """
        result = {"status": "3", "result": "", "header": ""}
        url = request_param["url"]
        opener = urllib2.build_opener()
        if request_param["headers"].get("cookie") is not None:
            opener.addheaders.append(("Cookie", request_param["headers"]["cookie"]))
        request = urllib2.Request(url, headers=request_param["headers"])
        try:
            response = opener.open(request, timeout=20)
            header = response.info()
            body = response.read()
            if ('Content-Encoding' in header and header['Content-Encoding']) or \
                    ('content-encoding' in header and header['content-encoding']):
                import gzip
                import StringIO
                d = StringIO.StringIO(body)
                gz = gzip.GzipFile(fileobj=d)
                body = gz.read()
                gz.close()
            body = self.encoding(body)
            if body is not None:
                result["status"] = "2"
                result["result"] = body
                result["header"] = str(header)
        except Exception, e:
            traceback.print_exc()
            return result
        return result
