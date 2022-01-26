
def is_prime(n):
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def primes():
    n = 3
    while True:
        if is_prime(n):
            yield n
        n += 1


def odd_composites():
    n = 2
    while True:
        if not is_prime(n) and n % 2 != 0:
            yield n
        n += 1


N = 5000


def solve():
    for odd_composite, _ in zip(odd_composites(), range(N)):
        i = 1
        waste_of_time = False
        while 2*i*i < odd_composite:
            if is_prime(odd_composite - 2*i*i):
                waste_of_time = True
                break
            i += 1
        if not waste_of_time:
            return odd_composite
