# -*- coding: utf-8 -*-
# @Desc     :
# @license : Copyright(C), CBR
# @Contact : shiliang@chinaratings.com.cn
# @Site    :
import urllib


def read_text():
    quotes = open("movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    check_profanity(contents_of_file)
    quotes.close()


def check_profanity(contents_of_file):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + contents_of_file)
    result = connection.read()
    print ('\n'+result)
    connection.close()
    if "true" in result:
        print ("\n Profanity Alert")
    elif "false" in result:
        print ("\n This document has no curse words")
    else:
        print ("\n Could not scan the document properly")


read_text()