from bs4 import BeautifulSoup

html = '''<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html;charset=utf-8">
        <title>DannyWu Blog</title>
    </head>
    <body>
        <div class="content">
            <h1 id="title">VPN</h1>
            <p>你好</p>
            <p>vpn</p>
        </div>
    </body>
</html>'''

soup = BeautifulSoup(html,'lxml')
print(soup.select('p').text)
#print(soup.prettify())
