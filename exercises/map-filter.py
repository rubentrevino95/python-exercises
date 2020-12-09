def square(num):
    return num**2

# lambda functions
square = lambda num: num**2

print(square(5))

my_nums = [1,2,3,4,5,6]

# map function requires a function in first arg and iterable in second arg
for item in map(square, my_nums):
    print(item)

# or use lambda
list(map(lambda num:num**2,mynums))

# to return the list
list(map(square, my_nums))


def splicer(mystring):
    if len(mystring) % 2 ==0:
        return 'EVEN'
    else:
        return mystring[0]

names = ['Tom', 'Jerry', 'Cat', 'CJ']

print(list(map(splicer, names)))

# filter

def check_even(num):
    return num % 2 == 0

for item in filter(check_even, my_nums):
    print(item)