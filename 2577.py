a = int(input())
b = int(input())
c = int(input())

result = a*b*c
sum1 = []
for i in str(result):
    sum1.append(int(i))
    
arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in sum1:
    for k in range(10):
        if i == k:
            arr[k] += 1
            break
for i in arr:
    print(i)
