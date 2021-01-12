 
def hello(name='Ben'):
    print('Hello() function has been executed')

    def greet():
        return 'greet() func inside hello'

    def welcome():
        return 'This is welcome() inside hello'

    if name == 'Ben':
        return greet
    else:
        return welcome

my_new_func = hello('Ben')

print(greet())
print(welcome())

def cool():

    def super_cool():
        return 'woah!'
    
    return super_cool

print(some_func = cool())

def new_decorator(original_func):
    def wrap_func():
        print('extra code goes here')

        original_func()
        print('extra code goes here too')

    return wrap_func 





