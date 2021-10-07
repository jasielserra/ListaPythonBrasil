def lazy_range(n):
    i = 0
    while i < n:
        yield i
        i += 1

def natural_numbers():
    """ retorna 1, 2, 3, ..."""
    i = 10
    while i > 0:
        yield i
        i -= 1

lazy_even_below_20 = (i for i in lazy_range(20) if i % 2 == 0)


print(list(lazy_range(10)))
print('=' * 30)
print(list(natural_numbers()))
print('=' * 30)
print(list(lazy_even_below_20))