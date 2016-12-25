# -*- coding:utf8 -*-
import json
from eb_extractor.extractor import Extractor
from webutil.html_downloader import HTMLLocalDownloader
import traceback

class TbListExtractor(Extractor):
    def __init__(self):
        super(TbListExtractor, self).__init__()

    def extractor_spu(self, html_data):
        pass

    def extractor(self, html_data):
        # print html_data
        results = []
        try:
            jsonstr = self.get_jsonstr_from_html(html_data)
        except Exception:
            # traceback.print_exc()
            return results

        if "API.CustomizedApi" in jsonstr:
            jsonstr = str.replace(str(jsonstr), "API.CustomizedApi", "items")
            json_data = json.loads(jsonstr)["items"]["itemlist"]["auctions"]
        elif "spulist" in jsonstr:
            return results
        elif "redirect" in jsonstr:
            return results
        else:
            if json.loads(jsonstr)["mods"]["itemlist"].get("data") is None:
                return results

            json_data = json.loads(jsonstr)["mods"]["itemlist"]["data"]["auctions"]
        for productItem in json_data:
            result = dict()
            if productItem['category'] == "":
                # print "continue"
                continue
            result['category'] = productItem['category']
            result['comment_count'] = productItem['comment_count']
            result['detail_url'] = productItem['detail_url']
            result['item_loc'] = productItem['item_loc']
            result['nick'] = productItem['nick']
            result['nid'] = productItem['nid']
            result['raw_title'] = productItem["raw_title"]
            # result['nid'] = productItem["nid"]
            result['reserve_price'] = productItem['reserve_price']
            result['risk'] = productItem['risk']

            result['delivery_score'] = productItem['shopcard']["delivery"][0]
            result['delivery_score_lv'] = productItem['shopcard']["delivery"][1]
            result['delivery_score_de'] = productItem['shopcard']["delivery"][2]

            result['description_score'] = productItem['shopcard']["description"][0]
            result['description_score_lv'] = productItem['shopcard']["description"][1]
            result['description_score_de'] = productItem['shopcard']["description"][2]

            result['service_score'] = productItem['shopcard']["service"][0]
            result['service_score_lv'] = productItem['shopcard']["service"][1]
            result['service_score_de'] = productItem['shopcard']["service"][2]
            # print productItem['shopcard']["isTmall"]
            if productItem['shopcard']["isTmall"]:
                result["is_tmall"] =1
            else:
                result["is_tmall"] = 0
            result["red_word"] = self.get_red_word(productItem["title"])
            result['user_id'] = productItem['user_id']

            result['view_fee'] = productItem['view_fee']
            result['view_price'] = productItem['view_price']
            result['view_sales'] = str.replace(str(productItem['view_sales']), "人付款", "")
            results.append(result)
        return results


def main():
    hd = HTMLLocalDownloader()
    url = "https://s.taobao.com/search?data-key=s&data-value=0&ajax=true&_ksTS=1479622818620_1819&callback=jsonp1820&q=adfa&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20161120&ie=utf8&bcoffset=4&p4ppushleft=1%2C48&ntoffset=4&s=10"
    headers = dict()
    headers["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36"
    request_param = {"url": url, "headers": headers, "data": ""}
    response = hd.get(request_param)
    print TbListExtractor().extractor(response["result"])
    pass

if __name__ == '__main__':
    main()
    # pass

