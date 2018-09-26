# "MoSt AvErAgE sEnTeNcE"

import math

import sys

# assigning a variable inpt to the string of characters in the text file
inpt = open(sys.argv[1],'r').read()

# define splitting function that works for multiple delimiters at once
def split(delimiters, string, maxsplit=0):
    
    import re
    
    regexPattern = '|'.join(map(re.escape, delimiters))
    
    return re.split(regexPattern, string, maxsplit)

# use this function to split inpt (string) into list of sentences 
sentences = split('.!?', inpt) 

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

# printing out the list at this point for error checking purposes
print fixedsentences 

# create blank array who's elements will be arrays of words in each sentance
mainarr = []	

# create blank array that will be filled with just one instance of each unique word in the entire body
wordsarr = []	

# create blank array pslenarr that will be the length of each sentence
pslenarr = []

# for each sentence j within the fixed sentences
for j in fixedsentences: 

	# set the element equal to an array split with the delimiter ' '
	j = filter(lambda a: a != '',list(j.split(' ')))

	# add this list as an element in mainarr
	mainarr.append(j)

	# add the length of the list (sentence length) 
	pslenarr.append(len(j))

	# fill wordsarr with one instance of each unique word
	for k in j:

		if k not in wordsarr:

			wordsarr.append(k)

# obtain the average number of words per sentence
# rounding this up will obtain the number of slots to be filled in the final output
numfin = float(sum(pslenarr)) / len(fixedsentences)

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
		self.normindx = float(psindx) / pslen
		self.sval = 1 / float(pslen)

# create blank array to fill with 'eword' objects
ewordarr = []

# loop through each sentence l in mainarr
for l in mainarr:

	# variable to hold index of word within parent sentence
	countindx = 0

	# loop through each word m in sentence l
	for m in l:

		# add a new eword object with word string = m, parent sentence length len(l),
		# and parent sentence index equal to the counter that resets each new sentence
		ewordarr.append(eword(m,len(l),countindx))
		countindx += 1

# create blank dictionary to capture the frequency of each unique word in entire body
freqarr = {}

# for each unique word
for r in wordsarr:

	# variable to hold number of occurances of the unique word
	counts = 0

	# count the number of occurances of the unique word r within array of every word
	for s in ewordarr:

		if s.word == r:

			counts += 1

	# create a key-value pair in freqarr equal to the unique word : total occurances in body
	freqarr[r] = counts

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
	for o in ewordarr:

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

	# check:
	# print n/numfin, o.normindx, (n+1)/float(int(round(numfin))), o.word, inwords

	# once the bin is full, attenuate sval sums by dividing by the square root of total
	# occurances of that word in the entire body
	for r in inarr:

		# check:
		# print r.word, r.sval, freqarr[r.word]

		# using math.sqrt as ** (1/2) doesn't seem to yeild the same result
		r.sval = r.sval / math.sqrt(freqarr[r.word])

		# check:
		# print r.sval

	# now that the final scores have been calculated, sort inarr from highest to lowest based
	# on the eword property
	inarr.sort(key = lambda x: x.sval, reverse = True)

	# add this array to the outer array
	outarr.append(inarr)

	# check:
	# print inarr[0].word, inarr[0].sval, inarr[0].normindx

# printing the words with highest sval in respective slot, along with the runner ups
# for context
for q in outarr:

	print q[0].word, q[0].sval, q[1].word, q[1].sval









