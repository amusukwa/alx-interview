#!/usr/bin/python3

""" Module for minoperations """


def minOperations(n:int)-> int:
    """ function that calculates # of operations """
    if n <= 1:
        return n

    operations = 0
    characters = 1  # Start with one 'H' character

    while characters < n:
        if n % characters == 0:
            operations += 2  # Copy all and paste operation
            characters *= 2  # Double the count of characters
        else:
            factor = find_smallest_factor(n)
            operations += factor
            characters += factor

    return operations

def find_smallest_factor(n:int)->int:
    """Find the smallest factor of n (excluding 1)"""
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i
    return n
