# сортування вибором, slow

l = [5, 12, 14, 2, 3]


def min(l):
    m = l[0]
    for i in range(1, len(l)):
        if m >= l[i]:
            m = l[i]
    return m


def sort(l):
    res = []
    while len(l) > 0:
        a = min(l)
        res.append(a)
        l.remove(a)
    return res


print(sort(l))

