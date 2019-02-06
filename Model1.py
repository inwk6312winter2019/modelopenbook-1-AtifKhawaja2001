def list_ifname_ip():
	fout = open('running-config.cfg')
	print(fout)

	l = []
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

	print(l)

list_ifname_ip()
