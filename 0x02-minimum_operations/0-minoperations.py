#!/usr/bin/env python3

def minOperations(n):
    if n <= 0:
        return 0
    
    # Initialize the number of operations
    operations = 0
    
    # Keep doubling the number of characters until it exceeds n
    while n > 1:
        # If n is a power of 2, the minimum number of operations is the number of doublings
        if (n & (n - 1)) == 0:
            return operations + 1
        
        # Double the number of characters
        n = n - (n >> 1)
        operations += 1
    
    return operations
