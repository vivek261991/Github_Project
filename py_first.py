import binascii
from socket import *
import time
import sys
import pickle as pickle
from collections import deque
filename = ['link1flow','link2flow','link3flow']
rawList1 = []
rawList2 = []
rawList3 = []
bitList4 = []
bitList5 = []
output_port1 = []
output_port2 = []
output_port3 = []
link1List = deque()
c = 0
count = 0
b  = ""
counties = 0
routing_table = {'221.111.180.241':'output_port1','222.112.192.202':'output_port2','223.113.132.243':'output_port3'}
print routing_table['221.111.180.241']

for file in filename:
	with open(file, 'rb') as f:
			content = f.read(2500)
			if not content: break
			for a in content:
				count += 1
				b += a
				if(count == 500):
					if file == 'link1flow':
						rawList1.append(b)
					if file == 'link2flow':
						rawList2.append(b)
					if file == 'link3flow':
						rawList3.append(b)
					 
					b = ""
					count = 0
						
print "before pop....................."
print len(rawList1)
print len(rawList2)
print len(rawList3)

def write_to_files(op1, op2, op3):
	
	
	o1 = open('output_link_1.txt', "w")
	o2 = open('output_link_2.txt', "w")
	o3 = open('output_link_3.txt', "w")
	
	while (len(op1) != 0) and (len(op2) != 0) and (len(op3) != 0):
		if(len(op1) != 0):
			print >> o1,op1.pop(0)
		if(len(op2) != 0):
			print >> o2,op2.pop(0)
		if(len(op3) != 0):
			print >> o3,op3.pop(0)
	
	o1.close()
	o2.close()
	o3.close()
	

def exract_dest_addr(string):

	bitList = []
	binary_string = bin(int(binascii.hexlify(string), 16))[2:].zfill(8)
	
	for x in binary_string:
		bitList.append(x)
	
	dest1 = bitList[128]+bitList[129]+bitList[130]+bitList[131]+bitList[132]+bitList[133]+bitList[134]+bitList[135]
	dest2 = bitList[136]+bitList[137]+bitList[138]+bitList[139]+bitList[140]+bitList[141]+bitList[142]+bitList[143]
	dest3 = bitList[144]+bitList[145]+bitList[146]+bitList[147]+bitList[148]+bitList[149]+bitList[150]+bitList[151]
	dest4 = bitList[152]+bitList[153]+bitList[154]+bitList[155]+bitList[156]+bitList[157]+bitList[158]+bitList[159]
	full_dest = str(int(dest1, 2)) + "." + str(int(dest2, 2)) + "." + str(int(dest3, 2)) + "." + str(int(dest4, 2))

	return full_dest

def router(rawList1,rawList2,rawList3):

	while (len(rawList1) != 0) and (len(rawList2) != 0) and (len(rawList3) != 0):
  
		if(len(rawList1) != 0):
			p = rawList1.pop(0)
			if routing_table[exract_dest_addr(p)] == 'output_port1':
				output_port1.append(p)
		if(len(rawList2) != 0):
			q = rawList2.pop(0)
			if routing_table[exract_dest_addr(q)] == 'output_port2':
				output_port2.append(q)
		if(len(rawList3) != 0):
			r = rawList3.pop(0)
			if routing_table[exract_dest_addr(r)] == 'output_port3':
				output_port3.append(r)

	write_to_files(output_port1, output_port2, output_port3)
		
	print "after pop................."		
	print	len(rawList1)
	print	len(rawList2)
	print	len(rawList3)
	
	
	







router(rawList1,rawList2,rawList3)



	
	

	
	#clientSocket = socket(AF_INET, SOCK_STREAM)
	#clientSocket.connect(('localhost', 9007))
	#data = pickle.dumps(link1List.popleft())
	#clientSocket.send(data)
	#clientSocket.close()