# Cleans CSV and returns first column as 3D list of list of lists (tweets, sentences, words)
import csv
import re
import numpy as np
from mtclasses import replace_all, filterblanks

# CSV -> List of [[Text, Date... etc],[Text, ...]]
def tweetparse(file_name):
	with open(file_name, 'r') as f:
		readcsv = csv.reader(f)
		alldata = list(readcsv)[1:]
	
	tweets = []

	# allowable characters list
	chrallow = range(97,123)
	chrallow.extend(range(48,58))
	chrallow.extend([32,33,38,39,45,46,47,43,58,63])

	separators = ['.','?','!']
	d = {':':'','.':'','&amp':'and','-':'','!':''}

	# obtain list of words in tweets
	for row in alldata:
		tweetxt = row[0].lower()
		tweetxt = ''.join([char if ord(char) in chrallow else ' ' for char in tweetxt])
		tweetxt = list(tweetxt.split(' '))
		wordlist = []
		for word in tweetxt: # hyperlink control and sentence encoding
			if '/' in word and '.' in word:
				if 'http' in word:
					word = word[0:word.find('http')]
				elif 'pic.' in word:
					word = word[0:word.find('pic.')]
			elif len(word) > 1 and word[-1] in separators:
				word = word[:-1] + '*'
			wordlist.append(replace_all(word,d))
		wordlist = filterblanks(wordlist)
		sentences = list(' '.join(wordlist).split('*'))
		sentences = filterblanks(sentences)
		senwords = []

		for o in sentences:
			words2 = list(o.split(' '))
			words2 = filterblanks(words2)
			senwords.append(words2)
		if senwords != []:
			tweets.append(np.concatenate(senwords))

	return tweets