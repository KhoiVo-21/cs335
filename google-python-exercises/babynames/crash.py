#!/usr/bin/python -tt

import os

for num in [11, 9, 0, 7, 2, 0]:
    try:
        print "Number is %d" % (100/num)
    except ZeroDivisionError as err:
        print err
        

# files = ["bby1990.htlm", "babu1992.html"];
# for file in files:
#     f = open(file, 'rU')
#     print f.name