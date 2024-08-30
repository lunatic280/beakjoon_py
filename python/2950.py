a = list(map(int, input().split()))

c = sorted(a, reverse=True)
b = sorted(a, reverse=False)


if a == b:
    print("ascending")
elif a == c:
    print("descending")
else:
    print("mixed")