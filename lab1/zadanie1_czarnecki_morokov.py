import csv
import time
from xml.dom import minidom

xml_ = minidom.parse('lab1.xml')
settings_tree = xml_.documentElement
settings = settings_tree.getElementsByTagName('items')
time_ = 0
file_name = ''
time_collecting = 0 
for setting in settings:
    par_time = setting.getElementsByTagName('time')[0]
    time_= int(par_time.childNodes[0].data)
    par_file = setting.getElementsByTagName('file_name')[0]
    file_name = par_file.childNodes[0].data
    par_time_collecting = setting.getElementsByTagName('time_collecting')[0]
    time_collecting = int(par_time_collecting.childNodes[0].data)       
print(time_)
print(file_name)
print(time_collecting)
time_sleep = time_ # co ile sekund odczytujemy wartosc entropii
time_measurement = time_collecting # czas pomiaru - w ciagu ilu sekund chcemy zapisywac wartosc entropii
number_entropy = int(time_measurement/time_sleep) # ile razy zmierzy nam entropie
print(number_entropy)

with open(file_name, 'w', encoding='utf-8') as csvfile:
	csvwriter = csv.writer(csvfile)
	for i in range(number_entropy):
		entropy_avile  = open("/proc/sys/kernel/random/entropy_avail", "r")
		for x in entropy_avile:
			s = int(x)
		entropy_avile.close()
		csvwriter.writerow([s])
		time.sleep(time_sleep)
csvfile.close()