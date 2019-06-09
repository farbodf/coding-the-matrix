# Solution to problem 1.5.1: Decrypting the encoded message

import string

num_to_letter = dict(zip([bin(x) for x in range(27)], string.printable[10:36] + ' '))
cyphertext = [bin(x) for x in [21, 4, 21, 11, 25, 3, 11, 21, 4, 25, 26]]
keys = [bin(x) for x in range(32)]
for key in keys:
    decrypted_bin = [bin(int(x, 2) ^ int(key, 2)) for x in cyphertext]
    decrypted = [num_to_letter.get(x, '?') for x in decrypted_bin]
    message = "".join(decrypted)
    if not '?' in message:
        print(message)
