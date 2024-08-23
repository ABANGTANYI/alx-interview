#!/usr/bin/env python3
# This function calculates the minimum number of "Copy All" and "Paste" operations
# needed to achieve a given number of 'H' characters in a text file.
def minOperations(n):
    if n <= 1:
        return 0

    # Find the largest power of 2 that is less than or equal to n
    power_of_2 = 1
    while power_of_2 * 2 <= n:
        power_of_2 *= 2

    # If n is a power of 2, return the number of operations needed
    if n == power_of_2:
        return n // 1

    # If n is not a power of 2, find the smallest power of 2 that is greater than n
    # and subtract the largest power of 2 that is less than or equal to n
    return (n - power_of_2) // (power_of_2 // 2) + n // power_of_2
