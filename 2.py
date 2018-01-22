#html文档
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
#导入bs4
from bs4 import BeautifulSoup
#做一个美味汤
soup = BeautifulSoup(html_doc,'html.parser')
#输出结果
#print(soup.prettify())
#输出文档中的对应标签中的内容
#print(soup.find_all(id='link1'))


#从文档中找到所有<a>标签的链接:  使用的是for循环
#发现了没有，find_all方法返回的是一个可以迭代的列表
for link in soup.find_all('a'):
    print(link.get('href'))

print(soup.get_text)














