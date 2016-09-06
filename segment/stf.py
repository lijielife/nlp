# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from nltk.tokenize.stanford_segmenter import StanfordSegmenter

seg = StanfordSegmenter(
    path_to_jar=r'D:\temp\stanford\stanford-segmenter.jar',
    path_to_slf4j=r'D:\temp\stanford\slf4j-api.jar',
    path_to_sihan_corpora_dict=r'D:\temp\stanford\data',
    path_to_model=r'D:\temp\stanford\data\ctb.gz',
    path_to_dict=r'D:\temp\stanford\data\dict-chris6.ser.gz',
)

# sentence = "这是斯坦福中文分词器测试"
sentence = "操你大爷，狗日的"
res = seg.segment(sentence)
print res

# import jieba
# ss = jieba.cut(sentence)
# print ' '.join(list(ss)), type(ss)

