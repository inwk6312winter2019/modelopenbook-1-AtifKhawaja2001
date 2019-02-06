def list_ifname_ip():
	fout = open('running-config.cfg')
	print(fout)

	l = []
	for line in fout:
		line1 = line.split()
		for i in range(len(line1)-2):
			if line1[i] == 'nameif':
				pass
				print(line1[i+1])
			if line1[i] == 'ip':
				if line1[i+1] == 'address':
					print(line1[i+2],line1[i+3])
list_ifname_ip()
