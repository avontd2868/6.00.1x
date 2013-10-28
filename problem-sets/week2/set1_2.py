numBobs = 0
s = 'abodkjboblskjbobobobkjsdflk'
for i in range(1, len(s)-1):
    print "\n--: %s" % s[i-1]
    print ">:  %s" % s[i]
    print "++: %s" % s[i+1]
    if s[i-1:i+2] == 'bob':
	print "A WILD BOB APPEARED"
        numBobs += 1
print '\nNumber of times bob occurs is:', numBobs
