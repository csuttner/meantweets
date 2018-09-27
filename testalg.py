def cleanup(file_name):

	def remove_non_ascii_1(text):

		out = ''

		for i in text:

			if ord(i)<128:

				out = out + i

			else:

				out = out + ' '

		return out

	def replace_all(text,dic):

		for p,q in dic.iteritems():

			text = text.replace(p,q)

		return text

	d = {'"':'', '(':'',')':'','&amp;':'','\n':' ',',':' '}

	stp = replace_all(remove_non_ascii_1(open(file_name,'U').read()),d)

	sliced = list(stp.split(' '))

	output = ''

	for i in sliced:

		if i != '':

			if len(i) > 1 and i.count('.') == len(i) / 2:

				output = output + i.replace('.', '') + ' '

			elif i.count('.') > 1 and i.count('.') < len(i) and 'pic' not in i[0:i.find('.')]:

				i = i[0:i.find('.')]

				if '/' not in i:

					output = output + i + '. '
			
			elif '/' not in i:

				output = output + i + ' '

	return output.lower()	
	
	# open('Obama2.txt','w').write(output)