import rsa
import stdio
import sys


# Entry point.
def main():
    # Accepting the two integers - n and e using the command line argument.
    n = int(sys.argv[1])
    e = int(sys.argv[2])
    # Getting the number of bits to encode n using the bitLength() function.
    width = rsa.bitLength(n)
    # Reading all the characters of the message using the standard input.
    message = stdio.readAll()
    # for each character in the message.
    for c in message:
        # turning a character into the integer using the built in function ord().
        x = ord(c)
        # Encrypting x using the encrypt() function from the rsa library.
        y = rsa.encrypt(x, n, e)
        # Converting y (encrypted value) from decimal to binary using the dec2bin() function from
        # the rsa library.
        z = rsa.dec2bin(y, width)
        # writing the encrypted value as a width long binary string using the standard output.
        stdio.write(z)

    stdio.writeln()


if __name__ == '__main__':
    main()
