filename = raw_input('Enter a (.txt) filename ')

F = open(filename,"r")
wcount = 0
scount = 0
i = 0

cnv = F.read()

for i in range(0,len(cnv)):
	if cnv[i] == ".":
		scount = scount + 1
	elif cnv[i] == " ":
		wcount = wcount + 1
	i = i + 1
print scount
print wcount + 1