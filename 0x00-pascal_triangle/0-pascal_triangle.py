#!/usr/bin/python3
# Pascal's Triangle


def pascal_triangle(n):
    # A function that returns a list of integers
 #   if n <= 0:
#        return []

    # Initializes pascal's triangle with the first row
    lists = []
    if n == 0:
        return lists
    for i in range(n):
        lists.append([])
        lists[i].append(1)
        if (i > 0):
            for j in range(1, i):
                lists[i].append(lists[i - 1][j - 1] + lists[i - 1][j])
            lists[i].append(1)
    return lists
