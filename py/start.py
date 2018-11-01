# -*- coding:utf-8 -*-
# Author:Gao Shuai
import datetime
import time
#可以放在linux中  linux可以不用关机，即定时任务一直存活；
def doSth():
    #把爬虫程序放在这个类里
    print(u'这个程序要开始疯狂的运转啦')
#一般的网站都是一点更新数据，所有每天凌晨一点启动
def main(h=1,m=0):
    while True:
        now = datetime.datetime.now()
        print(now.hour,now.minute)
        if now.hour == h and now.minute == m:
            break
            #每隔60秒检测一次
            time.sleep(60)
    doSth()

main()