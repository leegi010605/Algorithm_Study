def solution(strings, n):
    strings.sort(); return sorted(strings,key = lambda x : x[n])

#인덱스 1의 문자가 같은 문자열이 여럿 일 경우, 
#사전순으로 앞선 문자열이 앞쪽에 위치합니다.
#이 부분을 해결을 못했었다
# def solution(strings, n):
#     a =[]
#     for i in range(len(strings)):
#         a.append(str(strings[i])[n:n+1])
#     return ([strings[sorted(a).index(i)] for i in a])