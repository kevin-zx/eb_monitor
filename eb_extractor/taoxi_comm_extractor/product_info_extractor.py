# -*- coding:utf8 -*-
from webutil.html_downloader import HTMLLocalDownloader
from eb_extractor.extractor import Extractor
import json


# https://mdskip.taobao.com/core/initItemDetail.htm?progressiveSupport=true&itemId=43417684104&areaId=330100&tmallBuySupport=true&queryMemberRight=true&callback=setMdskip


class ProductInfoExtractor(Extractor):
    def extractor(self, html_data, needmap={}):
        """

        :param html_data:
        :param needmap:
        :return:
        """
        # print html_data
        result = dict()
        try:
            jsonstr = self.get_jsonstr_from_html(html_data)
        except Exception ,e:
            return 'exception','exception','exception'

        jsondata = json.loads(jsonstr)
        if jsondata.get("success") is not None and not jsondata.get("success"):
            result["start_time"] = -1
            return result,[],''
        result["start_time"] = jsondata["defaultModel"]["tradeResult"]["startTime"]
        sell_count_do = jsondata["defaultModel"].get("sellCountDO",0)
        if sell_count_do != 0:
            try:
                result["month_sales"] = sell_count_do.get("sellCount",-1)
            except Exception, e:
                print e
        else:
            result["month_sales"] = -1
        progressive_info_do = jsondata["defaultModel"].get("progressiveInfoDO",0)
        if progressive_info_do != 0:
            resx = progressive_info_do.get("text")
            # print type(resx)
            if resx is None:
                result["repayment"] = 0
            else:
                repayment = resx[7:8]
                result["repayment"] = repayment
        else:
            result["repayment"] = 0

        delivery_do_list = jsondata["defaultModel"].get("deliveryDO",{"deliverySkuMap":""})["deliverySkuMap"]
        if len(delivery_do_list) > 0:
            key_delivery = delivery_do_list.keys()[0]
            money = delivery_do_list[key_delivery][0].get("money",-1)
            if money == -1:
                result["view_fee"] = '0.00'
            else:
                result["view_fee"] = money
        else:
            result["view_fee"] = '0.00'

        sku_list = jsondata["defaultModel"]["itemPriceResultDO"]["priceInfo"]
        key = ""
        promotion_list = []
        if len(sku_list) > 0:
            key = sku_list.keys()[0]
        if key != "":
            sku = sku_list[key]
            promotion_raw_list = sku.get("promotionList",[])
            for promotion in promotion_raw_list:
                # print promotion
                prom = dict()
                prom["prom_type"] = promotion["promType"]
                prom["prom_type_name"] = promotion["type"]
                prom["end_time"] = promotion.get("endTime", 0)
                prom["start_time"] = promotion.get("startTime", 0)
                #get  不到 默认为0
                prom["price"] = promotion.get("price", 0)
                promotion_list.append(prom)

        # servicePromise
        product_promiselist = []
        service_promise_list = jsondata["defaultModel"]["servicePromise"]["servicePromiseList"]
        if len(service_promise_list) > 0:
            for servicePromise in service_promise_list:
                product = dict()
                product["descripTion"] = servicePromise.get("description",'')
                product["displayText"] = servicePromise.get("displayText", '')
                # print servicePromise.get("description",'')
                product_promiselist.append(product)
        # print len(product_promiselist)
        return result, promotion_list, product_promiselist


def main():
    url = '''https://mdskip.taobao.com/core/initItemDetail.htm?progressiveSupport=true&itemId=20123030100&areaId=330100&tmallBuySupport=true&queryMemberRight=true&callback=setMdskip'''
    hd = HTMLLocalDownloader()
    headers = dict()
    headers["cookie"] = ""
    headers["referer"] = "https://detail.tmall.com/item.htm"
    headers[
        "user-agent"] = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36"
    request_param = {"url": url, "headers": headers, "data": ""}
    html = hd.get(request_param)["result"]
    print html

    ProductInfoExtractor().extractor(html)


if __name__ == '__main__':
    main()
