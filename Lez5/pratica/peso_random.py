import random

animali = ['gatto', 'papagallo', 'leone', 'cane', 'criceto']

c = random.choices(animali, k=10, weights=[10, 10, 5, 2, 1])

print(c)

