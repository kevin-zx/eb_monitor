# -*- coding:utf8 -*-
import re
# import sys
import sys
reload(sys)
sys.setdefaultencoding('utf8')


class Extractor(object):
    def __init__(self):
        pass

    def extractor(self, html_data):
        """
        :param html_data:
        :return:
        """
        return []

    @staticmethod
    def get_jsonstr_from_html(html):
        """
        :param html:
        :return: json str
        """
        so = re.search(r"\{.+\}", html)
        # if so is None:
        #     return None
        return so.group(0)

    @staticmethod
    def get_red_word(title):
        complie_object = re.compile("H>.+?<")
        red_word_part = complie_object.findall(title)
        for i in range(0, len(red_word_part)):
            red_word_part[i] = str.replace(str(red_word_part[i]), "H>", "")
            red_word_part[i] = str.replace(red_word_part[i], "<", "")
        subsquen = "&"
        return subsquen.join(red_word_part)


def main():
    ex = Extractor()
    bs = ex.get_red_word("小狗超静音小型强力除螨仪大吸力大功率无耗材机D-9005")
    # for b in bs:
    #     print b
    str1 = "&"
    print str1.join(bs)

if __name__ == '__main__':
    main()
