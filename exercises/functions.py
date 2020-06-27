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