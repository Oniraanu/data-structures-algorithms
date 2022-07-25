import collections


def cut_sticks(sticks):
    count = 0
    if sticks:
        small_stick = min(sticks)
    else:
        return
    new_sticks = []
    for element in sticks:
        count = count + 1
        new_element = element - small_stick
        if new_element != 0:
            new_sticks.append(new_element)


print(cut_sticks([1, 2, 3]))
