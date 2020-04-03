# this is the first file I imported using git and my terminal
# yayyy!! :)

# The task was to count the maximum consecutive 1's
# in an input converted to binary.
# the script should be self-explanatory, I will add more descriptions
# to future code ;)

#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())
    assert 1 <= n <= 10**6
    binary = bin(n)[2:]
    counter = 0
    saved = int()
    for i in range(0, len(binary)):
        if binary[i] == "1":
            counter +=1
        if binary[i] == "0":
            counter = 0
        if counter > saved:
            saved = counter

print(saved)
