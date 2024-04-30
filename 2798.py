import sys
n, m = map(int, sys.stdin.readline().split())
n_list = list(map(int, sys.stdin.readline().split()))
max = 0
for_out = 0
for i in range(len(n_list)):
    if for_out == 1:
        break
    for k in range(len(n_list)):
        if i == k:
            continue
        if for_out == 1:
            break
        for j in range(len(n_list)):
            if n_list[i] == n_list[j]:
                continue
            if n_list[k] == n_list[j]:
                continue
            sum1 = n_list[i] + n_list[k] + n_list[j]
            if sum1 == m:
                print(sum1)
                for_out = 1
                break
            elif sum1 < m and max < sum1:
                max = sum1
            else:
                continue
if for_out == 0:
    print(max)
            




