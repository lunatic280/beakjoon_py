import sys
from collections import deque
a = int(sys.stdin.readline())

arr1 = deque(range(1, a+1))

while (len(arr1) != 1):
    arr1.popleft()
    arr1.append(arr1.popleft())

print(arr1[0])
