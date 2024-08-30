import sys
import math

def is_prime_number(x):
    if x == 1:
        return False
    elif x == 2:
        return True
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

n = int(input())

arr1 = list(map(int, sys.stdin.readline().split()))
num1 = []
for i in arr1:
    x = is_prime_number(i)
    if x == True:
        num1.append(i)
    else:
        continue

print(len(num1))