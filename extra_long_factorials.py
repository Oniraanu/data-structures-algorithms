import math


def extra_factorial(number):
    multiplier = 1
    if number <= 1:
        return number
    else:
        for i in range(1, number + 1):
            multiplier *= i
        return multiplier

    #           OR

    # if number == 1:
    #     return 1
    # else:
    #     multiplier = math.factorial(number)
    # return multiplier


print(extra_factorial(25))
