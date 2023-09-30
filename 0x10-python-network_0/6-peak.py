#!/usr/bin/python3
"""
Technical interview
NB: A peak element in a list of integers is any element that is greater
than both of its neighboring elements
"""

def find_peak(list_of_integers):
    """
    Find a peak in a list of integers
    """
    if list_of_integers is None or type(list_of_integers) is not list:
        return
    if len(list_of_integers) == 0:
        return

    # Indices
    lower = 0;
    upper = len(list_of_integers) - 1
    trials = 0
    print()     # test
    peak = find_peak_aux(list_of_integers, lower, upper, trials)
    print("\nExhausted this list")    # test
    return(peak)

def find_peak_aux(i_list, lower, upper, trials):
    """
    An auxiallary function
    Find any of the peaks in a list
    """
    '''
    # Safety
    if trials > 10:     # test
        print("number of trials has reached maximum: {}".format(trials))    # test
        return
    else:
        trials += 1
    '''

    if i_list is None or type(i_list) is not list:
        return
    if len(i_list) == 0:
        return
    if upper < 0 or lower < 0 or lower > upper:
        return

    # Operation
    print("\nAnalyzing: {}".format(i_list))   # test
    print("Range: {}".format(i_list[lower:upper + 1]))  # test
    print("lower index: {}".format(lower))    # test
    print("upper index: {}".format(upper))    # test
    if upper == lower:
        print("aux: upper is same as lower")    # test
        return i_list[upper]

    if upper - lower == 1:
        if i_list[upper] >= i_list[lower]:
            return i_list[upper]
        else:
            return i_list[lower]

    if upper - lower == 2:
        mid = lower + 1
        if (i_list[mid] >= i_list[mid -1 ] and i_list[mid] >= i_list[mid + 1]):
            return i_list[mid]
        else:
            return None

    elif upper - lower > 2:
        peak1 = find_peak_aux(i_list, lower, lower + int((upper - lower) / 2), trials)
        peak2 = find_peak_aux(i_list, lower + int((upper - lower) / 2) + 1, upper, trials)
        if peak1 is not None:
            return peak1
        else:
            return peak2
