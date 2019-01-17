"""
Name Khoi Vo
Class cs335
This program's supposed to multiply some stuff
"""
#!/usr/bin/env python3
import sys

# This thing multiply stuffs
def mult(a,b):
    print(str(a * b))

if __name__ == '__main__':
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    mult(num1, num2)

