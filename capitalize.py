#!/bin/python3

"""
You are asked to ensure that the first and last names of
people begin with a capital letter in their passports.
For example, alison heck should be capitalised correctly
as Alison Heck.

The string consists of alphanumeric characters and spaces.
Note: in a word only the first character is capitalized.
Example 12abc when capitalized remains 12abc.

Solved in 45 min
"""

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    new_string = s.title()
    m = re.search('([0-9][A-Z])', new_string)
    if m != None:
        new_string = new_string.replace(m.group(), m.group().lower())
    return new_string

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
