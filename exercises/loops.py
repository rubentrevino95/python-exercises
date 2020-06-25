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
