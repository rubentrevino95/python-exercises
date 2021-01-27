from collections import Counter
from collections import defaultdict
from collections import namedtuple


numlist = [1, 1, 1, 2, 2, 3, 3]

c = Counter(numlist)

print(c.most_common(3))

print(list(c))


dictionary = {'a': 10}

print(dictionary['a'])

dictionary = defaultdict(lambda: 0)

dictionary['correct'] = 100

print(dictionary['correct'])

# similar to class attributes and class call
person = namedtuple('person',['age', 'gender', 'bloodtype'])

sammy = person(age= 21, gender= 'male', bloodtype= 'O-')

print(sammy)


# for x in range(0,100):
#     if x % 15 == 0:
#         print('fizzbuzz')
#     elif x % 5 == 0:
#         print('buzz')
#     elif x % 3 == 0:
#         print('fizz')
#     else:
#         print(x)