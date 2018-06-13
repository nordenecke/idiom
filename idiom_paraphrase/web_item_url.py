# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 13:18:49 2018

@author: eqhuliu
"""

import requests

import re

import web_item_content

def parse_web_page(site_base_url,html_text):
    content_text=html_text
    pattern_item=re.compile("<ul.*?</ul>",re.DOTALL)
    if None==pattern_item.search(content_text):
        result_str=None
    else:
        result=pattern_item.search(content_text).group()
        pattern_link_url=re.compile('<.*?(href=".*?").*?')
        if []!=pattern_link_url.findall(result):
            result_str=""
            count=0
#            print(result)
            for i in pattern_link_url.findall(result):
#                print(i)
                url_l=i.strip('<a href=\"').strip('\">')
#                print(url_l)
                result_str+=url_l
                count+=1
                if count>=1:
                    break
                result_str+="\n"
        else:
            result_str=None
    if None!=result_str:
        result_str=site_base_url+result_str
    return result_str


def get_url_from_item(item):
    site_base_url='http://cy.babihu.com'
    site_query_url = site_base_url+'/edata/searchcy'
    data = {'w': item}
    session = requests.Session()
    session.get(site_query_url)
    response = session.post(site_query_url, data)
#    print(response.text)
    item_url=parse_web_page(site_base_url,response.text)
#    print(item_url)
    return item_url




def main():
    item_url=get_url_from_item(u'至死不渝')
    if None==item_url:
        print(u"Error in get item URL!")
    else:
        item_content_data=web_item_content.get_content_from_url(item_url)
    for i in item_content_data:
        print(i)        
#        print(item_content_data)

if __name__=="__main__":
    main()