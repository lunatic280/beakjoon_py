t = int(input())
r = []
s = []
for i in range(t):
    r_input, s_input = list(map(str, input().split()))
    r.append(r_input)
    s.append(s_input)
for i in range(t):
    result = s[i]
    list(result)
    mul = r[i]
    a = ''
    for i in result:
        a += str(i) * int(mul)
    print(a)
