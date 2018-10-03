import sys
import math
from cleaner import tweetparse
import matplotlib.pyplot as plt

tweets = tweetparse('obama.csv')
uwords = {}	
wordsoup = []
numwords = 0

for tweet in tweets:
	t_len = len(tweet)
	for t_inx, word in enumerate(tweet):
		wordsoup.append([word,t_inx/float(t_len),1/math.sqrt(t_len)])
		numwords += 1
		uwords[word] = uwords.get(word,0) + 1

avwords_int = int(round(numwords / len(tweets)))
avwords_fl = float(avwords_int)
outarr = []
outarr1 = []

for spot in range(avwords_int):
	indic = {}
	for werd in wordsoup:
		# if the normalized index of the word falls within the range of n to n+1
		if werd[1] < (spot+1)/avwords_fl and werd[1] >= spot/avwords_fl:
			indic[werd[0]] = indic.get(werd[0],0) + werd[2] 
	# once bin full, attenuate scores of common words
	for itm in indic:
		indic[itm] = indic[itm] ** (1/math.sqrt(uwords[itm]))
	# sort by attentuated score
	outarr.append(sorted(indic, key=indic.__getitem__, reverse = True)) 
	outarr1.append(sorted(indic, reverse = True))
# printing the words with highest sval in respective slot, & runner ups
printout = ''
x = []
y = []
for inx, q in enumerate(outarr):
	# printout += q[0] + ' '
	x.append(outarr1[inx])
	y.append(uwords[q[0]])
# print printout

print x
print y

plt.scatter(x,y)
plt.show()