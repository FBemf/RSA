# Implementation of Euclidean Algorithm

# Euclidean Algorithm
def gcf(a, b):

    # Make this straightforward, a>=b
    if (b > a):
        c = a
        a = b
        b = c

    r=1
    q=0
    while not (r == 0):
        q = a // b
        r = a - q*b
        # a = qb + r
        #print(str(a) + "=" + str(q) + "*" + str(b) + " + " + str(r))
        a = b
        b = r
    return a

def lcm(a, b):
    return (a * b) // gcf(a, b)

# Extended Euclidean Algorithm
def eux(a, b):
    r = [max(a, b), min(a, b)]
    s = [1, 0]
    t = [0, 1]

    while not (r[-1] == 0):
        q = r[-2] // r[-1]
        r.append(r[-2] - q*r[-1])
        s.append(s[-2] - q*s[-1])
        t.append(t[-2] - q*t[-1])

    # r[0]*s[-2] + r[1]*t[-2] = r[-2]
    if (a>=b):
        return (s[-2], t[-2])
    else:
        return (t[-2], s[-2])
