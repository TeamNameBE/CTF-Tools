import sys
import logging

baconed_string = sys.argv[1]

if len(baconed_string) % 5 != 0:
    logging.error("Input's size must be a multiple of 5")
    exit(1)

# I/J are the same chars
# u/v are same chars
thresholds = [9, 15]


decoded = ""
for index in range(len(baconed_string) // 5):
    enc_char = baconed_string[index * 5:(index * 5) + 5]
    char_val = 0
    for index, val in enumerate(enc_char[::-1]):
        char_val += (val == "B") * 2 ** index

    for thresh in thresholds:
        if thresh < char_val:
            char_val += 1

    decoded += chr(char_val + 65)
    print(enc_char, "->", chr(char_val + 65))
print("result :", decoded)
