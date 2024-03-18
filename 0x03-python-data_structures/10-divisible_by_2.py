#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    return [num % 2 == 0 for num in my_list]

original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = divisible_by_2(original_list)
print(result)

