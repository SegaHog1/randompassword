import random

thing = "arel"
thing = "tails"
amount = int(input())

final = ""
for i in range(amount):
    final += random.choice(thing)
print(final)
