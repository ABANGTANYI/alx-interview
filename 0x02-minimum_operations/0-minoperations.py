#!/usr/bin/env python3

"""
Calculates the minimum number of 'Copy All' and 'Paste' operations
needed to generate n 'H' characters in a text file.

Args:
    n (int): The target number of 'H' characters to generate.

Returns:
    int: The minimum number of operations needed to generate n 'H' characters.
         If n is impossible to achieve, returns 0.
"""
def minOperation(n):
    if n <= 0:
        return 0
    
    print("n before loop", n)
    
    divisor = 2
    num_of_operations = 0
    
    while n > 1:
        if n % divisor == 0:
            print("divisor is : ", divisor)
            n = n / divisor
            print("\nn = n / divisor", n)
            
            num_of_operations += 1
            print("num of ops", num_of_operations)
        else:
            divisor += 1
            print("divisor after increment:", divisor)
    
    return num_of_operations

n = 12
print(minOperation(n))
