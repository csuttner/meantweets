# define class eword (every word) to give each word in the body properties:
# 'normindx' (normalized index): value between 0 and 1 that represents the location
# of the word within the parent sentence
# 'sval' (sentance value): weight of this word's 'value' inversely proportional to
# sentance length (words occuring in shorter sentances have more weight)
class eword:
	def __init__(self, word, pslen, psindx):
		self.word = word
		self.pslen = pslen
		self.psindx = psindx
		self.normindx = psindx / float(pslen)
		self.sval = 1 / float(pslen)

# define splitting function that works for multiple delimiters at once
def split(delimiters, string, maxsplit=0):
	regexPattern = '|'.join(map(re.escape, delimiters))
	return re.split(regexPattern, string, maxsplit)

# muliple replacement function
def replace_all(string, dic):
	for p, q in dic.iteritems():
		string = string.replace(p,q)
	return string

def filterblanks(string):
	return filter(lambda a: a != '',string)