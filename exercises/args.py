# args & kwargs

def myfunc(a, b, c=0, d=0, e=0):
    return sum((a, b, c, d, e)) * 0.05

print(myfunc(40, 60))

# sets all parameters into tuples
def nfunc(*args):
    # for item in args
    # print(item)
    return (args)

print(nfunc(40, 60, 100, 1, 34))

# kwargs
def kwargs(**kwargs):
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I did not find ant fruit here')

kwargs(fruit='banana')

# def afunc(*args, **kwargs):
#     print(args)
#     print(kwargs)
#     print("I would like {} {}".format(args[0],kwargs['food']))

# afunc(10, 20, 30, fruit='fruit', fruit='eggs', animal='dog')