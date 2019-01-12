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

'''
bs4课件
1、医疗器械网爬虫 http://www.chinamedevice.cn/
以医疗产品分类下的外科器械，康复护理设备器具，口腔科设备等大的分类为入口，爬取医疗产品
使用 BeautifuSoup4 解析器进行数据提取，提取产品名称，产品url，封面url，产品类别，
批准文号，产品规格，产品说明,产品说明，联系人，联系电话，移动电话，单位地址
保存到mysql数据库中
'''

from bs4 import BeautifulSoup
import requests
from lxml import etree
import chardet
import pymysql

def Hospitle():
    url= 'http://www.chinamedevice.cn/'
    req = requests.get(url)
    html = req.content.decode('gbk')
    # print(html)
    # 创建Bs4对象
    soup = BeautifulSoup(html,'lxml')
    a=soup.select('.f12')
    num = 0
    for i in a:
        one_href = 'http://www.chinamedevice.cn'
        name = i.get_text()
        new_url = one_href+i['href']
        reqq = requests.get(new_url)
        # charset = chardet.detect()
        htmls = reqq.content
        charset = chardet.detect(htmls)['encoding']
        htmls = htmls.decode(charset, 'ignore')
        num+=1
        print('第%s页加载完成'%num)
        # print(name,new_url)
        soup2 = BeautifulSoup(htmls,'lxml')
        b = soup2.select('.list > ul >li')

        for j in b:
            # 单个产品的链接
            datail_url = j.select('a')[0].attrs['href']
            print('产品url',datail_url)
            # 图片链接
            img_url = j.select('img')[0].attrs['src']
            print('图片url',img_url)
            # 进入单个商品的链接
            reqqq = requests.get(datail_url)
            htmlss = reqqq.content
            charsets = chardet.detect(htmlss)['encoding']
            htmlss = htmlss.decode(charsets,'ignore')
            # print(htmlss)
            soup3 = BeautifulSoup(htmlss,'lxml')

            # 提取产品名称，产品类别，产品批准文号，产品规格
            c = soup3.select('div[class="text01"] > ul > li')
            name = c[0].get_text()
            print(name)
            kind = c[1].get_text()
            print(kind)
            bianhao = c[3].get_text()
            print(bianhao)
            guige = c[4].get_text()
            print(guige)
            print('-'*50)
            d = soup3.select('dd[class="text03"]')[0].get_text()
            print(d)
            print('-' * 50)
            # 联系人，联系电话，移动电话，单位地址
            e = soup3.select('dd[class="text04"] > ul > li')
            # 联系人
            name_p = e[2].get_text()
            print(name_p)
            # 联系电话
            phone = e[3].get_text()
            print(phone)
            mobile_phone = e[4].get_text()
            print(mobile_phone)
            # 单位地址
            add = e[9].get_text()
            print(add)
            date=name,kind,bianhao,guige,name_p,phone,mobile_phone,add
            # 写入数据库

            con = pymysql.connect(host='localhost', user='root', password='123456', database='game', port=3306)
            cur = con.cursor(cursor=pymysql.cursors.DictCursor)
            try:
                nn = cur.execute("insert into yiliao values (0,%s,%s,%s,%s,%s,%s,%s)", date)
                con.commit()
            except Exception as e:
                print(e)
                if con is not None:
                    con.rollback()
            finally:
                if cur is not None:
                    cur.close()
                if con is not None:
                    con.close()

            print('*' * 70)

if __name__ == '__main__':
    Hospitle()