"""Introduction to Lists
Lists are a datatype you can use to store a collection of different pieces of information as a sequence under a single variable name. (Datatypes you've already learned about include strings, numbers, and booleans.)

You can assign items to a list with an expression of the form

list_name = [item_1, item_2]
with the items in between brackets. A list can also be empty: empty_list = [].

Lists are very similar to strings, but there are a few key differences.

Instructions
The list zoo_animals has three items (check them out on line 1). Go ahead and add a fourth! Just enter the name of your favorite animal (as a "string") on line 1, after the final comma but before the closing ]."""

zoo_animals = ["pangolin", "cassowary", "sloth", "lemur" ];
# One animal is missing!

if len(zoo_animals) > 3:
	print "The first animal at the zoo is the " + zoo_animals[0]
	print "The second animal at the zoo is the " + zoo_animals[1]
	print "The third animal at the zoo is the " + zoo_animals[2]
	print "The fourth animal at the zoo is the " + zoo_animals[3]

"""Access by Index
You can access an individual item on the list by its index. An index is like an address that identifies the item's place in the list. The index appears directly after the list name, in between brackets, like this: list_name[index].

List indices begin with 0, not 1! You access the first item in a list like this: list_name[0]. The second item in a list is at index 1: list_name[1]. Computer scientists love to start counting from zero.

Instructions
Write a statement that prints the result of adding the second and fourth items of the list. Make sure to access the list by index!"""

numbers = [5, 6, 7, 8]

print "Adding the numbers at indices 0 and 2..."
print numbers[0] + numbers[2]
print "Adding the numbers at indices 1 and 3..."
# Your code here!
print numbers[1] + numbers[3]

"""New Neighbors
A list index behaves like any other variable name! It can be used to access as well as assign values.

You saw how to access a list index like this:

zoo_animals[0]
# Gets the value "pangolin"
You can see how assignment works on line 5:

zoo_animals[2] = "hyena"
# Changes "sloth" to "hyena"
Instructions
Write an assignment statement that will replace the item that currently holds the value "tiger" with another animal (as a string). It can be any animal you like."""

zoo_animals = ["pangolin", "cassowary", "sloth", "tiger"]
# Last night our zoo's sloth brutally attacked 
#the poor tiger and ate it whole.

# The ferocious sloth has been replaced by a friendly hyena.
zoo_animals[2] = "hyena"

# What shall fill the void left by our dear departed tiger?
# Your code here!
zoo_animals[3] = "lemur"

"""Late Arrivals & List Length
A list doesn't have to have a fixed length. You can add items to the end of a list any time you like!

letters = ['a', 'b', 'c']
letters.append('d')
print len(letters)
print letters
In the above example, we first create a list called letters.
Then, we add the string 'd' to the end of the letters list.
Next, we print out 4, the length of the letters list.
Finally, we print out ['a', 'b', 'c', 'd'].
Instructions
On lines 5, 6, and 7, append three more items to the suitcase list, just like the second line of the example above. (Maybe bring a bathing suit?)
Then, set list_length equal to the length of the suitcase list."""

suitcase = [] 
suitcase.append("sunglasses")

# Your code here!
suitcase.append("bathing suit")
suitcase.append("towel")
suitcase.append("last item")



list_length = len(suitcase) # Set this to the length of suitcase

print "There are %d items in the suitcase." % (list_length)
print suitcase

"""List Slicing
Sometimes, you only want to access a portion of a list.

letters = ['a', 'b', 'c', 'd', 'e']
slice = letters[1:3]
print slice
print letters
In the above example, we first create a list called letters.
Then, we take a subsection and store it in the slice list. We start at the index before the colon and continue up to but not including the index after the colon.
Next, we print out ['b', 'c']. Remember that we start counting indices from 0 and that we stopped before index 3.
Finally, we print out ['a', 'b', 'c', 'd', 'e'], just to show that we did not modify the original letters list.
Instructions
On line 4, create a list called middle containing only the two middle items from suitcase.
On line 5, create a list called last made up only of the last two items from suitcase."""

suitcase = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]

first  = suitcase[0:2]  # The first and second items (index zero and one)
middle =  suitcase[2:4]              # Third and fourth items (index two and three)
last   =  suitcase[4:6]              # The last two items (index four and five)

"""Slicing Lists and Strings
You can slice a string exactly like a list! In fact, you can think of strings as lists of characters: each character is a sequential item in the list, starting from index 0.

my_list[:2]
# Grabs the first two items
my_list[3:]
# Grabs the fourth through last items
If your list slice includes the very first or last item in a list (or a string), the index for that item doesn't have to be included.

Instructions
Assign to dog a slice of animals from index 3 up until but not including index 6.
Assign to frog a slice of animals from index 6 until the end of the string."""

animals = "catdogfrog"
cat  = animals[:3]   # The first three characters of animals
dog  = animals[3:6]              # The fourth through sixth characters
frog =    animals[6:]           # From the seventh character to the end

"""Maintaining Order
Sometimes you need to search for an item in a list.

animals = ["ant", "bat", "cat"]
print animals.index("bat")
First, we create a list called animals with three strings.
Then, we print the first index that contains the string "bat", which will print 1.
We can also insert items into a list.

animals.insert(1, "dog")
print animals
We insert "dog" at index 1, which moves everything down by 1.
We print out ["ant", "dog", "bat", "cat"]
Instructions
Use the .index(item) function to find the index of "duck". Assign that result to a variable called duck_index.
Then .insert(index, item) the string "cobra" at that index."""

animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index =  animals.index("duck")  # Use index() to find "duck"

# Your code here!

animals.insert(duck_index,"cobra")

print animals # Observe what prints after the insert operation

"""For One and All
If you want to do something with every item in the list, you can use a for loop. If you've learned about for loops in JavaScript, pay close attention! They're different in Python.

for variable in list_name:
    # Do stuff!
A variable name follows the for keyword; it will be assigned the value of each list item in turn.

Then in list_name designates list_name as the list the loop will work on. The line ends with a colon (:) and the indented code that follows it will be executed once per item in the list.

Instructions
Write a statement in the indented part of the for-loop that prints a number equal to 2 * number for every list item."""

my_list = [1,9,3,8,5,7]

for number in my_list:
    # Your code here
    print number * 2

"""More with 'for'
If your list is a jumbled mess, you may need to sort() it.

animals = ["cat", "ant", "bat"]
animals.sort()

for animal in animals:
    print animal
First, we create a list called animals with three strings. The strings are not in alphabetical order.
Then, we sort animals into alphabetical order. Note that .sort() modifies the list rather than returning a new list.
Then, for each item in animals, we print that item out as "ant", "bat", "cat" on their own line each.
Instructions
Write a for-loop that iterates over start_list and .append()s each number squared (x ** 2) to square_list.
Then sort square_list!"""

start_list = [5, 3, 1, 2, 4]
square_list = []

# Your code here!
for i in start_list:
    square_list.append(i ** 2)
square_list.sort()
print square_list

"""This Next Part is Key
A dictionary is similar to a list, but you access values by looking up a key instead of an index. A key can be any string or number. Dictionaries are enclosed in curly braces, like so:

d = {'key1' : 1, 'key2' : 2, 'key3' : 3}
This is a dictionary called d with three key-value pairs. The key 'key1' points to the value 1, 'key2' to 2, and so on.

Dictionaries are great for things like phone books (pairing a name with a phone number), login pages (pairing an e-mail address with a username), and more!

Instructions
Print the values stored under the 'Sloth' and 'Burmese Python' keys. Accessing dictionary values by key is just like accessing list values by index:

residents['Puffin']
# Gets the value 104"""

# Assigning a dictionary with three key-value pairs to residents:
residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}

print residents['Puffin'] # Prints Puffin's room number

# Your code here!
print residents['Sloth']
print residents['Burmese Python']

"""New Entries
Like Lists, Dictionaries are "mutable". This means they can be changed after they are created. One advantage of this is that we can add new key/value pairs to the dictionary after it is created like so:

dict_name[new_key] = new_value
An empty pair of curly braces {} is an empty dictionary, just like an empty pair of [] is an empty list.

The length len() of a dictionary is the number of key-value pairs it has. Each pair counts only once, even if the value is a list. (That's right: you can put lists inside dictionaries!)
Add at least three more key-value pairs to the menu variable, with the dish name (as a "string") for the key and the price (a float or integer) as the value. Here's an example:

menu['Spam'] = 2.50"""

menu = {} # Empty dictionary
menu['Chicken Alfredo'] = 14.50 # Adding new key-value pair
print menu['Chicken Alfredo']

# Your code here: Add some dish-price pairs to menu!
menu['Spam'] = 2.00
menu['Eggs'] = 3.00
menu['Python'] = 18.00
menu['Go'] = 100.00



print "There are " + str(len(menu)) + " items on the menu."
print menu

"""Changing Your Mind
Because dictionaries are mutable, they can be changed in many ways. Items can be removed from a dictionary with the del command:

del dict_name[key_name]
will remove the key key_name and its associated value from the dictionary.

A new value can be associated with a key by assigning a value to the key, like so:

dict_name[key] = new_value
Instructions
Delete the 'Sloth' and 'Bengal Tiger' items from zoo_animals using del.

Set the value associated with 'Rockhopper Penguin' to anything other than 'Arctic Exhibit'."""

# key - animal_name : value - location 
zoo_animals = { 'Unicorn' : 'Cotton Candy House',
'Sloth' : 'Rainforest Exhibit',
'Bengal Tiger' : 'Jungle House',
'Atlantic Puffin' : 'Arctic Exhibit',
'Rockhopper Penguin' : 'Arctic Exhibit'}
# A dictionary (or list) declaration may break across multiple lines

# Removing the 'Unicorn' entry. (Unicorns are incredibly expensive.)
del zoo_animals['Unicorn']

# Your code here!

del zoo_animals['Sloth']
del zoo_animals['Bengal Tiger']

zoo_animals["Rockhopper Penguin"] = 'Cotton Candy House'


print zoo_animals

"""Remove a Few Things
Sometimes you need to remove something from a list.

beatles = ["john","paul","george","ringo","stuart"]
beatles.remove("stuart")
print beatles
>> ["john","paul","george","ringo"]
We create a list called beatles with 5 strings.
Then, we remove the first item from beatles that matches the string "stuart". Note that .remove(item) does not return anything.
Finally, we print out that list just to see that "stuart" was actually removed.
Instructions
Remove 'dagger' from the list of items stored in the backpack variable.

?
"""

backpack = ['xylophone', 'dagger', 'tent', 'bread loaf']
backpack.remove("dagger")

"""It's Dangerous to Go Alone! Take This
Let's go over a few last notes about dictionaries

my_dict = {
    "fish": ["c", "a", "r", "p"],
    "cash": -4483,
    "luck": "good"
}
print my_dict["fish"][0]
In the example above, we created a dictionary that holds many types of values.
The key "fish" has a list, the key "cash" has an int, and the key "luck" has a string.
Finally, we print the letter 'c'. When we access a value in the dictionary like my_dict["fish"], we have direct access to that value. So we can access the item at index '0' in the list stored by the key "fish"
Instructions
Add a key to inventory called 'pocket'
Set the value of 'pocket' to be a list consisting of the strings 'seashell', 'strange berry', and 'lint'
.sort() the items in the list stored under the 'backpack' key
Then .remove('dagger') from the list of items stored under the 'backpack' key
Add 50 to the number stored under the 'gold' key"""

inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf'],
    'pocket' : ['seashell', 'strange berry', 'lint']
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort() 

# Your code here
inventory['backpack'].sort()
inventory['backpack'].remove('dagger')
inventory['gold'] = 550

# the following also works:

inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort() 

# Your code here
inventory['pocket'] = ['seashell', 'strange berry', 'lint']
inventory['backpack'].sort()
inventory['backpack'].remove('dagger')
inventory['gold'] = inventory['gold'] + 50