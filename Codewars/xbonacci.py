"""
A Xbonacci function that takes a signature of X elements (each next element is the sum of the last X elements 
- and returns the first n elements of the so seeded sequence).
"""

def Xbonacci(signature, n):
    result = 0
    if n < len(signature):
        signature = signature[:n]
    else:
        for i in range(n-len(signature)):
            result = sum(signature[i::])
            signature.append(result)
    return signature
