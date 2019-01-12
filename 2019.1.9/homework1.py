"""
__title__ = ''
__author__ = 'Thompson'
__mtime__ = '2018/9/25'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃███━███ ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃     ┃ 
                ┃     ┃ 
                ┃     ┃ 
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
from urllib import request
from urllib import parse
from lxml import etree
import chardet

url="http://www.renren.com/969396513"
head = {}
head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
head['Cookie'] = 'anonymid=jqozso0m-b50nve; depovince=HEN; _r01_=1; JSESSIONID=abcZKiFiZbSV3cKRY_XGw; ick_login=ba62a23a-4147-40c0-9a96-2b9f79d99832; t=1c6614f12d6587e45a66ad708425bd393; societyguester=1c6614f12d6587e45a66ad708425bd393; id=969396513; xnsid=ce04ac7a; ver=7.0; loginfrom=null; jebe_key=3dd574dc-026c-46e7-adb4-96cc721864c7%7C5db5c239b773c27b9510fed6af26a538%7C1547026787661%7C1%7C1547026787501; wp_fold=0; jebecookies=63e38085-5ef5-4b3d-9037-0f9eb857299c|||||'

req = request.Request(url,headers=head)
response = request.urlopen(req)
html = response.read()
charset = chardet.detect(html)['encoding']
html = html.decode(charset)
print(html)