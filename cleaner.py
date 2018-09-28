# Cleans CSV and returns first column as 3D list of list of lists (tweets, sentences, words)

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
	chrallow.extend([32,33,38,39,45,46,47,43,58,63,])

	separators = ['.','?','!']
	d = {':':'','.':'','&amp':'and','-':'','!':''}

	# obtain list of words in tweets
	for i in alldata[1:len(alldata)]:
		i[0] = i[0].lower()
		i[0] = ''.join([k if ord(k) in chrallow else ' ' for k in i[0]])
		j = list(i[0].split(' '))
		words = []
		
		for n in j: # hyperlink control and sentence encoding
			if '/' in n and '.' in n:
				if 'http' in n:
					n = n[0:n.find('http')]
				elif 'pic.' in n:
					n = n[0:n.find('pic.')]
			elif len(n) > 1 and n[-1] in separators:
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