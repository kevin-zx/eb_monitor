# -*- coding: utf-8 -*-
from eb_extractor.taoxi_comm_extractor.product_info_extractor import ProductInfoExtractor
from webutil.html_downloader import HTMLLocalDownloader


class ProductInfoGet(object):
    def __init__(self):
        self.api_format_url = "https://mdskip.taobao.com/core/initItemDetail.htm?progressiveSupport=true&itemId={0}&areaId=330100&tmallBuySupport=true&queryMemberRight=true&callback=setMdskip"

    def get(self, product_id):
        c_url = self.api_format_url.format(product_id)
        hd = HTMLLocalDownloader()
        headers = dict()
        headers["cookie"] = '''cna=udetDhAG+kMCATrS6eojPUd7; thw=cn; miid=8500937081866481993; ali_ab=58.210.233.234.1472787076757.6; ali_apache_id=10.103.188.156.1474443514900.823590.3; hng=CN%7Czh-cn%7CCNY; _m_h5_tk=736c842806698c479e161d65e1efa01b_1479377404697; _m_h5_tk_enc=7ec44e68aca8041b678913a45edf8227; _m_user_unitinfo_=unit|unsz; _m_unitapi_v_=1478069694624; x=1973353526; uss=VvkmnyCLe7M81WS76%2FLI9wZjvmcxkxA5HWAqTi1cpzfZV00gZzJrvOGR4mA%3D; v=0; uc3=sg2=AiBidGoL%2FoFBQbTaaGEp6lDcR1Gii4LYDTDtQ9dTyv8%3D&nk2=F5QqboH0gOPanQ%3D%3D&id2=W8gzaQ7Xbn7H&vt3=F8dARHD6oZgMK0tB4gA%3D&lg2=VFC%2FuZ9ayeYq2g%3D%3D; existShop=MTQ3OTY5ODI3OA%3D%3D; lgc=tb_6442664; tracknick=tb_6442664; cookie2=1751b247bce3dc5a78c7fd373e1a5bcd; sg=40d; mt=np=&ci=2_1&cyk=1_1; cookie1=BvXjvOrzB6Hjv%2FqAVNk9ASMo8r4Tp1ahB0kuYAOyFTw%3D; unb=810537450; skt=bce85d267040a2cc; t=b1927f421039a5707bf1951a146a60f2; _cc_=VT5L2FSpdA%3D%3D; tg=0; _l_g_=Ug%3D%3D; _nk_=tb_6442664; cookie17=W8gzaQ7Xbn7H; _tb_token_=Tdiw6CS7FANn; linezing_session=kqmlEJhmavGxcaH9Opg7ABcT_1479698313770t3Go_2; uc1=cookie14=UoWwLQZnpEV8uQ%3D%3D&lng=zh_CN&cookie16=V32FPkk%2FxXMk5UvIbNtImtMfJQ%3D%3D&existShop=false&cookie21=W5iHLLyFe3xm&tag=3&cookie15=U%2BGCWk%2F75gdr5Q%3D%3D&pas=0; l=AlhY9GJ2CkT1pEWua0aMsZ7iqIzqd7zI; isg=AsPDNmCDnxjpA1zxL2UYJYOpUoc9lFd6FN2y0fWgKCKatOLWfQkmywomSPMA; ubn=p; ucn=unsz'''
        # print c_url
        headers["referer"] = "https://detail.tmall.com/item.htm"
        headers[
            "user-agent"] = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36"
        request_param = {"url": c_url, "headers": headers, "data": ""}
        html_result = hd.get(request_param)
        pe = ProductInfoExtractor()
        result, promotion_list, product_promiselist = pe.extractor(html_result.get("result"))

        while 'exception' in result:
            c_url = self.api_format_url.format(product_id)
            hd = HTMLLocalDownloader()
            headers = dict()
            headers[
                "cookie"] = '''cna=udetDhAG+kMCATrS6eojPUd7; thw=cn; miid=8500937081866481993; ali_ab=58.210.233.234.1472787076757.6; ali_apache_id=10.103.188.156.1474443514900.823590.3; hng=CN%7Czh-cn%7CCNY; _m_h5_tk=736c842806698c479e161d65e1efa01b_1479377404697; _m_h5_tk_enc=7ec44e68aca8041b678913a45edf8227; _m_user_unitinfo_=unit|unsz; _m_unitapi_v_=1478069694624; x=1973353526; uss=VvkmnyCLe7M81WS76%2FLI9wZjvmcxkxA5HWAqTi1cpzfZV00gZzJrvOGR4mA%3D; v=0; uc3=sg2=AiBidGoL%2FoFBQbTaaGEp6lDcR1Gii4LYDTDtQ9dTyv8%3D&nk2=F5QqboH0gOPanQ%3D%3D&id2=W8gzaQ7Xbn7H&vt3=F8dARHD6oZgMK0tB4gA%3D&lg2=VFC%2FuZ9ayeYq2g%3D%3D; existShop=MTQ3OTY5ODI3OA%3D%3D; lgc=tb_6442664; tracknick=tb_6442664; cookie2=1751b247bce3dc5a78c7fd373e1a5bcd; sg=40d; mt=np=&ci=2_1&cyk=1_1; cookie1=BvXjvOrzB6Hjv%2FqAVNk9ASMo8r4Tp1ahB0kuYAOyFTw%3D; unb=810537450; skt=bce85d267040a2cc; t=b1927f421039a5707bf1951a146a60f2; _cc_=VT5L2FSpdA%3D%3D; tg=0; _l_g_=Ug%3D%3D; _nk_=tb_6442664; cookie17=W8gzaQ7Xbn7H; _tb_token_=Tdiw6CS7FANn; linezing_session=kqmlEJhmavGxcaH9Opg7ABcT_1479698313770t3Go_2; uc1=cookie14=UoWwLQZnpEV8uQ%3D%3D&lng=zh_CN&cookie16=V32FPkk%2FxXMk5UvIbNtImtMfJQ%3D%3D&existShop=false&cookie21=W5iHLLyFe3xm&tag=3&cookie15=U%2BGCWk%2F75gdr5Q%3D%3D&pas=0; l=AlhY9GJ2CkT1pEWua0aMsZ7iqIzqd7zI; isg=AsPDNmCDnxjpA1zxL2UYJYOpUoc9lFd6FN2y0fWgKCKatOLWfQkmywomSPMA; ubn=p; ucn=unsz'''
            headers["referer"] = "https://detail.tmall.com/item.htm"
            headers[
                "user-agent"] = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36"
            request_param = {"url": c_url, "headers": headers, "data": ""}
            html_result = hd.get(request_param)
            pe = ProductInfoExtractor()
            result, promotion_list, product_promiselist = pe.extractor(html_result.get("result"))

        return result, promotion_list,product_promiselist


