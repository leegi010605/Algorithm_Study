# # := 바다코끼리 연산으로 간단하게 코딩
# def solution(id_pw, db):
#     if db_pw := dict(db).get(id_pw[0]):
#         return "login" if db_pw == id_pw[1] else "wrong pw"
#     return "fail"

#Hash
def solution(id_pw, db):
    dic = {i[0] : i[1] for i in db}
    if id_pw[0] in dic:
        if id_pw[1] == dic[id_pw[0]]:
            return "login"
        else:
            return "wrong pw"
    return "fail"