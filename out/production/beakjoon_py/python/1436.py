a = int(input())
count = 0
b = '666'
while 1:
    if a == count:
        break
    try:
        if b.find('666') != -1:
            count += 1
        b = int(b)+1
    except AttributeError:
        b = str(b)
print(b - 1)
