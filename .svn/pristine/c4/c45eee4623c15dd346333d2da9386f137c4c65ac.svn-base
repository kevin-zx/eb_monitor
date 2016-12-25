# -*- coding:utf8 -*-
import urllib
import time
from webutil.html_downloader import HTMLLocalDownloader
# from eb_extractor.taobao_extractor.list_extract.list_extractor import TbListExtractor

from eb_extractor.taobao_extractor.shop_extract.shop_extract import ShopExtract

def get(shop_url, page ,user_id):
    urls = get_url(shop_url, page ,user_id)
    # print urls
    results = []
    for url in urls:
        headers = dict()
        headers["cookie"] = "cna=vZGpEDf7mCECATrS6eo2Bd6o; sm4=320500; uss=WvZkvF55EFfHkeM6lE8wp0VWdO8sADi9M8F8%2BsXbypjeWUGwWz%2FoZQw7X0Y%3D; _tb_token_=f71d934085bfb; uc3=nk2=FK4slm2XNQ%3D%3D&id2=UoH623lKljltaQ%3D%3D&vt3=F8dARHDxtHCi%2F0mz4Pc%3D&lg2=URm48syIIVrSKA%3D%3D; lgc=w724228; tracknick=w724228; cookie2=1c532ced424d37ea30638361c404f8b9; skt=6c9a4f546a57eb69; t=e4f96743e5b797e0b954e021a4f1087f; _uab_collina=148050412279664330366762; _umdata=6AF5B463492A874DF0C7991DD4476942F218176BC42BE0A90AC2A92A6983762181B6870DB7E025121759E2E8D0A1B55A44B5836D4FAD66CB62E203CD504A01EB59F9C843DBA5F6FC60161759EAD7C38BEA801ABA338C2A67CC3490BA2409EAB2; pnm_cku822=; cq=ccp%3D1; l=AqKiE6kArk1jAG8uYAcmuhRYciIELKYN; isg=AnJyqY1AfrI8AEKTotfiiiJgw7iYEXadjQgWbTxLQSUQzxDJJZUOrOlnydwI"
        headers["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36"
        request_param = {"url": url, "headers": headers, "data": ""}
        html = HTMLLocalDownloader().get(request_param=request_param)
        le = ShopExtract()
        rs,maxPage = le.extractorSx(html["result"])

        while 'exception' in rs:
            headers = dict()
            headers[
                "cookie"] = "cna=vZGpEDf7mCECATrS6eo2Bd6o; sm4=320500; uss=WvZkvF55EFfHkeM6lE8wp0VWdO8sADi9M8F8%2BsXbypjeWUGwWz%2FoZQw7X0Y%3D; _tb_token_=f71d934085bfb; uc3=nk2=FK4slm2XNQ%3D%3D&id2=UoH623lKljltaQ%3D%3D&vt3=F8dARHDxtHCi%2F0mz4Pc%3D&lg2=URm48syIIVrSKA%3D%3D; lgc=w724228; tracknick=w724228; cookie2=1c532ced424d37ea30638361c404f8b9; skt=6c9a4f546a57eb69; t=e4f96743e5b797e0b954e021a4f1087f; _uab_collina=148050412279664330366762; _umdata=6AF5B463492A874DF0C7991DD4476942F218176BC42BE0A90AC2A92A6983762181B6870DB7E025121759E2E8D0A1B55A44B5836D4FAD66CB62E203CD504A01EB59F9C843DBA5F6FC60161759EAD7C38BEA801ABA338C2A67CC3490BA2409EAB2; pnm_cku822=; cq=ccp%3D1; l=AqKiE6kArk1jAG8uYAcmuhRYciIELKYN; isg=AnJyqY1AfrI8AEKTotfiiiJgw7iYEXadjQgWbTxLQSUQzxDJJZUOrOlnydwI"
            headers[
                "user-agent"] = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36"
            request_param = {"url": url, "headers": headers, "data": ""}
            html = HTMLLocalDownloader().get(request_param=request_param)
            le = ShopExtract()
            rs, maxPage = le.extractorSx(html["result"])

        results.extend(rs)
        if page == 1 and len(rs) != 35:
            break
    for i in range(0, len(results)):
        if page == 1:
            results[i]["rank"] = i
        else:
            results[i]["rank"] = (page - 2) * 41 + 47 + i
        # print results[i]
    return results,maxPage


def get_url(shop_url, page,user_id):
    # print shop_url+"...bbb"
    urls = []
    # unix_time = str(int(time.time() * 1000))
    # data_value = (page - 1) * 44
    # ss = (page - 2) * 44
    # shop_url = urllib.quote(shop_url)
    # apiurl = ""
    mid = "w-{0}-0".format(user_id)
    apiurl = "{0}i/asynSearch.htm?&callback=jsonp433&mid={1}&wid={2}&path=/search.htm&&search=y&scene=taobao_shop&pageNo={3}&tsearch=y".format(shop_url,mid,user_id,page)

    # print apiurl
    # https: // xiaogouds.tmall.com / i / asynSearch.htm?_ksTS = 1480474960091
    # _193 & callback = jsonp194 & mid = w - 14664434829 - 0 & wid = 14664434829 & path = / search.htm & & search = y & spm = a1z10
    # .3 - b - s.w5001 - 14664434815.4.ISN84w & scene = taobao_shop

    # if ss < 0:
    #     ss = 0
    #     apiurl = "https://s.taobao.com/api?_ksTS={0}_302&callback=jsonp303&ajax=true&m=customized&rn=e54827016f39420ab98dbbaae15edf95&q={1}&imgfile=&js=1&style=grid&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20161116&ie=utf8&s=36&bcoffset=-1".format(
    #         unix_time, keyword)
    # products_url = '''https://s.taobao.com/search?data-key=s&data-value={0}&ajax=true&_ksTS={1}_1181&callback=jsonp1182&q={2}&imgfile=&js=1&style=grid&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20161116&ie=utf8&bcoffset=0&ntoffset=6&p4ppushleft=1%2C48&s={3}''' \
    #     .format(data_value, unix_time, keyword, ss)
    # urls.append(products_url)
    if apiurl != "":
        urls.append(apiurl)
    return urls


def main():
    print len(get("牛仔裤", 1))


if __name__ == '__main__':
    main()
