def solution(n):
    s = "수박"
    return s*int(n//2) if n % 2 == 0 else s*int(n//2)+ s[:-1]

# def water_melon(n):
#     s = "수박" * n
#     return s[:n]
