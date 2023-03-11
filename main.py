import random

thing = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
amount = int(input())

final = ""
for i in range(amount):
    final += random.choice(thing)
print(final)
