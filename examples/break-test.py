for n in range(2, 10):
	for x in range(2, n):
		if n % x == 0:
			print str(n) + ' equals ' + str(x) + ' * ' + str(n/x)
			break
		else:
			print str(n) + ' is a prime'
