import itertools
#n = input()
l1 = ["".join(seq) for seq in itertools.product("01", repeat=11)]
#print l1

for i in range(0,len(l1)):
	
	os = l1[i]

	c1 = int(os[-1])^int(os[-2])^int(os[-3])^int(os[-4])^int(os[-9])^int(os[-10])^int(os[-11]) 
	c2 = int(os[-1])^int(os[-2])^int(os[-3])^int(os[-5])^int(os[-7])^int(os[-8])^int(os[-11])
	c3 = int(os[-1])^int(os[-2])^int(os[-4])^int(os[-5])^int(os[-6])^int(os[-10])^int(os[-8])
	c4 = int(os[-1])^int(os[-5])^int(os[-3])^int(os[-4])^int(os[-6])^int(os[-7])^int(os[-9])
	#l1[11] = c1
	l1[i] = os + str(c1) +str(c2) + str(c3) + str(c4)
	#ns = os + c1 + c2 + c3 + c4
#	l1[i] = ns
minv = 3
for i in range(0,len(l1)):
	
	for j in range(i+1,len(l1)):
		print i,j
		ls = len([k for k in xrange(len(l1[i])) if l1[i][k] != l1[j][k]])
		print ls
		if ls < minv :		
			minv = ls

print minv

