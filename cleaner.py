# Obtains 3D list of list of lists (tweets, sentances, words)

import csv
import re
from mtclasses import split, replace_all, filterblanks

# CSV -> List of [[Text, Date... etc],[Text, ...]]
def tweetparse(file_name):
	with open(file_name, 'r') as f:
		readcsv = csv.reader(f)
		alldata = list(readcsv)
	
	tweets = []

	# allowable characters list
	chrallow = range(97,123)
	chrallow.extend(range(48,58))
	chrallow.extend([32,33,35,38,39,46,47,43,58,63,64,])

	separators = ['.','?','!']
	d = {':':'','.':'','&amp':'and'}

	# obtain list of words in tweets
	for i in alldata[1:len(alldata)]:
		i[0] = i[0].lower()
		i[0] = ''.join([k if ord(k) in chrallow else ' ' for k in i[0]])
		j = list(i[0].split(' '))
		words = []
		
		for n in j: # hyperlink control and sentance encoding
			if '/' in n and '.' in n:
				n = n[0:n.find('http')]
				n = n[0:n.find('pic.')]
			elif len(n) > 0 and n[-1] in separators:
				n = n[:-1] + '*'
			words.append(replace_all(n,d))
		
		words = filterblanks(words)
		sentences = list(' '.join(words).split('*'))
		sentences = filterblanks(sentences)
		senwords = []
		
		for o in sentences:
			words2 = list(o.split(' '))
			words2 = filterblanks(words2)
			senwords.append(words2)
		
		tweets.append(senwords)

	return tweets