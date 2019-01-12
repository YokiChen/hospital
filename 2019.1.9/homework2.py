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

# 2、利用cookie和post模拟登录人人网个人主页
from urllib import request
from urllib import parse
import requests


url = 'http://www.renren.com/SysHome.do'
# 创建session 对象，保存cookie
cookie_ = requests.session()
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
# 输入用户名密码
data = {'email':'873356647','password':'czy5210.0'}
cookie_.post(url,data=data,headers=headers)
respon = cookie_.get('http://www.renren.com/969396513')
print(respon.text)