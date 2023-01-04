# 따옴표 추가
# cipher ="pfqallllabwaoclk"
# code = 2
# print("\"",cipher[code-1::code],"\"",sep="")

def solution(cipher, code):
    return cipher[code-1::code]