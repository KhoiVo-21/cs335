#!/usr/bin/python
import re

def get_initial(names):
    arr = []
    each = []
    for name in names:
        if len(name.split()) < 3:
            arr.append(name.split()[0][0] + name.split()[1][0])
        else:
            arr.append(name.split()[0][0] + name.split()[1][0] + name.split()[2][0])
    return arr

def main():
    names = ["Debby Ryan", "Channing Tatum", "Coretta Scott King", "Emmylou Harris"]
    arr = get_initial(names)
    print arr
    
if __name__ == "__main__":
    main()
