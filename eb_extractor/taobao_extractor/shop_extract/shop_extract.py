# -*- conding:utf8 -*-
from eb_extractor.extractor import Extractor
from bs4 import BeautifulSoup as bs
import json


class ShopExtract(Extractor):
    def __init__(self):
        pass

    def extractor(self, html_data):
        soup = bs(html_data.replace("\\", ""), "lxml")
        # print soup
        max_page = soup.select(".ui-page-s-len")[0].text.split("/")[1]
        # print max_page
        # product_elements = soup.select("div.item5line1 > .item ")
        product_elements = soup.select("div.item5line1 > .item ")
        if len(product_elements) == 0:
            print "item4line1"
            product_elements = soup.select("div.item4line1 > .item ")
        results = []
        for product_element in product_elements:
            result = dict()
            result["nid"] = product_element.attrs.get("data-id")
            img_element = product_element.select(".photo > a > img")

            if len(img_element) > 0:
                result["pic_url"] = img_element[0].attrs.get("data-ks-lazyload")
                result["raw_title"] = img_element[0].attrs.get("alt")
            product_info_element = product_element.select(".photo > a")[0]
            result["detail_url"] = product_info_element.attrs.get("href")
            gold_data = product_info_element.attrs.get("data-gold-data")
            details = product_element.select(".detail > .attribute")
            json_data = json.loads(gold_data)
            gokey_datas = json_data["gokey"].split("&")
            for gokey_data in gokey_datas:
                if "sellerid" in gokey_data:
                    result['user_id'] = gokey_data.split("=")[1]
            result["view_price"] = details[0].select(".cprice-area > .c-price")[0].text

            sale_num = details[0].select(".sale-area > .sale-num")
            if len(sale_num) !=0:
                result["total_sales"] = details[0].select(".sale-area > .sale-num")[0].text

            rates = product_element.select(".rates")
            if len(rates) == 0:
                # results.append(result)
                print 'rates  length 0'
                # continue
            else:
                for rate in rates:
                    comment = rate.select("span")[0].text
                    result["view_comment_count"] = comment[3:]
            results.append(result)
            print result
        print len(results)
        return results,max_page


    def extractorSx(self, html_data):
        soup = bs(html_data.replace("\\", ""))
        # return 'exception', 'exception'
        try:
            max_page = soup.select(".ui-page-s-len")[0].text.split("/")[1]
        except Exception, e:
            return 'exception','exception'

        jtItems = soup.select("div.J_TItems > div ")
        results = []
        if len(jtItems) > 0:
            for items in jtItems:
                classname = items.attrs.get("class")[0]
                # for classname in classname_all:
                if 'item' in classname:
                    # print 11
                    product_elements = items.select(".item")
                    for product_element in product_elements:
                        result = dict()
                        result["nid"] = product_element.attrs.get("data-id")
                        img_element = product_element.select(".photo > a > img")

                        if len(img_element) > 0:
                            result["pic_url"] = img_element[0].attrs.get("data-ks-lazyload")
                            result["raw_title"] = img_element[0].attrs.get("alt")
                        product_info_element = product_element.select(".photo > a")[0]
                        result["detail_url"] = product_info_element.attrs.get("href")
                        gold_data = product_info_element.attrs.get("data-gold-data")
                        details = product_element.select(".detail > .attribute")
                        json_data = json.loads(gold_data)
                        gokey_datas = json_data["gokey"].split("&")
                        for gokey_data in gokey_datas:
                            if "sellerid" in gokey_data:
                                result['user_id'] = gokey_data.split("=")[1]
                        result["view_price"] = details[0].select(".cprice-area > .c-price")[0].text

                        sale_num = details[0].select(".sale-area > .sale-num")
                        if len(sale_num) != 0:
                            result["total_sales"] = details[0].select(".sale-area > .sale-num")[0].text

                        rates = product_element.select(".rates")
                        if len(rates) > 0:
                            for rate in rates:
                                comment = rate.select("span")[0].text
                                result["view_comment_count"] = comment[3:]
                        else:
                            result["view_comment_count"] = -1
                        results.append(result)
                        # print result
                else:
                    break
                    # print len(results)
                    # return results, max_page
        print len(results)
        if len(results) > 48:
            print
            print results
        return results, max_page


def main():
    from webutil.html_downloader import HTMLLocalDownloader
    # api_url = '''https://lkdq.tmall.com/i/asynSearch.htm?_ksTS=1480322057878_363&callback=jsonp364&mid=w-14784681269-0&wid=14784681269&path=/search.htm&&search=y&spm=a1z10.1-b-s.w11311120-14784681109.2.6yZkUF&scene=taobao_shop'''

    # api_url = '''https://xiaogouwd.tmall.com/i/asynSearch.htm?&callback=jsonp433&mid=w-14641566554-0&wid=14641566554&path=/search.htm&&search=y&scene=taobao_shop&pageNo=1&tsearch=y'''
    api_url = '''https://xiaogouds.tmall.com/i/asynSearch.htm?&callback=jsonp433&mid=w-14664434829-0&wid=14664434829&path=/search.htm&&search=y&scene=taobao_shop&pageNo=1&tsearch=y'''

    hd = HTMLLocalDownloader()
    headers = dict()
    headers["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36"
    headers["cookie"] = "cna=vZGpEDf7mCECATrS6eo2Bd6o; sm4=320500; uss=WvZkvF55EFfHkeM6lE8wp0VWdO8sADi9M8F8%2BsXbypjeWUGwWz%2FoZQw7X0Y%3D; _tb_token_=f71d934085bfb; uc3=nk2=FK4slm2XNQ%3D%3D&id2=UoH623lKljltaQ%3D%3D&vt3=F8dARHDxtHCi%2F0mz4Pc%3D&lg2=URm48syIIVrSKA%3D%3D; lgc=w724228; tracknick=w724228; cookie2=1c532ced424d37ea30638361c404f8b9; skt=6c9a4f546a57eb69; t=e4f96743e5b797e0b954e021a4f1087f; _uab_collina=148050412279664330366762; _umdata=6AF5B463492A874DF0C7991DD4476942F218176BC42BE0A90AC2A92A6983762181B6870DB7E025121759E2E8D0A1B55A44B5836D4FAD66CB62E203CD504A01EB59F9C843DBA5F6FC60161759EAD7C38BEA801ABA338C2A67CC3490BA2409EAB2; pnm_cku822=; cq=ccp%3D1; l=AqKiE6kArk1jAG8uYAcmuhRYciIELKYN; isg=AnJyqY1AfrI8AEKTotfiiiJgw7iYEXadjQgWbTxLQSUQzxDJJZUOrOlnydwI"
    headers[
        "referer"] = "https://lkdq.tmall.com/search.htm?spm=a1z10.1-b-s.w11311120-14784681109.2.6yZkUF&scene=taobao_shop"
    request_param = {"url": api_url, "headers": headers, "data": ""}
    response = hd.get(request_param)
    se = ShopExtract()
    a,b = se.extractorSx(response["result"])
    if 'exception' in a:
        print 11
    print a
    print b

if __name__ == '__main__':
    main()
