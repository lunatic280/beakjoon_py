import sys
a = int(input())
arr1 = []
arr1 = list(map(int, sys.stdin.readline().split()))

arr1.sort(reverse=True)

m = arr1[0]

m_arr1 = []
for i in range(len(arr1)):
    if arr1[i] == 0:
        ip = 0
    else:

        ip = arr1[i] / m

        m_arr1.append(ip*100)


sum = 0
for i in m_arr1:
    sum += i
result = sum / a
print(result)
