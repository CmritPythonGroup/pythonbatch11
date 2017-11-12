try:
	with open('first.txt', 'r') as inp:
		with open('second.txt', 'w') as out:
			for line in inp:
				out.write(line)
except IOError:
        print "Wrong file or file path"
