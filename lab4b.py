#!/usr/bin/env python3

def join_lists(l1, l2):
    # join_lists will return a list that contains every value from both l1 and l2
    tm_s1 = set(l1)
    tm_s2 = set(l2)
    jo_set = tm_s1 | tm_s2
    jo_list = list(jo_set)
    return jo_list


def match_lists(l1, l2):
    # match_lists will return a list that contains all values found in both l1 and l2
    tm_s1 = set(l1)
    tm_s2 = set(l2)
    mat_set = tm_s1 & tm_s2
    mat_list = list(mat_set)
    return mat_list


def diff_lists(l1, l2):
    # diff_lists will return a list that contains all different values, which are not shared between the lists
    tm_s1 = set(l1)
    tm_s2 = set(l2)
    diff_set = tm_s1 ^ tm_s2
    diff_list = list(diff_set)
    return diff_list

if __name__ == '__main__':
    list1 = list(range(1,10))
    list2 = list(range(5,15))
    print('list1: ', list1)
    print('list2: ', list2)
    print('join: ', join_lists(list1, list2))
    print('match: ', match_lists(list1, list2))
    print('diff: ', diff_lists(list1, list2))