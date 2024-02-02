#!/usr/bin/python3
def magic_string(counter=[]):
    counter.append("BestSchool")  # list persists across calls
    return ", ".join(counter)
