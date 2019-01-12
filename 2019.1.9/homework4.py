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
import chardet
from lxml import etree

url = 'http://zst.aicai.com/ssq/openInfo/'
headers = {'User-Agent':'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)'}
req = request.Request(url,headers=headers)
response = request.urlopen(req)
# 读取页面源码
html = response.read()
html = html.decode()
# 获取每条历史信息
selector = etree.HTML(html)
print(selector)
ccc = selector.xpath('//tr[contains(@onmouseout, "this.style.")]')
# print(ccc)
for i in ccc:
    infor = i.xpath('.//td/text()')
    print('期号：',infor[0],'开奖日期：',infor[1],'红色球：',infor[2:8],'蓝色球：',infor[9],'一等奖:','注数:',infor[10],'金额：',infor[11],'二等奖:','注数:',infor[12],'金额：',infor[13])
