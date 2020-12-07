import random

upper_case = "ABCDEFGHIJKL"
lower_case = upper_case.lower()
digits = "123456789"
symbols = ".,;$#@!"

upper,lower,num,sym = True,True,True,True

aall = ""

if upper:

    aall += upper_case

if lower:

    aall += lower_case

if num:

    aall += digits

if symbols:

    aall += symbols

length = 20

amount = 10

for x in range(amount):

    password = "".join(random.sample(aall,length))

    print(password)
