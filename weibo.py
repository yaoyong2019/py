import os
import re
import sys
import time
import json
import requests
import multool
from bs4 import BeautifulSoup as bs

#uid即进入对方微博主页后网址部分/u/后的那一串数字
#https://weibo.cn/u/1912992047?page=1
wbname='yaoyong001'
wbpwd='yy@2489504'
uid = 1912992047
url = 'https://weibo.cn/u/' + str(uid)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Referer': 'https://passport.weibo.cn/signin/login',
    'Connection': 'close',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3'
    }

pictrue_num = 0 #当前已爬取的图片总数
Loginsession = requests.session()

def GetPageAddr():
    GetSession()
    r = Loginsession.get(url, headers=headers)
    soup = bs(r.text, 'lxml')
    # 所访问的微博用户名
    weibo_user_name = soup.find('title').text.replace(u'的微博', '')

    # 存放图片的根目录
    rootDir = 'D://微博配图相册//' + weibo_user_name + '//'
    if not os.path.exists(rootDir):
        os.makedirs(rootDir)
    
    # 微博总页数,通过审查元素可知
    totalPage = int(soup.find('input', attrs={'name':'mp'}).attrs['value'])
    print('总共检测到%d页微博页面' % totalPage)
    
    for pagenum in range(1,totalPage+1):
        GetPageItems(rootDir,pagenum)
    print('总共爬取了%d张图片,存放在%s目录下' % (pictrue_num, rootDir))
        
def GetPageItems(dirpath,pagenum):
    # 每页微博的URL的列表
    weibo_url = url + '?page=' + str(pagenum)
    r = Loginsession.get(weibo_url, headers=headers)
    soup = bs(r.text, 'lxml')
    
    #每条微博所对应的标签代码块列表
    weibo_tags_list = soup.find_all('div', attrs={'class': 'c'}, id=True)
    
    wma = MulTool.WorkManager(8)
    #微博发送时间与微博配图的字典
    for u in range(len(weibo_tags_list)):
        print('正在爬取第%d页第%d条微博' % (pagenum, u + 1))
        wma.add_job(GetOneAlbum,dirpath,weibo_tags_list[u])
    wma.start()
    wma.wait_for_complete()
    print('第%d页微博爬取完毕,开始生成图片' % (pagenum))
        
        
def GetOneAlbum(dirpath,weibo_tag):       
    #获取微博发送时间
    try:
        hms = ' '.join(weibo_tag.find('span', attrs={'class': 'ct'}).string.replace('\xa0', ' ').replace(':', '-').split(' ')[:2])
    except:
        hms = ' '.join(weibo_tag.find('span', attrs={'class': 'ct'}).text.replace('\xa0', ' ').replace(':', '-').split(' ')[:2])
        
    if weibo_tag.find('span', attrs={'class': 'cmt'}):
        print("转发\n")
        #return; #本行如果注释掉就和下载转发的微博
    t=1    
    #该条微博若带有组图，获取组图中所有图片的URL
    if weibo_tag.find('a', text=re.compile('组图')):
        imgs_url = weibo_tag.find('a', text=re.compile('组图')).attrs['href']
        html = Loginsession.get(imgs_url, headers=headers)
        imgs_soup = bs(html.text, 'html.parser')
        imgs_tags_List = imgs_soup.find_all('img', alt='图片加载中...')
        img_urls_list = [imgs_tag.attrs['src'].replace('thumb180', 'large') for imgs_tag in imgs_tags_List]
        #imgs_urls_dic[hms] = img_urls_list
    #该条微博仅有一张配图，或者没有图片，获取图片的URL
    else:
        img_tags_List = weibo_tag.find_all('img', alt='图片')
        img_urls_list = [img_tag.attrs['src'].replace('wap180', 'large') for img_tag in img_tags_List]
        #imgs_urls_dic[hms] = img_urls_list
    print("该条微博还有%d 张图片" %len(img_urls_list))
    wmb = MulTool.WorkManager(6)
    for u in range(len(img_urls_list)):
        wmb.add_job(SaveImg,dirpath,hms,img_urls_list[u],t)
        t=t+1
    wmb.start()
    wmb.wait_for_complete()
    
def SaveImg(dirpath,hms,img_url,index):
    global pictrue_num
    #生成图片的存放路径，图片被命名为微博发送时间
    path = dirpath + hms
    
    #如果一条微博在同一时间发送了多张图片(即组图)的命名处理
    if(img_url[-3:]=="gif"):
        path = path + '-' + str(index+1)+'.gif'
    else:
        path = path + '-' + str(index+1)+'.jpg'
    try:
        if not os.path.exists(path):
            r = Loginsession.get(img_url)
            with open(path, 'wb') as f:
                f.write(r.content)
                pictrue_num = pictrue_num + 1
            time.sleep(1)
        else:
            print('%s已经存在' % path)
            pictrue_num = pictrue_num + 1
        print('success,成功爬取第%d张图片' % pictrue_num)
    except Exception as e:
        print('爬取失败,%s' % img_url)

def GetSession():
    loginApi = 'https://passport.weibo.cn/sso/login'
    loginPostData = {
        'username':wbname,
        'password':wbpwd,
        'savestate':1,
        'r':'',
        'ec':'0',
        'pagerefer':'',
        'entry':'mweibo',
        'wentry':'',
        'loginfrom':'',
        'client_id':'',
        'code':'',
        'qq':'',
        'mainpageflag':1,
        'hff':'',
        'hfp':''
    }
    r = Loginsession.post(loginApi,data=loginPostData,headers=headers)
    try:
        if r.status_code == 200 and json.loads(r.text)['retcode'] == 20000000:
            print("successful")
        else:
            #print(r.status_code)
            #print(r.text)
            print("Logon failure!")
    except Exception as e:
        print(e)
        print("Logon failure2!")
        
GetPageAddr()