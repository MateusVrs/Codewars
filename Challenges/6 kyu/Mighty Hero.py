from math import factorial


def count_of_heads(initial, n, swings):
    for v in range(1, swings+1):
        initial = initial - 1 + (factorial(v)*n)
    return initial
