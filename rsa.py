# RSA encryption

import mr
import eu
import random

# Miller-Rabin Tester
def main():
    print(makeKeys(1024))

# Prime Finder

# Find a prime between a and b
def getPrime(bits):
    return getPrimeRange(2**(bits-1), 2**bits)

def getPrimeRange(a, b):
    r = random.SystemRandom()
    n = r.randint(a, b)
    if (n%2==0):
        n+=1
    assert(n%2==1)
    for i in range(1100):
        if (mr.isPrime(n, 64)):
            return n
        #print("Failed!")
        n+=2
    return 0

# Totient Getter
def carmichael(a, b):
    #assumes a and b are prime
    return eu.lcm((a-1), (b-1))

# 65537
ENCRYPTION_BASE = 65537

# Create Keys
def makeKeys(b):
    # Makes a public modulus n and a private key d
    p=0
    q=0
    while not p:
        p = getPrime(1024)
    while not q:
        q = getPrime(1024)

    n = p * q
    y = carmichael(p, q)
    e = ENCRYPTION_BASE

    d = abs(eu.eux(e, y)[0])

    return (n, d)

# Encryptor

# Decryptor
# Text-to-number and back

if __name__ == "__main__":
    main()
