import random
import string

def numbers(passlength):
    password = "".join(random.choice(string.digits) for _ in range(passlength))
    return password

def letters(passlength):
    password = "".join(random.choice(string.ascii_letters) for _ in range(passlength))
    return password

def both(passlength):
    both = string.digits + string.ascii_letters
    password = "".join(random.choice(both) for _ in range(passlength))
    return password
