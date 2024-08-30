import sys
#T의 개수를 입력받음
t = int(sys.stdin.readline())
#t_list 리스트 생성
t_list = []
#T의 개수만큼 입력받음
for i in range(t):
  t_append = sys.stdin.readline().strip()
  t_list.append(t_append)

#괄호가 닫혔는지 계산

for args in t_list:
  #괄호가 닫혔는지 계산
  count = []
  for index in args:
    if index == '(':
      count.append(1)
    elif index == ')':
      if count:
        count.pop()
      else:
        print("NO")
        break
  else:
    if len(count) == 0:
      print("YES")
    else:
      print("NO")
  