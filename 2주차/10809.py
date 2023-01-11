# 알파벳 찾기
alpha = 'abcdefghijklmnopqrstuwxyz'
S = input()

for i in alpha:
  if i in S:
    print(S.index(i),end=" ")
  else:
    print(-1,end=" ")