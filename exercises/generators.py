def create_cubes(n):
    for x in range(n):
        yield x**3

for x in create_cubes(10):
    print(x)

print(list(create_cubes(10)))

def gen_fibon(n):

    a = 1
    b = 1
    output = []

    for i in range(n):
        output.append(a)
        a,b = b,a+b

for num in gen_fibon(10):
    print(num)


print(list(gen_fibon(10)))


def simple_gen():
    for x in range(3):
        yield x

for num in simple_gen():
    print(num)

g = simple_gen()

print(next(g))