problem = int(input())
arr = list(map(int,input().split()))
sum  = 0
count = 1
for i in arr:
    if i == 1:
        sum = sum + count
        count += 1
    else:
        count = 1

print(sum)
    
        