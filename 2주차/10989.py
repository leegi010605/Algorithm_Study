#수 정렬하기 3
import sys

N = int(sys.stdin.readline())
a=[]
for i in range(N):
  a.append(int(sys.stdin.readline()))
a.sort()
for i in a:
  print(i)