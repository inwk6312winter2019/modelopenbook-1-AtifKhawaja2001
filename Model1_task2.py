def newfile():
	fout = open('running-config.cfg')
	fin = open('newconfigfile.cfg','w+')

	l = []
	l1 = []

	book = fout.read()
	line = book.split()

	for i in range(len(line)):
		if '192.' in line[i]:
			line[i] = line[i].replace('192.','10.')
		if '172.' in line[i]:
			line[i] = line[i].replace('172.','10.')
		if '255.255.255.0' in line[i]:
			line[i] = line[i].replace('255.255.255.0','255.0.0.0')
		if '255.255.0.0' in line[i]:
			line[i] = line[i].replace('255.255.0.0','255.0.0.0')

	result = '\n'.join(line)
	print(result)

	fin.write(result)

newfile()

