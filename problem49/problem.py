
def is_prime(n):
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def per_val(n):
    return int(''.join(sorted(str(n))))

def groupby(iterable, key=None):
    groups = {}
    for item in iterable:
        k = key(item)
        groups[k] = groups.get(k, [])
        groups[k].append(item)
    
    yield from groups.values()

def find_sequence(nums):
    num_set = set(nums)
    for num1 in nums:
        for num2 in nums:
            if num1 == num2:
                continue
            t1, t2, t3 = [None]*3
            if num1 > num2:
                t1, t2 = num2, num1
            else:
                t1, t2 = num1, num2
            t3 = t1 + 2*(t2-t1)
            if t3 in num_set:
                return t1, t2, t3

def solve():
    primes = [*filter(is_prime, range(1000, 10000))]
    groups = groupby(primes, key=per_val)
    filter1 = filter(lambda x: len(x) > 2, groups)
    results = filter(bool, map(find_sequence, filter1))
    for result in results:
        print(''.join(map(str, result)))


solve()
