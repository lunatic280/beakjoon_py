import sys
n = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
m_list = list(map(int, sys.stdin.readline().split()))
result = [0 for i in range(m)]
count = 0
for i in m_list:
    for k in n_list:
        if i == k:
            result[count] += 1
        else:
            continue
        
    count += 1

for i in result:
    print(i, end=" ")