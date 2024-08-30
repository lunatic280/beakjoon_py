import sys
def my_round(x):
    if x - int(x) >= 0.5:
        return int(x) + 1
    else:
        return int(x)
a = int(sys.stdin.readline())
arr1 = []
for i in range(a):
    b = int(sys.stdin.readline())
    arr1.append(b)

arr1.sort()
len_arr1 = len(arr1)
if a == 0:
    print(0)
else:
    sub_avg = my_round(len_arr1 * 0.15)
    del arr1[0:sub_avg]
    del arr1[len(arr1) - sub_avg:]
    sum = 0
    for i in arr1:
        sum += i
    avg = my_round(sum / len(arr1))
    print(avg)
