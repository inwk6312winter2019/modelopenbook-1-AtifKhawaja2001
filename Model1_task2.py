def newfile():
	fout = open('running-config.cfg')
	fin = open('newconfigfile.cfg','w+')

	a = ''
	l = []
	l1 = []

	book = fout.read()
	line = book.split()

	#for word in line:
		#l.append(word)
	#print(l)

	for i in book:
		for word in line:
			if '192.' in word:
				a = word.replace('192.','10.')
				print(a)
			if '172.' in word:
				a = word.replace('172.','10.')
				print(a)
			if word == '255.255.0.0':
				a = word.replace('255.255.0.0','255.0.0.0')
				print(a)
			if word == '255.255.255.0':
				a = word.replace('255.255.255.0','255.0.0.0')
				print(a)


newfile()

