# muliple replacement function
def replace_all(string, dic):
	for p, q in dic.iteritems():
		string = string.replace(p,q)
	return string

def filterblanks(string):
	return filter(lambda a: a != '',string)

