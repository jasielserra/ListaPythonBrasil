from random import shuffle

n = list(range(10))
shuffle(n)
print(n)

n.sort(reverse=True)
print(n)