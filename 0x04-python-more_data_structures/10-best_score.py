#!/usr/bin/python3

# first unpack to get the starting max

def best_score(a_dictionary):

    if not a_dictionary:  # empty
        return None

    score = max(a_dictionary, key=a_dictionary.get)  # get the best score
    return score
