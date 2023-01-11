def solution(num, total):
    average = total / num
    return [int(((2* average) - (num-1))//2)+ i for i in range(num)]

print(solution(4,14))