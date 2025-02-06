#!/usr/bin/env python3
# Strings 1

str1 = 'Hello World!!'
str2 = 'Seneca College'

num1 = 1500
num2 = 1.50

def first_five(str:str)->str:
    # Place code here - refer to function specifics in section below
    fir_five = str[0:5]
    return fir_five

def last_seven(str:str)->str:
    # Place code here - refer to function specifics in section below
    last_seven = str[-7:]
    return last_seven

def middle_number(num)->str:
    # Place code here - refer to function specifics in section below
    tmp_str = str(num)
    mid_num = tmp_str[1:3]
    return mid_num

def first_three_last_three(str1, str2)->str:
    # Place code here - refer to function specifics in section below
    first_three_last_three = str1[0:3] + str2[-3:]
    return first_three_last_three


if __name__ == '__main__':
    print(first_five(str1))
    print(first_five(str2))
    print(last_seven(str1))
    print(last_seven(str2))
    print(middle_number(num1))
    print(middle_number(num2))
    print(first_three_last_three(str1, str2))
    print(first_three_last_three(str2, str1))