#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    global count
    try:
        count = 0
        for i in range(0, x, 1):
            print(my_list[i], end="")
            count += 1
        print("")
    except IndexError:
        print("")
    finally:
        return count
