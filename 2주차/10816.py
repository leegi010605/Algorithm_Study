N = int(input())
A = list(map(int,input().split()))
M = int(input())
B = list(map(int,input().split()))

dic = {}
for i in A:
  if i not in dic:
    dic[i] = 1
  else:
    dic[i] += 1
#print(dic)

for i in B:
  if i in dic:
    print(dic[i],end=" ")
  else: 
    print(0,end=" ")