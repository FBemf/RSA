# RSA encryption

import mr
import eu
import random

def main():
    kp = makeKeys(BITS)
    print("PUBLIC = " + str(kp[0]))
    print("PRIVATE = " + str(kp[1]))

    m = asciiToInt(input("ASCII to encrypt / decrypt: "))
    c = encrypt(m, kp[0])
    a = decrypt(c, kp[0], kp[1])
    #assert(m==c)
    print("Number: " + str(m))
    print("Encrypted: " +  str(c))
    print("Decrypted: " + str(a))
    o = intToAscii(a)
    print("Text: " + o)
    return 0

# Constants
ENCRYPTION_BASE = 65537
BITS = 1024

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
        n+=2
    return 0

# Totient Getter
def carmichael(a, b):
    #assumes a and b are prime
    return eu.lcm(a-1, b-1)

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

    d = eu.eux(e, y)[0]
    while (d < 0):
        d+=y

    return (n, d)

# Encrypt - Decrypt

def encrypt(m, n):
    # encrypt(integer plaintext, public key)
    return pow(m, ENCRYPTION_BASE, n)

def decrypt(c, n, d):
    # integer cyphertext, public key, private key
    return pow(c, d, n)

# Text-to-number and back
def asciiToInt(t):
    m = "1"
    for c in t:
        m += str(ord(c)).rjust(3, '0')
    return int(m)

def intToAscii(c):
    t=str(c)
    assert(t[0]=='1')
    t=t[1:]
    m=""
    assert(len(t)%3==0)
    while (len(t) > 0):
        m += chr(int(t[:3]))
        t=t[3:]
    return m

# TODO: OAEM
# TODO: Long plaintext support

if __name__ == "__main__":
    main()
