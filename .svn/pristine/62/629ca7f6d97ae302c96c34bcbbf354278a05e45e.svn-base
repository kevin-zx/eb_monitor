# -*- coding:utf8 -*-
from eb_extractor.extractor import Extractor
import json


class CommentExtractor(Extractor):
    def extractor(self, html_data):
        jsonstr = self.get_jsonstr_from_html(html_data)
        json_data = json.loads(jsonstr)
        return json_data["count"]


def main():
    str1 = '''jsonp100({"count": 2640})'''
    r_extractor = CommentExtractor()
    print type(r_extractor.extractor(str1))

if __name__ == '__main__':
    main()
