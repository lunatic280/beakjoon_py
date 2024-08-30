a = input()
a1 = a.lower()
a2 = list(a1)

check = []
for i in a2:
    if i not in check:
            check.append(i)

check1 = []
for i in check:
    count = 0
    for j in a2:
        if i == j:
            count += 1
    check1.append(count)

max1 = 0
count1 = 0
key = 0
for i in range(len(check)):
     if check1[i] > max1:
          max1 = check1[i]
          count1 = 0
          key = i
     elif check1[i] == max1:
          count1 = 1
if count1 == 1:
     print('?')
else:
     print(check[key].upper())
         



