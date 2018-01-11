# RSA encryption

import mr
import random

# Miller-Rabin Tester
def main():
    print(getPrime(1024))

# Prime Finder

# Find a prime between a and b
def getPrime(bits):
    getPrimeRange(2**(bits-1), 2**bits)

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
def eulerPhi(a, b):
    #assumes a and b are prime
    return (a-1)*(b-1)

# 65537
ENCRYPTION_BASE = 65537

# Encryptor
# Decryptor
# Text-to-number and back

if __name__ == "__main__":
    main()
