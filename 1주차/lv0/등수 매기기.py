def solution(score):
    a = []
    answer = []
    for x,y in score:
        a.append((x+y)/2)
    a_compare = sorted(a)
    a_compare.reverse()
    for i in a:
        answer.append(a_compare.index(i)+1)
    return answer

#바보같이 자료형 int로 해서 소수점도 비교 안해줌...