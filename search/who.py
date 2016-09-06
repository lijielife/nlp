# -*- coding: utf-8 -*-
from os.path import dirname, join, abspath
from whoosh.index import create_in
from whoosh.fields import *

dir_path = join(dirname(abspath(__file__)), 'indexer')

schema = Schema(t=TEXT(stored=True), path=ID(stored=True), c=TEXT())
index = create_in(dir_path, schema)
writer = index.writer()

writer.add_document(
    t='1 doc',
    path='111/',
    c='你大爷， 不想活了吗？'
)

writer.add_document(
    t='2 doc',
    path='222/',
    c='是的， 不想活了！'
)

