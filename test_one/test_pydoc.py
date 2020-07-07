from docx import Document
import requests
from bs4 import BeautifulSoup as bs

#url = 'https://www.jianshu.com/p/ea6f7fb69501'
#res = requests.get(url)
#res.encoding = 'utf-8'
#print(res.text)

doc = Document()
paragraph = doc.add_paragraph('    中国，你好！\n anih')
doc.save('E:\\DannyWu\\Desktop\\de.docx')
