import sys

# input comes from STDIN (standard input)



for lines in sys.stdin:
	line=lines.strip()
	words = line.split()
	for word in words:
		print("%s\t%s" %(word,1))
