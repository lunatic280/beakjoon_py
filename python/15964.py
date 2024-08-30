def add(a, b):
    sum = (a+b)*(a-b)
    print(sum)

a, b = map(int, input().split())
add(a, b)
