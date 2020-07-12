
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


def perfect_number(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n


print(perfect_number(6))


def pascal_triangle(n):
    trow = [1]
    y = [0]
    for x in range(max(n,0)):
        print(trow)
        trow=[l+r for l,r in zip(trow+y, y+trow)]
    return n>=1


pascal_triangle(6)


items=[n for n in input().split('-')]
items.sort()
print('-'.join(items))


def calculateSum(num):
    if num:
        return num + calculateSum(num-1)
    else:
        return 0


res = calculateSum(10)

print(res)