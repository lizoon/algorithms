import random


def test(gcd, n_iter=100):
    for i in range(n_iter):
        c = random.randint(0, 1024)
        a = c * random.randint(0, 128)
        b = c * random.randint(0, 128)
        assert gcd(a, a) == gcd(a, 0) == a
        assert gcd(b, b) == gcd(b, 0) == b
        assert gcd(a, 1) == gcd(b, 1) == 1
        d = gcd(a, b)
        assert a % d == b % d == 0


def gcd1(a, b):
    assert a >= 0 and b >= 0
    for d in reversed(range(1, max(a, b) + 1)):
        if a % d == b % d == 0:
            return d


# algo evklid

def gcd2(a, b):
    while a and b:
        if a > b:
            a -= b
        if b > a:
            b -= a
    return max(a, b)


def gcd3(a, b):
    assert a >= 0 and b >= 0
    if a == 0 or b == 0:
        return max(a, b)
    elif a >= b:
        return gcd3(a % b, a)
    elif b >= a:
        return gcd3(b % a, b)


def gcd4(a, b, c, d):
    assert a >= 0 and b >= 0

    while a != c and b != d:
        if a == 0 or b == 0:
            return 'NO'
        return gcd4(b % a, a, c, d)
    return 'YES'


if __name__ == '__main__':
    k = int(input())
    while k:
        a, b, c, d = int(input()), int(input()), int(input()), int(input())
        print(gcd4(a, b, c, d))
