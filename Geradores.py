def lazy_range(n):
    i = 0
    while i < n:
        yield i
        i += 1



print(list(lazy_range(10)))