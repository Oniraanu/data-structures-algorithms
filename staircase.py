def staircase(n):
    for i in range(1, n + 1):
        print(str("#" * i).rjust(n))


print(staircase(4))
