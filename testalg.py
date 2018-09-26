inpt = open('obama1.txt','U').read()


def remove_non_ascii_1(text):
	out = ''
	for i in text:
		if ord(i)<128:
			out = out + i
		else:
			out = out + ' '
        return out


d = {'"':'', '(':'',')':'','&amp;':'','\n':' ',',':' '}


def replace_all(text, dic):
    for p, q in dic.iteritems():
        text = text.replace(p,q)
    return text


stp = replace_all(remove_non_ascii_1(inpt),d)
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

new_file = open("new_file.txt", "w+")
new_file.write(output.replace(':', ''))

print 'ok'

# a = [1,2,3,4,5]

# b = a.pop(3)

# print a