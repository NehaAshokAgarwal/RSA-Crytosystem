import rsa
import stdio
import sys


# Entry point.
def main():
    # Accepting the two integer - n and d as command line arguments.
    n = int(sys.argv[1])
    d = int(sys.argv[2])
    # Getting the number of bits of n needed for the decryption using the bitLength() function from
    # the rsa library.
    width = rsa.bitLength(n)
    # Reading all the characters of the encrypted binary string using the standard input
    message = stdio.readAll()
    # For each character in the encrypted binary string (message).
    for i in range(0, len(message) - 1, width):
        # Creating a list of substring of message.
        s = message[i: i + width]
        # converting the decimal representation of the binary string s (encrypted message) using
        # the bin2dec() function in the rsa library.
        y = rsa.bin2dec(s)
        # Decrypting the y using the decrypt() function in the rsa library.
        c = rsa.decrypt(y, n, d)
        # converting the decrypted message into the character using the built in function chr().
        m = chr(c)
        # Printing the decrypted value using the standard output.
        stdio.write(m)


if __name__ == '__main__':
    main()
