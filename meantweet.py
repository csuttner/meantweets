import math
from cleaner import tweetparse
from mtclasses import eword

start_time = time.time()

tweets = tweetparse('Obama.csv')	

uwords = {}	
wordsoup = []
numwords = 0
numsens = 0

for tw_c, tweet in enumerate(tweets): 
	for sentance in tweet:
		s_len = len(sentance)
		numsens += 1
		for wo_c, word in enumerate(sentance):
			wordsoup.append(eword(word,s_len,wo_c))
			numwords += 1
			if word not in uwords.keys():
				uwords[word] = 1
			else:
				uwords[word] += 1
		
numfin = float(numwords) / numsens

# this is the final list, the length of which will be the average number of words in 
# the body's sentences. each element in this list will be an array of all of the body's 
# ewords who's normalized indexes fall into the range, sorted by highest to lowest total
# (sval sum)/sqrt(frequency of word in body). this seems to reasonably attenuate common 
# words like the, and, is. 
outarr = []
sandwich = ''

for n in range(int(round(numfin))):
	inarr = []
	inwords = []
	# loop through the array of every word in the body's eword objects
	for o in wordsoup:
		sandwich += o.word + ' '
		# if the normalized index of the word falls within the range of n to n+1
		if o.normindx < ((n+1)/float((int(round(numfin))))) and o.normindx >= (n/(float(int(round(numfin))))):
			if o.word not in inwords:
				inwords.append(o.word)
				inarr.append(o)
				
			else:
				for p in inarr:
					if p.word == o.word:
						p.sval += o.sval	
	
	# once the bin is full, attenuate sval sums by dividing by the square root of total
	# occurances of that word in the entire body
	for r in inarr:
		r.sval = r.sval / math.sqrt(uwords[r.word])
	# sort
	inarr.sort(key = lambda x: x.sval, reverse = True)
	outarr.append(inarr)

# print sandwich

# printing the words with highest sval in respective slot, along with the runner ups
# for context
for q in outarr:

	print q[0].word, q[0].sval, q[1].word, q[1].sval

