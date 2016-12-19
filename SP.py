import itertools
n = input()
l1 = ["".join(seq) for seq in itertools.product("01", repeat=n)]

print l1

for i in range(0,len(l1)):

	for j in range(i,len(l1)):
		print l1[i],l1[j]
		ls = len([k for k in xrange(len(l1[i])) if l1[i][k] != l1[j][k]])                
		print ls
	

	# new input 0
	# new state 
#	os = l1[i]
#	s0 = l1[i]+ '0'
	#new input 1
#	s1 = l1[i]+ '1'
	# first output		#int(k[1][1])^int(k[2][2])	
	# 11
#	if n == 2:
#		z1 = int(s0[-1])^int(s0[-3])
#		o1 = int(s1[-1])^int(s1[-3])
	# second output
#		z2 = int(s0[-1])^int(s0[-3])^int(s0[-2])
#		o2 = int(s1[-1])^int(s1[-2])^int(s1[-3])
#	else :

#		z1 = int(s0[-1])^int(s0[-2])^int(s0[-4])
#		o1 = int(s1[-2])^int(s0[-3])^int(s1[-4])
	# second output
        #print s," will have ", g0
#		z2 = int(s0[-1])^int(s0[-3])^int(s0[-2])
#		o2 = int(s1[-1])^int(s1[-2])^int(s1[-3])

#	print os,s0[1:],z1,z2,s1[1:],o1,o2
