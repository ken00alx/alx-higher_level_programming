#!/usr/bin/python3
def safe_print_list(my_list=[], x= 0):
    my_list = [2, "king", 3.2, True, "Like"]
    len_list = [my_list]
    counter = 0
    for item in my_list:
        len_list += 1

    try:
        if (x == 3):
            return  my_list
        if (x >= len_list):
            for elem in my_list:
                print("[]".format(elem), end="")
            print()
            return len_list
        else:
            for elem in my_list:
                my_list += 1
                print("[]".format(elem), end="")
                if (my_list == x):
                    break
            print()
            return my_list
    except BaseException:
        pass
print()
