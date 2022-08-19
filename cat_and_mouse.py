def catAndMouse(x, y, z):
    a = z - x
    b = z - y
    if abs(a) > abs(b):
        return "Cat B"
    elif abs(a) < abs(b):
        return "Cat A"
    else:
        return "Mouse"


print(catAndMouse(33, 86, 59))