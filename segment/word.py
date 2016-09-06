# -*- coding: utf-8 -*-
from os.path import dirname, abspath, join
import jieba
from jieba.analyse import extract_tags, set_idf_path, set_stop_words, default_tfidf, textrank

userdict_path = join(dirname(dirname(abspath(__file__))), 'libwords', 'dict.txt')
idf_path = join(dirname(dirname(abspath(__file__))), 'libwords', 'idf.txt.big')
stop_words_path = join(dirname(dirname(abspath(__file__))), 'libwords', 'stop_words.txt')

# jieba.load_userdict(userdict_path)
# jieba.add_word('石墨烯')
# jieba.add_word('凱特琳')

# sen = '我来到北.京清华大学'
# sen = '他来到了网易杭研大厦'
# sen = '小明硕士毕业于中国科学院计算所，后在日本京都大学深造'
# sen = '李小福是创新办主任也是云计算方面的专家,石墨烯凱特琳'
# sen = '如果放到post中将出错。'
# sen = '「台中」正确应该不会被切开'
# print('/'.join(jieba.cut(sen)))
# print('/'.join(jieba.cut(sen, HMM=False)))
#
# jieba.add_word('台中')
# # print jieba.suggest_freq('台中', tune=True)
# print('/'.join(jieba.cut(sen)))
# print('/'.join(jieba.cut(sen, HMM=False)))

jieba.add_word('拖拉机学院')
jieba.add_word('手扶拖拉机专业')

sens = '我是拖拉机学院手扶拖拉机专业的。不用多久，我就会升职加薪，当上CEO，走上人生巅峰。'
tags = extract_tags(sens, withWeight=True, topK=20, allowPOS=())

for word, weight in tags:
    print word, weight

# print '#' * 10
# # set_stop_words(stop_words_path)
# set_idf_path(idf_path)
# print default_tfidf.median_idf
#
# extract_tags(sens, topK=5, withWeight=True)
#
# for word, weight in tags:
#     print word, weight
#
# print('*' * 20)
# for w, i in textrank(sens, topK=5, withWeight=True):
#     print w, i


