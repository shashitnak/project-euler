from math import sqrt


def hexagonals():
    n = 144
    while True:
        yield n*(2*n-1)
        n += 1


def solve():
    for h in hexagonals():
        t = (sqrt(1+8*h) - 1) / 2
        if round(t) != t:
            continue
        p = (sqrt(1+24*h) + 1) / 6
        if round(p) != p:
            continue
        return h
