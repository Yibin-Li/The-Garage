import urllib.request
import gzip
def geturl(url):  
    #返回页面内容  
    doc = urllib.request.urlopen(url).read()  
    #解码  
      
    html=gzip.decompress(doc).decode("utf-8")  
     
    return html
print (geturl('http://sports.sina.com.cn/china/national/2016-08-30/doc-ifxvixer7459178.shtml'))
