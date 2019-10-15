import csv
import time
#from xml.dom import minidom
#settings = minidom.parse('lab1.xml')
#itemlist = settings.getElementsByTagName('item')
#a = settings.childNodes[0]
#print(itemlist)
#print (a.firstChild.nodeValue)

entropy  = open("/home/students/mgr2018/maccza/Desktop/KiBdF/entropy.txt", "r")
value = []
i = 0
while (True):
	entropy_avile  = open("/proc/sys/kernel/random/entropy_avail", "r")
	for x in entropy_avile:
			value.append(int(x))
	entropy_avile.close()
	with ("
	time.sleep(4)
print(value)	
			

