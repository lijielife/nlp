# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import jieba
from os.path import dirname, abspath, join
import jieba.posseg as pseg
from jieba import enable_parallel
jieba.add_word('拖拉机学院')
jieba.add_word('手扶拖拉机专业')

# words = pseg.cut("我是拖拉机学院手扶拖拉机专业的。不用多久，我就会升职加薪，当上CEO，走上人生巅峰。")
# for wf in words:
#     w, f = wf
#     print wf.word, wf.flag
#     print w, f
#
# print('&' * 20)
from jieba import tokenize

unicode_sens = u'永和服装饰品有限公司永和服装饰品有限公司'
# result = tokenize(unicode_sens)
result = tokenize(unicode_sens)


for tk in result:
    print("word %s\t\t start: %d \t\t end:%d" % (tk[0],tk[1],tk[2]))

print ' '.join(jieba.cut(unicode_sens))
# dir_name = join(dirname(dirname(abspath(__file__))), 'tmp')
#
# from jieba.analyse import ChineseAnalyzer
# from whoosh.index import create_in, open_dir
# from whoosh.fields import *
# from whoosh.qparser import QueryParser
#
# analyzer = ChineseAnalyzer()
# schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT(stored=True, analyzer=analyzer))
#
# ix = create_in(dir_name, schema)
# writer = ix.writer()
#
# writer.add_document(
#     title="document1",
#     path="/a",
#     content="This is the first document we’ve added!"
# )
#
# writer.add_document(
#     title="document2",
#     path="/b",
#     content="The second one 你 中文测试中文 is even more interesting! 吃水果"
# )
#
# writer.add_document(
#     title="document3",
#     path="/c",
#     content="买水果然后来世博园。"
# )
#
# writer.add_document(
#     title="document4",
#     path="/c",
#     content="工信处女干事每月经过下属科室都要亲口交代24口交换机等技术性器件的安装工作"
# )
#
# writer.add_document(
#     title="document4",
#     path="/c",
#     content="咱俩交换一下吧。"
# )
#
# writer.commit()
#
# searcher = ix.searcher()
# parser = QueryParser('content', ix.schema)
#
# for keyword in ("水果世博园","你","first","中文","交换机","交换"):
#     print"result of:", keyword
#     q = parser.parse(keyword)
#     results = searcher.search(q)
#     for hit in results:
#         print(hit.highlights("content"))
#     print("="*10)

# for t in analyzer("我的好朋友是李明;我爱北京天安门;IBM和Microsoft; I have a dream. this is intetesting and interested me a lot"):
#     print(t.text)
