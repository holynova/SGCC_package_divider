# -*- coding: utf-8 -*-
class VoltDic:
	def __init__(self,batch,volt,bottom,top):
		self.batch = batch
		self.volt = volt
		self.bottom = bottom
		self.top = top
	def __str__(self):
		return 'batch=%s, volt=%s, bottom=%d, top=%d' %(self.batch,self.volt,self.bottom,self.top)
class Package:
	def __init__(self,id,batch,pack_num,volt=''):
		self.id = id
		self.batch = batch
		self.pack_num = pack_num
		self.volt = volt
	def __str__(self):
		return 'id = %s,batch = %s,pack_num = %s, volt = %s' %(self.id,self.batch,self.pack_num,self.volt)
	def show_id_volt(self):
		print '%s,%s' %(self.id,self.volt)
	def find_volt(self):
		#dic = 
		for v in my_volt_dic:
			if self.batch == v.batch:
				if self.pack_num >= v.bottom and self.pack_num <= v.top:
					self.volt = v.volt
					break

my_volt_dic = [
VoltDic('2015#1','HV',1,30),
VoltDic('2015#1','MV',31,50),
VoltDic('2015#1','submarine',51,52),
VoltDic('2015#2','HV',1,45),
VoltDic('2015#2','HV',47,56),
VoltDic('2015#2','MV',57,95),
VoltDic('2015#2','submarine',46,46),
VoltDic('2015#2','submarine',66,66),
VoltDic('2015#2','submarine',96,96),
VoltDic('2015#3','HV',1,64),
VoltDic('2015#3','MV',65,96),
VoltDic('2015#3','submarine',97,100),
VoltDic('2015#4','HV',1,54),
VoltDic('2015#4','MV',55,73),
VoltDic('2015#5','HV',1,51),
VoltDic('2015#5','MV',52,68),
VoltDic('2015#6','HV',1,19),
VoltDic('2015#6','MV',20,36),
VoltDic('2015#6','submarine',37,39),
VoltDic('2016#1','220kv',1,3),
VoltDic('2016#1','HV',4,32),
VoltDic('2016#1','MV',33,47),
VoltDic('2014#1','HV',1,114),
VoltDic('2014#1','MV',115,158),
VoltDic('2014#2','HV',1,87),
VoltDic('2014#2','MV',88,168),
VoltDic('2014#2','submarine',169,171),
VoltDic('2014#3','HV',1,72),
VoltDic('2014#3','MV',73,148),
VoltDic('2014#3','submarine',149,150),
VoltDic('2014#4','HV',1,110),
VoltDic('2014#4','MV',111,145),
VoltDic('2014#5','HV',1,53),
VoltDic('2014#5','MV',54,91),
VoltDic('2014#6','HV',1,37),
VoltDic('2014#6','HV',39,67),
VoltDic('2014#6','MV',68,98),
VoltDic('2014#6','submarine',38,38),]


def import_package_from_file(filename):
	pack_arr = []
	with open(filename,'r') as data:
		while True:
			line = data.readline()
			if len(line) <= 5:
				break
			else:
				line_words_arr = line.split()
				if len(line_words_arr) == 3:
					pack_arr.append(Package(int(line_words_arr[0]),line_words_arr[1],int(line_words_arr[2]),'test'))
		return pack_arr

packages = import_package_from_file('C:\Users\sym\Desktop\package.txt')
result_file_name = 'C:\Users\sym\Desktop\\volt'+'_'+'.txt'


for package in packages:
	package.find_volt()
	package.show_id_volt()

