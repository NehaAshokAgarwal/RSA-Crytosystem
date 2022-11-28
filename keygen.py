import rsa
import stdio
import sys


# Entry point.
def main():
    # Accepting the integers - lo, and hi by using the command line arguments.
    lo = int(sys.argv[1])
    hi = int(sys.argv[2])
    # Generating a private/public key from the interval (lo, hi) by calling the Keygen() function
    # from the rsa library.
    key = rsa.keygen(lo, hi)
    # Printing the key (n, e, d) by using the standard output.
    stdio.write(str(key[0]) + ' ' + str(key[1]) + ' ' + str(key[2]))


if __name__ == '__main__':
    main()
