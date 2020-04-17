                # otp creation in python

import random,string
from random import choices
for i in range(0,10):
    print("The Otp is:",random.randrange(1000,9999))



                # creating an otp of both alphabets and nummbers
size=10
for number in range(0,10):
    l=[]
    for i in range(0,10):
        l.append(random.choice(string.ascii_letters+string.digits))
    l="".join(l)
    print('number:',l)

