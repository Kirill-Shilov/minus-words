from minus.minus import *
import random
import string
def rnd(a):
    b = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(a)])
    return(b)
minus_set = set()

for word in range(100):
    minus_set.add(rnd(7))

will_be_removed = set()

for word in minus_set:
    wrd = f"{rnd(3)}{word}{rnd(4)}"
    will_be_removed.add(wrd) 

half_safe_set = set()

for word in range(100):
    half_safe_set.add(rnd(14))

safe_set = half_safe_set - will_be_removed
fake_input = safe_set | will_be_removed

minus_test = Minus_words(fake_input, will_be_removed)
filtered = set(minus_test.minus())

assert safe_set == filtered
print("OK")
