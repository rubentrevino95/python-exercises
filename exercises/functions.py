# write a function that returns true if a two worded string matches both beginning letters, false if not


def letter_match(text):
    wordlist = text.lower().split()

    return wordlist[0][0] == wordlist[1][0]


print (letter_match('Python practice'))


def makes20(a, b):
    if a + b == 20:
        return True
    elif a == 20 or b == 20:
        return True
    else:
        return False


print (makes20(4, 15))


def add_function(a, b):
    return a + b


result = add_function(2, 3)

print (result)


def sub_function(a, b):
    return a - b


result2 = sub_function(2, 3)

print (result2)


def mult_function(a, b):
    return a*b


result3 = mult_function(9, 8)

print (result3)


def div_function(a, b):
    return a / b


result4 = div_function(24, 4)

print (result4)