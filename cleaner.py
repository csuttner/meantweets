# Goal - obtain list of sentences, in the format of a list of words

# how do we scan for just words to trim out all of the special characters as efficiently as possible?

import csv

# function to split csv into tweets
def tweetparse(file_name):

	with open(file_name, 'r') as f:
		reader = csv.reader(f)
		tweetlist = list(reader)

	# return tweetlist

	testlist = []

	for i in tweetlist:

		testlist.append(len(i))

	return tweetlist

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

print tweetparse('Trump.csv')