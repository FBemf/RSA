# Miller Rabin Test
# RSA encryption

import math
import random

# Miller-Rabin Tester
def main():
    n = int(input("Integer over 64: "))
    print(millerRabin(n, 64))

def millerRabin(n, i):
    # Tests to see if n is prime, using i iterations
    # of the Miller-Rabin primality test
    # n must be odd and greater than i; i is recommended
    # to be at least 64, for cryptographic safety.

    #find values s & r such that n=2^r*s+1, s is odd
    r=0
    s=0
    for t in range(1, math.ceil(math.log2(n))+1):
        s = (n-1) / pow(2, t)
        if (s.is_integer() and s % 2 == 1):
            s=int(s)
            r=t
            break
    else:
        print("Miller-Rabin Test Failure: r & s not found. Is n correct?")
        return(False)

    #test i consecutive values 1<=a<n
    #for a^s=1 (mod n) or a^[(2^j)s]=-1 (mod n) for all 0<=j<r
    rand=random.SystemRandom()
    a=rand.randint(1, n-i)
    for k in range(i):
        if (pow(a+k, s) % n == 1):
            continue

        b=0
        for j in range(r):
            if (pow(a+k, pow(2, j) * s) % n == n-1):
                b=1
                break
        if b==1:
            continue

        return False

    return True

if __name__ == "__main__":
    main()
