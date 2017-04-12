# BeFOR We Begin
# Before we begin our exercise, we should go over the Python for loop one more time. For now, we are only going to go over the for loop in terms of how it relates to lists and dictionaries. We'll explain more cool for loop uses in later courses.

# for loops allow us to iterate through all of the elements in a list from the left-most (or zeroth element) to the right-most element. A sample loop would be structured as follows:

# for x in a: 
#     # Do something for every x
# This loop will run all of the code in the indented block under the for x in a: statement. The item in the list that is currently being evaluated will be x. So running the following:

# for item in [1, 3, 21]: 
#     print item

# Instructions
# Use a for loop to print out all of the elements in the list names.

# names = ["dickwill","2edde","trvre","another","columbus"]
# for i in names:
# 	print i

"""This is KEY!
You can also use a for loop on a dictionary to loop through its keys with the following:

# A simple dictionary
d = {"foo" : "bar"}

for key in d: 
    print d[key]  # prints "bar" 
Note that dictionaries are unordered, meaning that any time you loop through a dictionary, you will go through every key, but you are not guaranteed to get them in any particular order."""

# webster = {
# 	"Aardvark" : "A star of a popular children's cartoon show.",
#     "Baa" : "The sound a goat makes.",
#     "Carpet": "Goes on the floor.",
#     "Dab": "A small amount."
# }

# for i in webster:
# 	print webster[i]

"""Control Flow and Looping
The blocks of code in a for loop can be as big or as small as they need to be.

While looping, you may want to perform different actions depending on the particular item in the list.

numbers = [1, 3, 4, 7]
for number in numbers: 
    if number > 6:
        print number
print "We printed 7."
In the above example, we create a list with 4 numbers in it.
Then we loop through the numbers list and store each item in the list in the variable number.
On each loop, if number is greater than 6, we print it out. So, we print 7.
Finally, we print out a sentence.
Make sure to keep track of your indentation or you may get confused!

Instructions
Like step 2 above, loop through each item in the list called a.
Like step 3 above, if the number is even, print it out. You can test if the item % 2 == 0 to help you out.
"""

# a = [0,1,2,3,4,5,6,7,8,9,10,11,12,13]

# for i in a:
# 	if a[i] % 2 == 0:
# 		print a[i]

"""Lists + Functions
Functions can also take lists as inputs and perform various operations on those lists.

def count_small(numbers):
    total = 0
    for n in numbers:
        if n < 10:
            total = total + 1
    return total

lost = [4, 8, 15, 16, 23, 42]
small = count_small(lost)
print small
In the above example, we define a function count_small that has one argument, numbers.
We initialize a variable total that we can use in the for loop.
For each item n in numbers, if n is less than 10, we increment total.
After the for loop, we return total.
After the function definition, we create an array of numbers called lost.
We call the count_small function, pass in lost, and store the returned result in small.
Finally, we print out the returned result, which is 2 since only 4 and 8 are less than 10.
Instructions
Write a function that counts how many times the string "fizz" appears in a list.

Write a function called fizz_count that takes a list x as input.
Create a variable count to hold the ongoing count. Initialize it to zero.
for each item in x:, if that item is equal to the string "fizz" then increment the count variable.
After the loop, please return the count variable.
For example, fizz_count(["fizz","cat","fizz"]) should return 2."""

# def fizz_count(x):
# 	count = 0
# 	for i in x:
# 		if i == "fizz":
# 			count = count + 1
# 	return count

"""String Looping
As we've mentioned, strings are like lists with characters as elements. You can loop through strings the same way you loop through lists! While we won't ask you to do that in this section, we've put an example in the editor of how looping through a string might work.

Instructions
Run the code to see string iteration in action!"""

# for letter in "Codecademy":
#     print letter
    
# # Empty lines to make the output pretty
# print
# print

# word = "Programming is fun!"
# for letter in word:
#     # Only print out the letter i
#     if letter == "i":
#         print letter

"""Your Own Store!
Okay—on to the core of our project.

Congratulations! You are now the proud owner of your very own Codecademy brand supermarket.

animal_counts = {
    "ant": 3,
    "bear": 6,
    "crow": 2
}
In the example above, we create a new dictionary called animal_counts with three entries. One of the entries has the key "ant" and the value 3.

Instructions
Create a new dictionary called prices using {} format like the example above.
Put these values in your prices dictionary, in between the {}:
"banana": 4,
"apple": 2,
"orange": 1.5,
"pear": 3
Yeah, this place is really expensive. (Your supermarket subsidizes the zoo from the last course.)"""

# prices = {
#     "banana": 4,
#     "apple": 2,
#     "orange": 1.5,
#     "pear": 3
# }

"""Investing in Stock
Good work! As a store manager, you’re also in charge of keeping track of your stock/inventory.

Instructions
Create a stock dictionary with the values below.

"banana": 6
"apple": 0
"orange": 32
"pear": 15
?
"""
# stock = {
#     "banana": 6,
#     "apple": 0,
#     "orange": 32,
#     "pear": 15
# }
