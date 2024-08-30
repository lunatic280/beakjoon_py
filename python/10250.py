from time import sleep


a = int(input())
for i in range(a):
    floor, abc, n = map(int, input().split())
    new_floor = n % floor #10번쨰 사람 에서 6층으로 나누면 4가 남으니까 4층
    new_abc = n // floor + 1#10번쨰 사람을 6층으로 나누면 1이나옴
    if new_floor == 0:
        new_floor = floor
        new_abc -= 1
    print(new_floor * 100 + new_abc)