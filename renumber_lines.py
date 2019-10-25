import sys

lineno = 1000
for line in sys.stdin.readlines():
	line = line.rstrip()
	
	if len(line) > 0:
		if line[0] == 'M' or line[0] == 'G':
			pp = line.split()
			wl = ''
			flag = True
			for item in pp:
				if (item[0] == 'X' or item[0] == 'Y' or item[0] == 'A' or item[0] == 'F' or item[0] == 'Z') and len(item) == 1:
					flag = False
					wl += item
				else:
					flag = True
					wl += item
					
				if flag:
					wl += ' '
					
			sys.stdout.write("N%d %s\n"%(lineno, wl))
			lineno += 10
		else:
			sys.stdout.write("%s\n"%(line))
	else:
		sys.stdout.write("\n")
		
