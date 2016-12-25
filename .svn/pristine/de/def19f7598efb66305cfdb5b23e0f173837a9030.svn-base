## -*- coding:utf8 -*-
import json
from eb_extractor.extractor import Extractor


class TbMListExtractor(Extractor):
    def __init__(self):
        pass

    def extractor(self, html_data):
        jsonstr = self.get_jsonstr_from_html(html_data)
        # print jsonstr
        jsondata = json.loads(jsonstr)
        # if()
        results = []
        productItems = jsondata.get("listItem")
        if productItems is None:
            return results

        for productItem in productItems:
            result = dict()
            # print productItem["isP4p"]
            if productItem["isP4p"] == "true":
                continue
            result["view_sales"] = productItem["act"]
            result["item_loc"] = productItem['area']
            result["view_fee"] = productItem["fastPostFee"]
            result["is_tmall"] = productItem["isB2c"]

            result["nid"] = productItem["item_id"]
            result["raw_title"] = productItem["name"]
            result["nick"] = productItem["nick"]
            result["reserve_price"] = productItem['originalPrice']
            result['detail_url'] = productItem['url']
            result["view_price"] = productItem["price"]
            result["user_id"] = productItem["userId"]
            result["category"] = productItem["category"]
            result["comment_count"] = productItem["commentCount"]
            results.append(result)
        return results



