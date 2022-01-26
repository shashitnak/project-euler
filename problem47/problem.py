
def count_prime_factors(n):
    count = 0
    facts = []
    while n:
        i = 2
        while i*i <= n:
            if n % i != 0:
                i += 1
                continue
            count += 1
            facts.append(i)
            while n % i == 0:
                n //= i
            break
        else:
            if n != 1:
                facts.append(n)
                count += 1
            break
    return count, facts


def solve():
    n = 4
    pfs = [0, 1, 1]
    while True:
        count, facts = count_prime_factors(n)
        pfs.append(count)
        if n % 10000 == 0:
            print(n, count, facts)
        if pfs[-4:] == [4]*4:
            print(pfs[-4:])
            return n-3
        n += 1


print(solve())
