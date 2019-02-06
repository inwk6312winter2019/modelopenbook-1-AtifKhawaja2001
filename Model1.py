def list_ifname_ip():
	fout = open('running-config.cfg')
	print(fout)
	a = ''
	d = {}
	l = []
	l1 = []
	l_ip = []
	l_name = []
	l_mask = []
	for line in fout:
		line1 = line.split()
		for i in range(len(line1)-1):
			if line1[i] == 'nameif':
				l.append(line1[i+1])
		for i in range(len(line1)-2):
			if line1[i] == 'ip':
				if line1[i+1] == 'address':
					l.append(line1[i+2])
					l.append(line1[i+3])


#Each of the for loops written below create a sublist from master list named 'l' for name, ip and subnetmask.

	for i in range(0,len(l)-2,3):
		l_ip.append(l[i+1])
	#print(l_ip)

	for i in range(0,len(l),3):
		l_name.append(l[i])
	#print(l_name)

	for i in range(0,len(l)-2,3):
		l_mask.append(l[i+2])
	#print(l_mask)

	for i in range(len(l)-2):
		t = zip(l_ip,l_mask)

	for pair in t:
		l1.append(pair)
	#print(l1)


	for i in range(len(l1)):
		d.setdefault(l_name[i],l1[i])
	print(d)

list_ifname_ip()
