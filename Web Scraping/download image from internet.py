import urllib.request
import datetime
raw_time = str(datetime.datetime.now())[:10] 
time_list = raw_time.split('-')
space = ''
time = space.join(time_list)
file_name = str('C:\\Users\\hp-pc\\Desktop\\' + time + '.jpg')
print ('file name:', file_name) 
file = open(file_name, 'wb')
url = input('Please enter url:')
content = urllib.request.urlopen(url).read()
file.write(content)
file.close()
print ('image download done')
