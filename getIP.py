#coding=UTF-8
import urllib.request
import sys,re

defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)


class Getip():
    def __init__(self,can):
        self.ur = "http://www.xiladaili.com/gaoni/"

    def getip(self,ren):
        
  
        url = self.ur+str(x)
  
        ip_proxy_re = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
        
        try:
            data = urllib.request.urlopen(url).read().decode()
            #print(data)
        except:
            #print("error")
            return None
  
        self.rel = []
  

        ip = ip_proxy_re.findall(data)
        
        return ip
if __name__ == '__main__':
    g=Getip("")
    res=[]
    
    import pprint
    for x in range(2,5):
        ips = g.getip(x)
        #print('获取到ip地址一共:',len(ips))
        #print(ips)
        if ips != None:
        	res += ips

    for i in res:
        print(i,end=' ')
      #print(res)