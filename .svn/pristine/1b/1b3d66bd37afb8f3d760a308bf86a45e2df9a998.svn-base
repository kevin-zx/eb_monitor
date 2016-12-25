# -*- coding: utf-8 -*-
import jieba

seg_list = jieba.cut(u"吸尘器家用 手持式",cut_all=True)
print "Full Mode:", "/ ".join(seg_list) #全模式
#
seg_list = jieba.cut(u"小狗除螨仪大吸力紫外线杀菌净化螨虫吸尘器家用床上除螨器d-609",cut_all=False)
print "Default Mode:", "/ ".join(seg_list) #精确模式
#
# seg_list = jieba.cut(u"他来到了网易杭研大厦") #默认是精确模式
# print ", ".join(seg_list)
#
seg_list = jieba.cut_for_search(u"小明硕士毕业于中国科学院计算所，后在日本京都大学深造") #搜索引擎模式
print ", ".join(seg_list)