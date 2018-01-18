import wechatsogou
from selenium import webdriver
import random

wxid=['手帐研究室','新华社']
turl = []
tname = []
ws_api =wechatsogou.WechatSogouAPI()
for w in wxid:
    url = ws_api.get_gzh_info(w)['profile_url']
    browser = webdriver.PhantomJS("phantomjs.exe")
    browser.get(url)
    t=browser.find_elements_by_tag_name('h4')
    for x in t:
        turl.append('https://mp.weixin.qq.com'+x.get_attribute('hrefs'))  #微信原文链接
        tname.append(x.text)  #微信原文标题
tshow=random.randint(0, len(tname)-1)  #产生随机一篇库中文章的序号
print(tname[tshow])
print(turl[tshow])
