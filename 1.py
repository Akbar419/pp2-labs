#py : home : intro : get started:

print("Hello, World!") 

#syntax : 

if 5 > 2:
  print("Five is greater than two!")

#syntax error:

if 5 > 2:
print("Five is greater than two!")

#the number of space is up to you : 

if 5 > 2:
 print("Five is greater than two!") 
if 5 > 2:
        print("Five is greater than two!") 

#the same of code have to be in the same block of code :

if 5 > 2:
 print("Five is greater than two!") 
if 5 > 2:
        print("Five is greater than two!") 

#comment starts with # this sign :

#This is a comment
print("Hello, World!")

#it can be placed anywhere :

print("Hello, World!") #This is a comment

#comment doesn't have to be a explaining of code :

#print("Hello, World!")
print("Cheers, Mate!")

#variable is created when give a value for it :

x = 5
y = "John"
print(x)
print(y)

#we can easily change the type of the variable :

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

#it is easy to clasify the data, if you want: 

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#a variable name rules : 
#1. A variable name must start with a letter or the underscore character
#2. A variable name cannot start with a number
#3. A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
#4. Variable names are case-sensitive (age, Age and AGE are three different variables)
#5. A variable name cannot be any of the Python keywords.

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#illegal varibale names:

2myvar = "John"
my-var = "John"
my var = "John"

#python allows to assign multiple values:

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#also you can assign the same value to multiple variables : 

x = y = z = "Orange"
print(x)
print(y)
print(z)

#collection of values called list or tuple, you can so extract the values into variables, this is called unpacking :

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# print() function is used to output the values : 

x = "Python is awesome"
print(x)

#you can also output multiple values by using comma :

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

#you can use "+" to output multiple values :

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

#for the numbers + is used like operation + :

x = 5
y = 10
print(x + y)

#but is you use + with string and integer you will see an error:

x = 5
y = "John"
print(x + y)

#on the other hand comma can be used for outputing different data types :

x = 5
y = "John"
print(x, y)

# if you create a value outside it will be called "global variable" the the function you can use it in the in function :

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#and you also can create the variable with the same name in the function and it would be a "local variable" :

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

#data types in python: you can use function "type()" to see which data type is the variable :

x = 5
print(type(x))

#data type is set when you assign the varible in python:

x = "Hello World"	str	
x = 20	int	
x = 20.5	float	
x = 1j	complex	
x = ["apple", "banana", "cherry"]	list	
x = ("apple", "banana", "cherry")	tuple	
x = range(6)	range	
x = {"name" : "John", "age" : 36}	dict	
x = {"apple", "banana", "cherry"}	set	
x = frozenset({"apple", "banana", "cherry"})	frozenset	
x = True	bool	
x = b"Hello"	bytes	
x = bytearray(5)	bytearray	
x = memoryview(bytes(5))	memoryview	
x = None	NoneType

#if you want to specify data type you can use the following constructor functions : 

x = str("Hello World")	str	
x = int(20)	int	
x = float(20.5)	float	
x = complex(1j)	complex	
x = list(("apple", "banana", "cherry"))	list	
x = tuple(("apple", "banana", "cherry"))	tuple	
x = range(6)	range	
x = dict(name="John", age=36)	dict	
x = set(("apple", "banana", "cherry"))	set	
x = frozenset(("apple", "banana", "cherry"))	frozenset	
x = bool(5)	bool	
x = bytes(5)	bytes	
x = bytearray(5)	bytearray	
x = memoryview(bytes(5))	memoryview	

#numeric types of values are created when you assign the variable :

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#to varify which data type is it use the same "type()" function :

print(type(x))
print(type(y))
print(type(z))

#casting in python:

 #"int()" constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number):
 
 x = int(1)   # x will be 1
 y = int(2.8) # y will be 2
 z = int("3") # z will be 3
 
 #"float()" constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
 
 x = float(1)     # x will be 1.0
 y = float(2.8)   # y will be 2.8
 z = float("3")   # z will be 3.0
 w = float("4.2") # w will be 4.2

 #"str()" constructs a string from a wide variety of data types, including strings, integer literals and float literals

 x = str("s1") # x will be 's1'
 y = str(2)    # y will be '2'
 z = str(3.0)  # z will be '3.0'

#Strings: in python you can either single quotation or double quotation marks:

print("Hello")
print('Hello')

#you can use the quotes as long as  they don't match the quotes surrounding the string:

print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

#in python you set string by using "=" sign:

a = "Hello"
print(a)

#you can also assign multiline string by using triple quote:

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#or three single quotes:

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

#you can specify the start index and the end index, separated by a colon, to return a part of the string :

bb = "Hello, World!"
print(b[2:5])

#also you can right it like this and you will get the positions from start to the second number you wrote : 

b = "Hello, World!"
print(b[:5])

#and to the end by writing klike this:

b = "Hello, World!"
print(b[2:])

#you can use negative indexes like this :

b = "Hello, World!"
print(b[-5:-2])

#".upper()" is used to make the string uppercase:

a = "Hello, World!"
print(a.upper())

#".lower()" is used to make the strings lowercase:

a = "Hello, World!"
print(a.lower())

#"strip()" is used to remove any whitespace from beginning to the end :

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

#to concatenate strings for example merge a and be into c:

a = "Hello"
b = "World"
c = a + b
print(c)

#to add space between you need to use a " ":

a = "Hello"
b = "World"
c = a + " " + b
print(c)

#we cannot combine strings and numbers like this:

age = 36
txt = "My name is John, I am " + age
print(txt)

#that's why we have f-strings in python when we use them we write f before the string and then we use curly brakets "{}" for variables :

age = 36
txt = f"My name is John, I am {age}"
print(txt)

#Place holders and modifiers: a placeholder can contain variables, operations, functions, and modifiers to format the value:

price = 59
txt = f"The price is {price} dollars"
print(txt)

#we use .2f when we need to output the fixed point number with 2 decimals and etc.:

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

#a placeholder can contain a python code like mathematical oparetions:

txt = f"The price is {20 * 59} dollars"
print(txt)

#you will get an error if you use a double quotes in the string:

txt = "We are the so-called "Vikings" from the north."

#instead you can use a escape character to allow it by using the '\"' sign:

txt = "We are the so-called \"Vikings\" from the north."

#escape characters:

\'	Single Quote	
\\	Backslash	
\n	New Line	
\r	Carriage Return	
\t	Tab	
\b	Backspace	
\f	Form Feed	
\ooo	Octal value	
\xhh	Hex value

#single methods in python

capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isascii()	Returns True if all characters in the string are ascii characters
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning

