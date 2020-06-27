my_list = [1,2,3]

another_list = [4,5,6]

new_list = [7,8,9]

print (len(my_list))

# list index
print(my_list[0])

# slice lists
print(my_list[1:])

# replace index
my_list[0] = 'one'

print (my_list + another_list)

# add to end of list
my_list.append('7')

print (my_list)

print (new_list)

# remove from end of list
# can also pop any index
popped_item = new_list.pop()

print (popped_item)


letter_list = ['a', 'l', 'c', 's']
num_list = [4,6,2,2,5,3]

# sort lists

letter_list.sort()
num_list.sort()
print (letter_list)
print (num_list)

# FLATTENED LOOPS

# append to list
my_string = 'hello'
# element for element
my_append = [x for x in my_string]

print (my_append)

# square every even number
lisst = [x**2 for x in range(0,11) if x % 2 == 0]

print (lisst)

# FIZZBUZZ
# fizz_list = []
# fizzbuzz = [x for x in range(0,101)]
#
# print (fizzbuzz)


# nested loops
nested = []
for x in [2,4,6]:
    for y in [100, 200, 300]:
        nested.append(x*y)

        print (nested)

# in one line nested lists
nested_flat = [x*y for x in [2,4,6] for y in [40,60,80]]

print (nested_flat)
