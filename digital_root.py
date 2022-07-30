import math


def digital_root(n):
    n = [sum((n // (10 ** i)) % 10 for i in range(math.ceil(math.log(n, 10)) - 1, -1, -1))]
    total = 0
    for i in range(0, len(n)):
        total += n[i]
        if total > 9:
            total = digital_root(total)
    return total

#           OR
#     while n > 9:
#         n = sum(int(i) for i in str(n))
#     return n


print(digital_root(493193))
