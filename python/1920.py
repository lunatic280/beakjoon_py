import sys
n = int(sys.stdin.readline())
arr_n = list(map(int, sys.stdin.readline().split()))
arr_n.sort()
m = int(sys.stdin.readline())
arr_m = list(map(int, sys.stdin.readline().split()))

def test(n, arr_n, index):
    
    left = 0
    right = n - 1
    while left <= right:
        mid = (left + right) // 2
        if arr_n[mid] == index:
            return True
        elif arr_n[mid] > index:
            right = mid - 1
        elif arr_n[mid] < index:
            left = mid + 1
    return False
    

for i in arr_m:
    if test(n, arr_n, i):
        print(1)
    else:
        print(0)