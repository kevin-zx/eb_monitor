# -*- coding: utf-8 -*-
from store.store_mysql import StoreMysql
from spider import config


class SubGroup:
    def __init__(self, keyword, main_word, sub_key=None):
        self.keyword = keyword
        self.main_word = main_word
        self.groups = []
        if sub_key is not None:
            self.append(sub_key)
        self.total_score = 0
        pass

    def append(self, sub_key):
        for group in self.groups:
            if group.is_belong_this_group(sub_key):
                group.append(sub_key)
                return
        self.groups.append(Group(sub_key))

    def set_score(self):
        for group in self.groups:
            if group.group_is_in_keyword(self.main_word):
                group.score = 5.0/4.0
                self.total_score += 5.0/4.0
            elif group.group_is_in_keyword(self.keyword):
                self.total_score += 5.0
            else:
                group.score = 5.0 / 3.0
                self.total_score += 5.0/3.0
        for group in self.groups:
            group.score = (group.score/self.total_score)
            group.set_score_and_store(self.keyword)


class Group:
    def __init__(self, sub_key):
        self.st = StoreMysql(**config.TAOBAO_DB)
        self.score = 5.0
        self.sub_keys = []
        self.total_len = 0.0
        self.append(sub_key)

    def append(self, sub_key):
        keylen = float(len(sub_key))
        self.total_len += keylen
        self.sub_keys.append({"sub_key": sub_key, "score": 0.0, "len": keylen})

    def is_belong_this_group(self, other_sub_key):
        for sub_key in self.sub_keys:
            if sub_key["sub_key"] in other_sub_key or other_sub_key in sub_key["sub_key"]:
                return True
        return False

    def group_is_in_keyword(self, keyword):
        for sub_key in self.sub_keys:
            if sub_key["sub_key"] in keyword:
                return True
        return False

    def set_score_and_store(self, keyword):
        for sub_key in self.sub_keys:
            # print (sub_key["len"]/self.total_len)*self.score
            # print sub_key["sub_key"]
            self.st.do("update keyword_match_info_score set score = {0} WHERE keyword = '{1}' and sub_keyword = '{2}'".format((sub_key["len"]/self.total_len)*self.score, keyword, sub_key["sub_key"]))
            # print "update keyword_match_info_score set score = {0} WHERE keyword = '{1}' and sub_keyword = '{2}'".format((sub_key["len"]/self.total_len)*self.score, keyword, sub_key["sub_key"])
