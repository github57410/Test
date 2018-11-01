# -*- coding:utf-8 -*-
# Author:Gao Shuai
from urllib import request
from bs4 import BeautifulSoup
if __name__ == "__main__":
    response = request.urlopen("http://baodu.com")
    html = response.read()
    html = html.decode("utf-8")#简单的decode()命令将网页的信息进行解码，并显示出来
    print(html)
# with open('url1.txt','w') as a:
#     a.write(text)