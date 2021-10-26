import random

#four_uniform_randoms = [random.random() for _ in range(4)]

four_with_replacement = [random.choice(range(100)) for _ in range(4)]


print(four_with_replacement)