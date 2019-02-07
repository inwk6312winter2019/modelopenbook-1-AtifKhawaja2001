def access_list():
	l_transit = []
	l_management = []
	l_global = []

	fout = open('running-config.cfg')
	for line in fout:
		line1 = line.split()
		for i in range(len(line1)):
			if line1[i] == 'access-list':
				if line1[i+1] == 'transit_access_in':
					l_transit.append((line1[i+2::]))

				if line1[i+1] == 'fw-management_access_in':
					l_management.append((line1[i+2::]))

				if line1[i+1] == 'global_access':
					l_global.append((line1[i+2::]))

	print("Transit Access List = ",l_transit,'\n')
	print("fw Management Access List = ", l_management,'\n')
	print("Global Access List = ", l_global)

access_list()
