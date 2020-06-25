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
