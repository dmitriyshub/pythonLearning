# my practise on CS50 2020 lecture 6 python
# link to lecture: https://www.youtube.com/watch?v=ZEQh45W_UDo&t=1420s

# ## python introduction ###

# in Python it is NECESSARY yo indent your code correctly by 4 spaces! YOU MUST DO SO! if not you will get a IndentationError !

print("Hello, world") # output something(in this case adding string Hello world) to console

# ## Variable: ###

string = "string" # declare str variable

"""
answer = input("What`s your name? ") # save the input answer in veriable called answer
print("Hello, " + answer + "!") # the + operator concatenate strings
"""

# ## Counter: ###

counter = 0 # declare int veriable

counter = counter + 1 # adiing 1 to counter
counter += 1 # also adding 1 to counter
print(counter)

# ## F-strings: (formated string) ###

# we can use curly braces to plug in a value of variable answer
# we also need insert the letter f in the beggining

"""
answer = input("What`s your name? ")
print(f"Hello, {answer}") 
"""

# ## Conditions: ###

x = 1
y = 2
if x < y:
    print("X is less than Y")
elif x > y: # else if :)
    print("X is greater than Y")
else:
    print("X is equal to Y")

# ## Loops: ###

# ## While loops ###

i = 0
while i < 3:
    print("1Hello, world")
    i += 1

# ## For loop ###

# for loop that says :
# 1#give me a variable i#
# 2#on the first iteration of the loop set i equal to 0#
# 3#on the second iteration set i equal to 1#
# 4# on the last iteration of this loop set i equal to 2 for me#

for i in [0,1,2]: # not a "Pythonic way"
    print("2Hello, World!")

# same for loop that uses a range function instead:
# this function will automatically generate for you a list of three values from 0 to 2
# and then python will itorate over those three values for you!

for i in range(3): # is a "Pythonic way"
    print("3Hello, world")

for i in range(0,101,2): # start in 0 stop in 101 in step by two (0, 2 ,4 ,6 ,8 and so on)
    print("4Hello, world")
# ## Types: ###

# Python is a loosely Typed language # C is a strongly Typed language
# in python the types also exicts but you can often infer them implicitly
# YOU DONT NEED TO DECLARE THE TYPES THE COMPUTER WILL DO IT FOR YOU :)

# ## Data Types: ###

bool # Boolean`s

float # Numbers with decimal point

int # Positive and negative numbers

str # Sring`s

# ## Sequence Data Types: ###

range # Data Type of sorts that give you back a range of values by default 0 on up based on the input you provide

list # List is a proper data Type that`s similar in spirit to arrays in C JS and more but with a small and important difference that list automatically resizes itself!

tuple # "like comma separated values" x and y or latitude and longitude coordinates

dict # Dictionaries allow you to store keys and values

set # Set is a collection of values like a,b,c or 1,2,3 without duplicates!

# ## Libraries ###

# we can import some libraries by typing [import library_name]
# or import only specific function by typing [from libray_name import function_name]

#Functions
# def for declare a function


words = set()

def check(word):
    if word.lower() in words:
        return True
    else:
        return False


def load(dictionary):
    file = open(dictionary, "r")
    for line in file:
        word.add(line.rstrip())
    file.close()
    return True


def size():
    return len(words)

def unload():
    return True


print(check("her"))
print(size())



