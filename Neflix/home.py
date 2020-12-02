#!C:\Python\python.exe
#-*- coding: utf-8 -*-
# import sys
# # import codecs
# # sys.stdout = codecs.getwriter("iso-8859-1")(sys.stdout, 'xmlcharrefreplace')
# if sys.stdout.encoding != 'cp850':
#       sys.stdout = codecs.getwriter('cp850')(sys.stdout.buffer, 'strict')
# if sys.stderr.encoding != 'cp850':
#   sys.stderr = codecs.getwriter('cp850')(sys.stderr.buffer, 'strict')
# #chcp 65001
# #print(data.decode('utf-8').encode('cp850','replace').decode('cp850'))

print("Content-type: text/html\n\n")

import view

html=view.head() + view.home() + view.footer()

print(html)