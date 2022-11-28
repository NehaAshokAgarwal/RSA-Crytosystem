import stdio
import stdrandom
import sys


# Generates and returns the public/private keys as a tuple (n, e, d). Prime numbers p and q
# needed to generate the keys are picked from the interval [lo, hi).
def keygen(lo, hi):
    # Getting a list of prime numbers from the interval (lo, hi) using the _primes() function.
    Primes_list_1 = _primes(lo, hi)

    # Getting a list of two distinct prime numbers (p and q) using the _sample() function, chosen at
    # random from the list of Primes_list_1
    sample = _sample(Primes_list_1, 2)
    # Assigning the values of p and q from the list - sample.
    p = sample[0]
    q = sample[1]
    # Assigning the variable n and m.
    n = p * q
    m = (p - 1) * (q - 1)
    # Receiving another list of prime numbers from the interval of (2, m), using the _primes()
    # function.
    Primes_list_2 = _primes(2, m)
    # selecting a random prime number e, which is less than m and such that e does not divide m,
    # using the _choice() function and while loop.
    e = _choice(Primes_list_2)
    while m % e == 0:
        e = _choice(Primes_list_2)
        # selecting a number d from the range of (1, m), e*d % n is equal to one using the for
        # loop.
    for d in range(1, m):
        if e * d % m == 1:
            break
    # return the tuple (public/private key) for encryption and decryption)
    return (n, e, d)


# Encrypts x (int) using the public key (n, e) and returns the encrypted value.
def encrypt(x, n, e):
    x = (x ** e) % n
    return x


# Decrypts y (int) using the private key (n, d) and returns the decrypted value.
def decrypt(y, n, d):
    y = (y ** d) % n
    return y


# Returns the least number of bits needed to represent n.
def bitLength(n):
    return len(bin(n)) - 2


# Returns the binary representation of n expressed in decimal, having the given width, and padded
# with leading zeros.
def dec2bin(n, width):
    return format(n, '0%db' % width)


# Returns the decimal representation of n expressed in binary.
def bin2dec(n):
    return int(n, 2)


# Returns a list of primes from the interval [lo, hi).
def _primes(lo, hi):
    # creating a list with name primes.
    primes = []
    for p in range(lo, hi):
        # if p is less than 2, i.e (0, 1), then continue, that is do not return them as primes.
        if p < 2:
            continue
        j = 2
        while j <= p / j:
            # if j divides p, then p is not a prime number thus exit the while loop.
            if p % j == 0:
                break
            j += 1
            # After exhausting the loop, the number is a prime. Thus append it to the list.
        if j > p / j:
            primes += [p]
    return primes


# Returns a list containing a random sample (without replacement) of k items from the list a.
def _sample(a, k):
    # creating a list b with all the elements of list a in it, through slicing (not copying).
    b = a[:]
    # Selecting the K number of elements of list b through a random process, and then shuffling
    # the elements to avoid replacements.
    for i in range(k):
        r = stdrandom.uniformInt(i, len(a))
        # shuffling the values
        temp = b[r]
        b[r] = b[i]
        b[i] = temp

    # return the List b with k elements.
    return b[:k]


# Returns a random item from the list a.
def _choice(a):
    r = stdrandom.uniformInt(0, len(a))
    return a[r]


# Unit tests the library [DO NOT EDIT].
def _main():
    x = ord(sys.argv[1])
    n, e, d = keygen(25, 100)
    encrypted = encrypt(x, n, e)
    stdio.writef('encrypt(%c) = %d\n', x, encrypted)
    decrypted = decrypt(encrypted, n, d)
    stdio.writef('decrypt(%d) = %c\n', encrypted, decrypted)
    width = bitLength(x)
    stdio.writef('bitLength(%d) = %d\n', x, width)
    xBinary = dec2bin(x, width)
    stdio.writef('dec2bin(%d) = %s\n', x, xBinary)
    stdio.writef('bin2dec(%s) = %d\n', xBinary, bin2dec(xBinary))


if __name__ == '__main__':
    _main()
