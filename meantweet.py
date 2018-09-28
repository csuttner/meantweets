import math

import time

from cleaner import cleanup

from mtclasses import eword

start_time = time.time()

# define splitting function that works for multiple delimiters at once
def split(delimiters, string, maxsplit=0):
    
    regexPattern = '|'.join(map(re.escape, delimiters))
    
	return re.split(regexPattern, string, maxsplit)

# assigning a variable inpt to the string of characters in the text file
# use this function to split inpt (string) into list of sentences 
sentences = split('.!?', cleanup('Obama.txt'))

# spaces will exist in front of the first word of every 2nd+ sentance, so creating a blank array to fill with fixed versions
fixedsentences = [] 
					
# set up loop through all elements of the 'sentences' list
for i in sentences: 

	# skip over all elements that are just '' or ' '
	if i != '' and i != ' ': 

		# if the first element in the sentence is a space...
		if i[0] == ' ':

			# add this sentence from index 1 over to the end of the blank array (list)
			fixedsentences.append(i[1:])

		else:

			# add this sentence to the end of the blank array (list)
			fixedsentences.append(i)

print 1, round(time.time() - start_time)

# create blank array to fill with 'eword' objects
mainarr = []	

# create blank array that will be filled with just one instance of each unique word in the entire body
wordsarr = {}	

numwords = 0

# for each sentence j within the fixed sentences
for j in fixedsentences: 

	# set the element equal to an array split with the delimiter ' '
	j = filter(lambda a: a != '',list(j.split(' ')))

	lenj = float(len(j))

	# fill wordsarr with one instance of each unique word
	for countindx, k in enumerate(j):

		mainarr.append(eword(k,lenj,countindx))

		if k not in wordsarr.keys():

			wordsarr[k] = 1

		else:

			wordsarr[k] += 1

	# varaiable to hold avg # words/sentence
	numwords += lenj

# obtain the average number of words per sentence
# rounding this up will obtain the number of slots to be filled in the final output
numfin = numwords / len(fixedsentences)

print 2, round(time.time() - start_time)

# this is the final list, the length of which will be the average number of words in 
# the body's sentences. each element in this list will be an array of all of the body's 
# ewords who's normalized indexes fall into the range, sorted by highest to lowest total
# (sval sum)/sqrt(frequency of word in body). this seems to reasonably attenuate common 
# words like the, and, is. 
outarr = []

# loop from 0 : rounded average number of words per sentence
for n in range(int(round(numfin))):

	# blank array to be appended to outarr
	inarr = []

	# unique word array per n to allow summing of svals per each unique word in slot n
	inwords = []

	# loop through the array of every word in the body's eword objects
	for o in mainarr:

		# if the normalized index of the word falls within the range of n to n+1
		if o.normindx < ((n+1)/float((int(round(numfin))))) and o.normindx >= (n/(float(int(round(numfin))))):

			# if this word hasn't appeared in the loop before
			if o.word not in inwords:

				# add the word itself to the list of unique words appearing in this slot
				inwords.append(o.word)

				# add the corresponding eword object to the slot's eword list
				inarr.append(o)

			# if o's word has appeared already in loop n
			else:

				# add the the sval of this word to inarr's existing instance of the word
				for p in inarr:

					if p.word == o.word:

						p.sval += o.sval	

	# once the bin is full, attenuate sval sums by dividing by the square root of total
	# occurances of that word in the entire body
	for r in inarr:

		# using math.sqrt as ** (1/2) doesn't seem to yeild the same result
		r.sval = r.sval / math.sqrt(wordsarr[r.word])

	# now that the final scores have been calculated, sort inarr from highest to lowest based
	# on the eword property
	inarr.sort(key = lambda x: x.sval, reverse = True)

	# add this array to the outer array
	outarr.append(inarr)

print 3, round(time.time() - start_time)

# printing the words with highest sval in respective slot, along with the runner ups
# for context
for q in outarr:

	print q[0].word

