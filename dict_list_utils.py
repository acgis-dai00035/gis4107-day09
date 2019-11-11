# -*- coding: UTF-8 -*-
# ------------------------------------------------------------------------------
# Name:        exercise_template.py
#
# Purpose:     Brief desciption of what module does
#
# Usage:       Module name and required/optional command-line parameters (if any)
#
# Author:      Your name(s)
#
# Created:     dd/mm/yyyy
# ------------------------------------------------------------------------------

def main():
    pass

def get_missing_keys(dict_ref,dict_to_compare):

    """two Dictionary parameters:  dict_ref and dict_to_compare where

    dict_to_compare is the dictionary that may have missing keys and dict_ref is

    the dictionary you want to compare it to"""

    keys = dict_ref.keys()

    miss = []

    for i in keys:

        if dict_to_compare.has_key(i):

            pass

        else:

            miss.append(i)

    return miss



def get_missing_keys_with_count(dict_ref,dict_to_compare):

    """return a tuple containing the number of missing keys and the list of missing keys"""

    lists = get_missing_keys(dict_ref,dict_to_compare)

    return  (len(lists),lists)



def get_unique(in_list):

    """get_unique that has one parameter named in_list that may have duplicate values

    and returns a list of only unique values"""

    out_list = []

    for i in in_list:

        if not i in out_list:

            out_list.append(i)

    return out_list



def flatten_list(in_list):

    """return a list that contains the items of the list that are not lists or tuples

    as well as the items of the list(s) or tuples(s)"""

    out_list = []

    for i in in_list:

        if type(i) == list or type(i) == tuple:

            for k in i:

                out_list.append(k)

        else:

            out_list.append(i)

    return out_list


if __name__ == '__main__':
    main()