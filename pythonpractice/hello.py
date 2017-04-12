ar = []

x = 1000

for i in range(1,(x + 1)):

	for j in range(1,i):
		
		if (i % j > 0) == False:

			print (str(i) + " " + str(j) + " " + "no remainder")

			ar = ar + [i]

		elif (i % j > 0) == True:

			print (str(i) + " " + str(j) + " " + "remainder")

	print ar

