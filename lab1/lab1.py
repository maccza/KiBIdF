import csv
import time
from xml.dom import minidom
xml_ = minidom.parse('lab1.xml')
settings_tree = xml_.documentElement
settings = settings_tree.getElementsByTagName('items')
time_ = 0
file_name = '' 
for setting in settings:
	par_time = setting.getElementsByTagName('time')[0]
	time_= int(par_time.childNodes[0].data)
	par_file = setting.getElementsByTagName('file_name')[0]
	file_name = par_file.childNodes[0].data
    
print(time_)
print(file_name)

entropy = []

while (True):
	entropy_avile  = open("/proc/sys/kernel/random/entropy_avail", "r")
	for x in entropy_avile:
			entropy.append(int(x))
	entropy_avile.close()
	#with ("
	time.sleep(time_)
	print(x)
	entropy.pop()
	
			

