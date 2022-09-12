# recurcy factorial
def fact(n):
    if n == 1:
        return 1
    return n*fact(n-1)


# print(fact(3))


# recurcy sum
def sum(l):
    if len(l) == 1:
        return l[0]
    elif len(l) == 0:
        return 0
    return l[0]+sum(l[1:])


# print(sum([1, 2, 3, 4, 6, 10]))


# recurcy count
def count(l):
    if len(l) > 1:
        return 1 + count(l[1:])
    return 1


# print(count([1, 2, 3, 4, 5, 6, 7, 8]))


# recurcy max
def max(l):
    if len(l) == 1:
        return l[0]
    elif len(l) == 0:
        return 0
    if l[0] < l[1]:
        return max(l[1:])
    else:
        l.remove(l[1])
        return max(l)


# print(max([1, 6, 3, 10, 5]))


# binary search

def bsearch(list, idx0, idxn, val):
    if (idxn < idx0):
        return None
    else:
        midval = idx0 + ((idxn - idx0) // 2)
        # Compare the search item with middle most value

        if list[midval] > val:
            return bsearch(list, idx0, midval - 1, val)
        elif list[midval] < val:
            return bsearch(list, midval + 1, idxn, val)
        else:
            return midval


list = [8, 11, 24, 56, 88, 131]
print(bsearch(list, 0, len(list), 24))
print(bsearch(list, 0, len(list), 0))
