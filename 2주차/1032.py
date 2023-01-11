#명령 프롬프트
N = int(input())
S = list(input())

for i in range(N-1):
  check = list(input())
  for j in range(len(S)):
    if S[j] != check[j]:
      S[j] = '?'
print(''.join(S))
