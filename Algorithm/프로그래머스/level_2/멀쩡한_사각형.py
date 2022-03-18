import math
def solution(w,h):
    return w*h - (w+h-1*math.gcd(w, h))