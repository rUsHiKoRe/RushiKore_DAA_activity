import math
import os
import random
import re
import sys

def extraLongFactorials(n):
    f=1
    for i in range(2,n+1):
        f=f*i
    return f
        
if __name__ == '__main__':
    n = int(input())

    print(extraLongFactorials(n))

