# RSA encryption

import mr
import random

# Miller-Rabin Tester
def main():
    print(getPrime(10**300, 10**301))

# Prime Finder

# Find a prime between a and b
def getPrime(a, b):
    r = random.SystemRandom()
    n = r.randint(a, b)
    if (n%2==0):
        n+=1
    print(n)
    assert(n%2==1)
    for i in range(1100):
        if (mr.isPrime(n, 64)):
            print("Success!")
            print(n)
            return n
        #print("Failed!")
        n+=2
    print("Failed after 1100 tries.") # TODO: False negatives?
    return n

# Totient Getter
# 65537
# Encryptor
# Decryptor
# Text-to-number and back

if __name__ == "__main__":
    main()
