import sys
from collections import OrderedDict
result = []
#테스트 케이스의 개수
t = int(sys.stdin.readline())
for i in range(t):
  #문서의 개수와 몇 번째로 인쇄되는 문서
  n, m = map(int, sys.stdin.readline().split())
  #문서의 리스트 만들기
  n_list_key = [i for i in range(n)]
  #print(n_list_key) 
  #문서들의 중요도
  n_list = list(map(int, sys.stdin.readline().split()))
  #print(n_list)
  #딕셔너리롤 만들기
  n_dict = dict(zip(n_list_key, n_list))
  #print(n_dict)
  #중요도 순으로 배열 정렬하기
  sorted_dict = sorted(zip(range(n), n_list), key=lambda x: (-x[1], x[0]))
  sorted_dict = OrderedDict(sorted_dict)
  #print(sorted_dict)
  #찾는 문서가 몇 번째로 출력되는지 찾기
  find_index = list(sorted_dict.keys()).index(m) + 1
  result.append(find_index)
  #print(find_index)
#값 출력
for i in result:
  print(i)
