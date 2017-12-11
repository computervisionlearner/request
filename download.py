"""
Created on Wed Sep 20 20:48:39 2017

@author: Administrator
"""

import re
import requests
import os
import urllib
import time
#import requests

headers = {
           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
           "Accept-Encoding": "gzip, deflate",
           "Accept-Language": "en-US,zh-CN;q=0.8,zh;q=0.6,en;q=0.4",
           "Cache-Control": "no-cache",
           "Connection": "keep-alive",
           "Cookie":"__cfduid=dcfc12ae114bd992191e9df6bcab73b411505894023; yjs_id=TW96aWxsYS81LjAgKFgxMTsgVWJ1bnR1OyBMaW51eCB4ODZfNjQ7IHJ2OjU1LjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvNTUuMHx3d3cuaGFvaTIzLm5ldHwxNTA1ODk0MDI1NjI2fGh0dHA6Ly93d3cuaGFvaTIzLm5ldC8; UM_distinctid=15e9e47525113e-05643a44814957-71206751-1aeaa0-15e9e47525259; CNZZDATA5003870=cnzz_eid%3D1625580320-1505889249-%26ntime%3D1506322448; AJSTAT_ok_times=11; Hm_lvt_93e96130e9baaf094d30957b36d95ccf=1505894029; _qddaz=QD.655le3.9mtu0v.j7sqfhvn; tencentSig=3851687936; pgv_pvi=6161187840; user=uid=623345387&pwd=a12345678; ASP.NET_SessionId=idizkcio235jgrcalvkijxal; IESESSION=alive; _qddab=3-m56pjk.j7zvummn; pgv_si=s1050876928; ctrl_time=1; AJSTAT_ok_pages=9; _qdda=3-1.2x97cs; _qddamta_800058301=3-0",
           "Pragma": "no-cache",
           "Referer": "http://www.haoi23.net/login.aspx?act=reg",
           "Upgrade-Insecure-Requests": "1",
           "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:55.0) Gecko/20100101 Firefox/55.0"
         }


session=requests.Session()


def dowmloadPic(html, page):
    print ('找到第'+str(page)+'页的图片，现在开始下载图片...')
    pictures_names=re.findall(r"img src='(http://.+?\.gif)'.+?<td>((?:\w|\d){4,5})</td>",html,re.S)
    os.chdir('pictures')
    for picture, name in pictures_names:
        if re.search(r'\d\d\d\d',name):
            if len(name)==4:
                print('_________start print new picture__________')
                urllib.request.urlretrieve(picture,name+'_{}.jpg'.format(page))
                time.sleep(0.05)

    os.chdir('..')

def main():
    if os.path.exists('pictures') is False:
        os.makedirs('pictures')
    
    start = input("Input start page: ")
    end = input("Input last page: ")
    while(int(end)<1):
        print('Input must be >0! Please input again.')
        end = input("Input last page: ")
    
    
    base_url = 'http://www.haoi23.net/u_3mypic.aspx?day=all&s=0&e=23&page={pageNum}'
    for i in range(int(start), int(end)+1):
        url = base_url.format(pageNum=i)
        result = session.get(url, headers=headers).text
        dowmloadPic(result, i)
    

if __name__=='__main__':
    main()

