
def is_even(n):
    if n%2 == 0:
        return True
        # print(True)  **tested to make sure it DOESN'T work
    else:
        return False


def is_greater(x,y):
    return x>y


def myfunc(*args):
    out = []
    for num in args:
        if num%2==0:
            out.append(num)
    return out


def myfunc(x):
    out = []
    for i in range(len(x)):
        if i%2==0:
            out.append(x[i].lower())
        else:
            out.append(x[i].upper())
    return ''.join(out)


# volume of sphere

def vol(rad):
    return (4/3)*3.14*(rad**3)


def ran_check(num, low, high):
    if num in range(low, high+1):
        print('{num} is in range of low and high'.format(num='num'))
    else:
        print ('not in range')