# for loops

numbers = [1,2,3,4,5,6,7,8,9]
for x in numbers:
    print (x)

# printing evens
for x in numbers:
    if x % 2 == 0:
        print (x)

# printing odds
for x in numbers:
    if x % 2 != 0:
        print (x)

# sum up numbers in list
sum_list = 0

for x in numbers:
    sum_list = sum_list + x
print (sum_list)

# tuples
# tuple unpacking
my_list = [(1,2),(3,4),(5,6)]
for a,b in my_list:
    print (a)
    print (b)


# looping dictionary

d = {'k1': 1, 'k2': 2, 'k3': 3}

for key,value in d.items():
    print (key)


#  WHILE LOOPS

x = 0

while x < 5:
    print ('the current value of x is {x}'.format(x= x))
    x = x + 1

else:
    print ('x is not less than 5')


num_set = [1,2,3]
# pass allows for nothing to be executed under loop
for x in num_set:
    pass


mystring = 'sammy'

for letter in mystring:
    if letter == 'a':
        continue
    print (letter)
# 'continue' goes to the top of closest enclosing loop
# 'break' will stop the loop


# for range operator
for x in range(3, 10):
    print (x)

# for loop counter
index_count = 0
word = 'abcde'

for letter in word:
    print (word[index_count])
    index_count +=1

# enumeration
# puts in form of tuples
word2 = 'fghijk'

for num, letter in enumerate(word2):
    print (num)
    print (letter)


my_list1 = [1,2,3]
my_list2 = ['a','b','c']

# zip lists together
print (zip(my_list1, my_list2))


# find items in lists
state = 'x' in ['x', 'y', 'z']

print (state)

# find values in dictionaries
dictionary = {'mykey': 345}
b = 345 in dictionary.values()
print (b)

# minimum value in list
my_list3 = [10,20,30,40,50,100]
print (min(my_list3))