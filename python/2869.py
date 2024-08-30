import sys
a, b, v = map(int, sys.stdin.readline().split())
plus_count = a - b
result_v = v - a
date1 = result_v % plus_count
date2 = result_v // plus_count
if date1 == 0:
    print(date2 + 1)
else:
    print(date2 + 2)

    
