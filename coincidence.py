from Integer import Integer

n = 0
n0 = 0
for i in range(1_000, 10_000):
    n0 += 1
    if Integer(i).is_prime and i % 10 == 7:
        n += 1
        print(n / n0, i)
