def solution(phone_number):
    return phone_number[len(phone_number) - 4:].rjust(len(phone_number), '*')

solution("01033334444")