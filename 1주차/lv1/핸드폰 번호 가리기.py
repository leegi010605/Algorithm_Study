def solution(phone_number):
    return phone_number.replace(phone_number[:-4],"*"*int(len(phone_number)-4))