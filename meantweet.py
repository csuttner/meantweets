import math
from cleaner import tweetparse
from mtclasses import eword

tweets = tweetparse('obama.csv')	

uwords = {}	
wordsoup = []
numwords = 0
numsens = 0

# collect properties of every word with eword class
for tweet in tweets:
	t_len = sum(len(t) for t in tweet)
	tw_indx = 0
	for sentence in tweet:
		s_len = len(sentence)
		numsens += 1
		for wo_c, word in enumerate(sentence):
			wordsoup.append(eword(word,s_len,wo_c,t_len,tw_indx))
			numwords += 1
			tw_indx += 1
			if word not in uwords.keys():
				uwords[word] = 1
			else:
				uwords[word] += 1
		
wavg_int = int(round(float(numwords) / len(tweets)))

# each element in outarr is an array of all of the body's ewords who's normalized indexes 
# fall into the range, sorted by highest to lowest total adjusted score

outarr = []

for n in range(wavg_int):
	inarr = []
	inwords = []
	# loop through the array of every word in the body's eword objects
	for o in wordsoup:
		# if the normalized index of the word falls within the range of n to n+1
		if o.tnormindx < (n+1)/float(wavg_int) and o.tnormindx >= n/(float(wavg_int)):
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
	
	# sort
	inarr.sort(key = lambda x: x.tval, reverse = True)
	outarr.append(inarr)

# printing the words with highest sval in respective slot, & runner upsx
for q in outarr:
	print q[0].word, q[0].tval, q[1].word, q[1].tval, q[2].word, q[2].tval

