# -*- coding:utf-8 -*-
# By 狂风烈酒 qq：2654785478
import requests
import re
import threading
import time
headers={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}

var1 = 'http://' #网址前
var3 = '.html'   #网址后

class myThread (threading.Thread):
    def __init__(self, a, sz):
        threading.Thread.__init__(self)
        self.a = a
        self.sz = sz
        
    def run(self):
      
 
        cai_ji(self.a, self.sz)

def cai_ji(a,sz):
 
   while a >0:

    var2 =str(sz)
    var = var1 + var2 + var3
    #网址合成
    r1 = requests.get(var,headers=headers)
    r1.encoding='utf-8'
    title= re.search('.*',r1.text,re.I)
    video = re.search('.*',r1.text,re.I)
    #".*"贪婪正则
    
    print(sz)
    print(a)
    if  title:
     if  video :
      ft = str(title.group())
      fv = str(video.group())
      
      fhtml= open('%d.html'%sz,'w+')
      ftitle=open('Title.txt','a')
      
     
      print(str(sz)+'\n',file=ftitle)
     
      print(fv,file=fhtml)
      
      print(ft)
      
      print(fv)
      fhtml.close()
      ftitle.close()
    a=a-1
    sz=sz-1

threadLock = threading.Lock()
threads = []

# 创建新线程
thread1 = myThread(2500,21379) #（爬取数量，开始位置）
thread2 = myThread(2500,23879)

# 开启新线程
thread1.start()
thread2.start()


# 添加线程到线程列表
threads.append(thread1)
threads.append(thread2)

# 等待所有线程完成
for t in threads:
    t.join()
print ("退出主线程")
