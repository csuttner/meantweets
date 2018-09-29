import math
from cleaner import tweetparse
from mtclasses import eword

tweets = tweetparse('Obama.csv')	

uwords = {}	
wordsoup = []
numwords = 0

# collect properties of every word with eword class
for tweet in tweets:
	t_len = sum(len(t) for t in tweet)
	t_inx = 0
	for sentence in tweet:
		s_len = len(sentence)
		for count, word in enumerate(sentence):
			wordsoup.append(eword(word,s_len,count,t_len,t_inx))
			numwords += 1
			t_inx += 1
			if word not in uwords.keys():
				uwords[word] = 1
			else:
				uwords[word] += 1
		
avw_int = int(round(numwords / len(tweets)))
avw_fl = float(avw_int)

# each element in outarr is an array of all of the body's ewords who's normalized indexes 
# fall into the range, sorted by highest to lowest total adjusted score

outarr = []

for n in range(avw_int):
	inarr = []
	inwords = []
	# loop through the array of every word in the body's eword objects
	for o in wordsoup:
		# if the normalized index of the word falls within the range of n to n+1
		if o.tnormindx < (n+1)/avw_fl and o.tnormindx >= n/avw_fl:
			if o.word not in inwords:
				inwords.append(o.word)
				inarr.append(o)
			else:
				for p in inarr:
					if p.word == o.word:
						p.tval += o.tval
	 
	# once bin full, attenuate scores of common words
	for r in inarr:
		r.tval = r.tval ** (1/math.sqrt(uwords[r.word]))
	
	# sort by attentuated score
	inarr.sort(key = lambda x: x.tval, reverse = True)
	outarr.append(inarr)

# printing the words with highest sval in respective slot, & runner ups
for q in outarr:
	print q[0].word, q[0].tval, q[1].word, q[1].tval, q[2].word, q[2].tval

