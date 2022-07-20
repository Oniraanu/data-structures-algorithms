def find_smaller_number(lst):
    # smallest is initialised to the item in the first index of the list.
    # smallest index is also initialised to first index
    smallest = lst[0]
    smallest_index = 0
    # loop through the list
    # if any item in the list is less than the initialised smallest, it takes the place of the smallest until the items
    # in the list has been exhausted.
    for i in range(0, len(lst) - 1):
        if lst[i] < smallest:
            smallest = lst[i]
            smallest_index = i
    return smallest_index


def selection_sort(lst):
    # create a new list to store the ordered items
    new_lst = []
    # loop through the old list
    for i in range(len(lst)):
        # smallest = find_smaller_number(lst)
        # new_lst.append(lst.pop(smallest))
        # --------------------------------------------
        # use the find_smaller_number function defined above to find the smallest number
        # pop it out of the list and append to new_lst
        new_lst.append(lst.pop(find_smaller_number(lst)))
    return new_lst


print(find_smaller_number([5, 7, 1, 3, 9, 2, 17]))
print(selection_sort([5, 7, 1, 3, 9, 2, 17]))
