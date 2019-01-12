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
# 3、用cookie模拟登录微博
from urllib import request
from urllib import parse
import requests
import chardet


# 微博链接
url="https://weibo.com/u/3830405053"
head = {}
# 设置请求头
head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
head['Cookie'] = 'Ugrow-G0=968b70b7bcdc28ac97c8130dd353b55e; login_sid_t=c18906631cc89fe169b367f57f6692ce; cross_origin_proto=SSL; YF-V5-G0=16139189c1dbd74e7d073bc6ebfa4935; WBStorage=bfb29263adc46711|undefined; wb_view_log=1366*7681; _s_tentry=passport.weibo.com; Apache=771426354371.687.1547033567670; SINAGLOBAL=771426354371.687.1547033567670; ULV=1547033567683:1:1:1:771426354371.687.1547033567670:; YF-Page-G0=e44a6a701dd9c412116754ca0e3c82c3; WBtopGlobal_register_version=b9a57a005a2c8e14; SCF=AnJVy9cdQaFysv58L3cD1lPhGNB85g4nW48lEwf7Wy2pKJtfDmx0TDyq4eSS2SP84-jfyjOaeBdV06gt20UMkJY.; SUB=_2A25xMazfDeRhGeVG6FIV8CvMzj-IHXVSRpkXrDV8PUNbmtBeLXf4kW9NT6dGSC9WbzG1wOByiLm50AQlJXHjXWFt; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9Wh.T8iLu--cfxOMxhl-9UIE5JpX5K2hUgL.FoeRe05Xeh-7SKe2dJLoIEvhPEH81C-4xF-4xCH8SbHFSFHFebH8SCHFeF-RxbH8SE-41CHFxFH81F-RSFHF15tt; SUHB=0A0J8PEOcjmrmU; ALF=1547638542; SSOLoginState=1547033743; un=15638130217; wb_view_log_3830405053=1366*7681; wvr=6'
req = request.Request(url,headers=head)
# 读取页面内容
response = request.urlopen(req)
html = response.read()
# 编码
charset = chardet.detect(html)['encoding']
html = html.decode(charset)
print(html)