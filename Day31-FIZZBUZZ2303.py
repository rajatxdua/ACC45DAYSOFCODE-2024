import math

def fact(n):
    return math.factorial(n)
    
for _ in range(int(input())):
    n = int(input())
    
    if n>2:
        print(fact(n)//fact(n-2))
    else:
        print(n)
        