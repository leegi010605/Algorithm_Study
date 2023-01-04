def solution(my_str, n):
    answer = [my_str[i:i+n] for i in range(0, len(my_str), n)]
    # a = [''.join(x) for x in zip(*[list(my_str[z::n]) for z in range(n)])]
    # print(a)  
    return answer

