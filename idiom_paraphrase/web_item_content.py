# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 13:19:40 2018

@author: eqhuliu
"""
import requests

import re

def parse_item_content_from_web_page(html_text):
    pattern_item=re.compile("<div class=\"msg_con\".*?<p class=\"pline\"",re.DOTALL)

#    print("error idiom:%s" %idiom)
    if None==pattern_item.search(html_text):
        print("idiom not found!")
        return None
    else:
        result=pattern_item.search(html_text).group()
#        print(result)
        pattern_item_p=re.compile('<p>.*?</p>')
        paraphrase_list=[]
        for j in pattern_item_p.findall(result):
            paraphrase_list.append(j.strip('<p>').strip('</p>'))
#            print(j.strip('<p>').strip('</p>'))
        return paraphrase_list

def get_content_from_url(url):
    session = requests.Session()
    response=session.get(url)
    paraphrase_list=parse_item_content_from_web_page(response.text)
#    for i in paraphrase_list:
#        print(i)
    return paraphrase_list
