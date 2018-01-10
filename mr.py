# Miller Rabin Test
# RSA encryption

import sm
import math
import random

# Miller-Rabin Tester
def main():
    n = int(input("Integer over 64: "))
    print(isPrime(n, 64))

def isPrime(n, i):
    # Tests to see if n is prime, using i iterations
    # of the Miller-Rabin primality test
    # n must be odd and greater than i; i is recommended
    # to be at least 64, for cryptographic safety.



    primes = \
    [ 2,      3,      5,      7,     11,     13,     17,     19,     23,     29,
     31,     37,     41,     43,     47,     53,     59,     61,     67,     71,
     73,     79,     83,     89,     97,    101,    103,    107,    109,    113,
    127,    131,    137,    139,    149,    151,    157,    163,    167,    173,
    179,    181,    191,    193,    197,    199,    211,    223,    227,    229,
    233,    239,    241,    251,    257,    263,    269,    271,    277,    281,
    283,    293,    307,    311,    313,    317,    331,    337,    347,    349,
    353,    359,    367,    373,    379,    383,    389,    397,    401,    409,
    419,    421,    431,    433,    439,    443,    449,    457,    461,    463,
    467,    479,    487,    491,    499,    503,    509,    521,    523,    541,
    547,    557,    563,    569,    571,    577,    587,    593,    599,    601,
    607,    613,    617,    619,    631,    641,    643,    647,    653,    659,
    661,    673,    677,    683,    691,    701,    709,    719,    727,    733,
    739,    743,    751,    757,    761,    769,    773,    787,    797,    809,
    811,    821,    823,    827,    829,    839,    853,    857,    859,    863,
    877,    881,    883,    887,    907,    911,    919,    929,    937,    941,
    947,    953,    967,    971,    977,    983,    991,    997]

    for p in primes:
        if (n == p):
            return True
        if (n % p == 0):
            return False

    if (n<=0):
        return False

    #find values s & r such that n=2^r*s+1, s is odd
    r=1
    s=n-1
    while (s%2 == 0):
        s=int(s/2)
        r=r*+1

    #test i consecutive values 1<=a<n
    #for a^s=1 (mod n) or a^[(2^j)s]=-1 (mod n) for all 0<=j<r
    rand=random.SystemRandom()
    a=rand.randint(1, n-i)
    for k in range(i):
        if (pow(a+k*2, s, n) == 1):
        #if (sm.squareAndMultiply(a+k, s, n) == 1):
            continue

        b=0
        for j in range(r):
            if (pow(a+k, pow(2, j) * s, n) == n-1):
            #if (sm.squareAndMultiply(a+k, s, n) == n - 1):
                b=1
                break
        if b==1:
            continue

        return False

    return True

if __name__ == "__main__":
    main()
