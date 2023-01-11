#나이순 정렬
N = int(input())
a = []
for i in range(N):
  a.append(list(map(str,input().split())))
a.sort(key = lambda x: int(x[0]))

for i in range(N):
  print(a[i][0], a[i][1])