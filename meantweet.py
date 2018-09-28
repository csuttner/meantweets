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
	for se_c, sentence in enumerate(tweet):
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
	# print t_len, tweet
		
numfin = float(numwords) / len(tweets)

# each element in outarr is an array of all of the body's ewords who's normalized indexes 
# fall into the range, sorted by highest to lowest total (sval sum)/sqrt(frequency of word in body)
# this seems to reasonably attenuate common words like the, and, is. 
outarr = []

for n in range(int(round(numfin))):
	inarr = []
	inwords = []
	# sandwich = ''
	# loop through the array of every word in the body's eword objects
	for o in wordsoup:
		# sandwich += o.word + ' '
		# if the normalized index of the word falls within the range of n to n+1
		if o.tnormindx < ((n+1)/float((int(round(numfin))))) and o.tnormindx >= (n/(float(int(round(numfin))))):
			if o.word not in inwords:
				inwords.append(o.word)
				inarr.append(o)
			else:
				for p in inarr:
					if p.word == o.word:
						p.tval += o.tval
	
	# once the bin is full, attenuate sval sums by dividing by the square root of total
	# occurances of that word in the entire body
	for r in inarr:
		r.tval = r.tval / math.log1p(uwords[r.word]+1)
	# sort
	inarr.sort(key = lambda x: x.tval, reverse = True)
	outarr.append(inarr)

# print sandwich

# printing the words with highest sval in respective slot, & runner upsx
for q in outarr:

	print q[0].word, q[0].tval, q[1].word, q[1].tval

