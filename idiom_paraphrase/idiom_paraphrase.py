# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 11:48:59 2017

@author: norden
"""

import idiom_list
import web_item_url
import web_item_content

input_idiom_list_file=r"idioms.txt"
output_docx_file=r"idiom_set.docx"
idiom_content_list=[]
def idiomcard_generator():
    il=idiom_list.get_idiom_list(input_idiom_list_file)
#    print(il)
    for item in il:
        print(item)
        item_url=web_item_url.get_url_from_item(item)
        if None==item_url:
            print(u"Error in get item URL!")
            str_not_found='[ '+item+' ]: '+ u'寻他于百度， 不见！'
            item_exception=[]
            item_exception.append(str_not_found)
            idiom_content_list.append(item_exception)
        else:
            item_content_data=web_item_content.get_content_from_url(item_url)
            idiom_content_list.append(item_content_data)
        for i in item_content_data:
            print(i)                
#        print(idiom_content)
#        print(idiom_content.idiom)
#        print(idiom_content.phonetic_symbol)
#        print(idiom_content.paraphrase)
#    print(idiom_content_list)
#    for i in idiom_content_list:
#        print(i.idiom)
#        print(i.phonetic_symbol)
#        print(i.paraphrase)
#format/output
    idiom_list.put_docx(output_docx_file,idiom_content_list)

def main():
    idiomcard_generator()

if __name__=="__main__":
    main()
