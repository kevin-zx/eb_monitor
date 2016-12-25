# -*- coding:utf8 -*-
from eb_extractor.extractor import Extractor
import json


class DsrAndCollectionExtractor(Extractor):
    def extractor(self, html_data):
        # print html_data
        html_data = str(html_data)
        html_data = str.replace(html_data, "{v:", "{\"v\":")
        html_data = str.replace(html_data, "nv:", "\"nv\":")
        html_data = str.replace(html_data, ",m:", ",\"m\":")
        html_data = str.replace(html_data, "m_g:", "\"m_g\":")
        html_data = str.replace(html_data, "s_UFB:", "\"s_UFB\":")
        html_data = str.replace(html_data, "m_UFB:", "\"m_UFB\":")
        html_data = str.replace(html_data, ",s:", ",\"s\":")
        html_data = str.replace(html_data, "s_g:", "\"s_g\":")
        html_data = str.replace(html_data, "c_UFB:", "\"c_UFB\":")
        html_data = str.replace(html_data, ",c:", ",\"c\":")
        html_data = str.replace(html_data, "c_g:", "\"c_g\":")
        html_data = str.replace(html_data, "gp:", "\"gp\":")
        html_data = str.replace(html_data, "ss:", "\"ss\":")
        html_data = str.replace(html_data, "hdr:", "\"hdr\":")
        jsonstr = self.get_jsonstr_from_html(html_data)
        jsondata = json.loads(jsonstr)
        result = dict()
        keyset = jsondata.keys()
        for key in keyset:
            if "ICCP" in key:
                result["collect_count"] = jsondata[key]
            if "dsr" in key:
                dsr_info = jsondata[key]

        # result["comment_count"] = jsondata[jsondata.keys()[0]];
        # dsr_info = jsondata[jsondata.keys()[1]]

        if (dsr_info == 0):
            result["collect_count"] = -1
            return result
        result["v"] = dsr_info["v"]
        result["nv"] = dsr_info["nv"]
        result["description_score"] = dsr_info["m"]
        result["description_score_de"] = dsr_info["m_g"]
        result["service_score_lv"] = dsr_info["s_UFB"]
        result["description_score_lv"] = dsr_info["m_UFB"]
        result["service_score"] = dsr_info["s"]
        result["service_score_de"] = dsr_info["s_g"]
        result["delivery_score_lv"] = dsr_info["c_UFB"]
        result["delivery_score"] = dsr_info["c"]
        result["delivery_score_de"] = dsr_info["c_g"]
        result["gp"] = dsr_info["gp"]
        result["ss"] = dsr_info["ss"]
        result["hdr"] = dsr_info["hdr"]

        return result


def main():
    str1 = '''jsonp218({"ICCP_1_21821291261":41507,"SM_368_dsr-681185851":{v:0,nv:100,m_UFB:0,m:4.88467,m_g:14.04,s_UFB:0,s:4.83337,s_g:5.93,c_UFB:0,c:4.82096,c_g:8.68,gp:100.00,ss:5237789,hdr:true}});'''
    r_extractor = DsrAndCollectionExtractor()
    print r_extractor.extractor(str1)

if __name__ == '__main__':
    main()
