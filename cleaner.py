# Goal - obtain list of sentences, in the format of a list of words

# how do we scan for just words to trim out all of the special characters as efficiently as possible?

import csv
# import re

#splitting function for multiple delimiters
# def split(delimiters, string, maxsplit=0):
# 	regexPattern = '|'.join(map(re.escape, delimiters))
# 	return re.split(regexPattern, string, maxsplit)

# CSV -> List of [[Text, Date... etc],[Text, ...]]
def tweetparse(file_name):
	with open(file_name, 'r') as f:
		readcsv = csv.reader(f)
		alldata = list(readcsv)

	tweets = []

	chrallow = range(97,122)
	chrallow.extend(range(48,57))
	chrallow.extend([32,33,35,39,45,46,47,43,58,63,64])

	for i in alldata[1:len(alldata)]:
		i[0] = i[0].lower()
		i[0] = ''.join([k if ord(k) in chrallow else ' ' for k in i[0]])
		j = list(i[0].split(' '))
		j = filter(lambda a: a != '',j)
		tweets.append(j)
	
	return tweets

	# need to handle special chars, hyperlinks, and aconyms



	# def remove_non_ascii_1(text):

	# 	text = text.lower()

	# 	return ''.join([i if ord(i) < 128 else ' ' for i in text])

	# def replace_all(text,dic):

	# 	for p,q in dic.iteritems():

	# 		text = text.replace(p,q)

	# 	return text

	# d = {'"':'', '(':'',')':'','&amp;':'','\n':' ',',':' '}

	# stp = replace_all(remove_non_ascii_1(open(file_name,'U').read()),d)

	# sliced = list(stp.split(' '))

	# output = ''

	# for i in sliced:

	# 	if i != '':

	# 		if len(i) > 1 and i.count('.') == len(i) / 2:

	# 			output = output + i.replace('.', '') + ' '

	# 		elif i.count('.') > 1 and i.count('.') < len(i) and 'pic' not in i[0:i.find('.')]:

	# 			i = i[0:i.find('.')]

	# 			if '/' not in i:

	# 				output = output + i + '. ' 
			
	# 		elif '/' not in i:

	# 			output = output + i + ' '	
	
	# return output

print tweetparse('obama.csv')

print ord('d')