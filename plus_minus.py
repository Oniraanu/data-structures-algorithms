def plusMinus(ar):
    count_greater = 0
    count_equal = 0
    count_less = 0
    for i in range(0, len(ar)):
        if ar[i] < 0:
            count_less += 1
        elif ar[i] == 0:
            count_equal += 1
        else:
            count_greater += 1
    a = count_less / len(ar)
    b = count_equal / len(ar)
    c = count_greater / len(ar)

    return print(f"{round(c, 6)}\n{round(a, 6)}\n{round(b, 6)}")


print(plusMinus([-4, 3, -9, 0, 4, 1]))

