'''
최단시간
30 이하의 자연수 중 소수구하기

import sys
def sosu(num):
    sosu_list = []
    
    for i in range(2, num+1):
        inc = 2
        Flag = True
        while inc <= i//2:
            if i % inc == 0:
                Flag = False
                break;
            inc += 1
        if (Flag):
            sosu_list.append(i)
    
    print(sosu_list)
        
    
num = int(sys.stdin.readline().strip())
sosu(num)
'''

'''
이진수 출력
import sys

def make_bin(num):
    bin_list = []
    i = num
    while i != 0:
        i,j = divmod(i, 2)
        bin_list.append(j)
        #bin_list.insert(0,j) 가 더 좋은방법
    result = bin_list[::-1]
    print(result)
    return

num = int(sys.stdin.readline().strip())
make_bin(num)
'''

'''
문제1
사용자로부터 날짜를 나타내는 세 개의 숫자를 입력받습니다. 첫 번째 숫자는 연도를 나타내는 네 자리 숫자이고, 두 번째 숫자는 월을, 세 번째 숫자는 일을 나타냅니다.

입력받은 날짜를 mm/dd/yyyy 형식으로 출력합니다. 월을 두 자리 숫자(01, 02, 03, ..., 12)로, 일을 두 자리 숫자(01, 02, 03, ..., 31)로, 연도를 네 자리 숫자로 나타냅니다.

입력받은 날짜의 다음 날에 해당하는 날짜도 같은 형식으로 출력합니다. 단, 윤년은 무시합니다(2월은 항상 28일까지 있다고 가정합니다).
import sys

def getnextdate(date):
    year, month, day = date
    ismaxday = {month:day} in [{1:31}, {2:28}, {3:31}, {4:30}, {5:31}, {6:30}, {7:31}, {8:31}, {9:30}, {10:31}, {11:30}, {12:31}]
    ismaxmonth = month == 12
    
    if ismaxday:
        day = 1
        if ismaxmonth:
            month = 1
            year += 1
        else:
            month += 1
    else:
        day += 1
    
    return year, month, day
    
def printdate(date):
    year, month, day = date
    print("%02d_%02d_%04d" %(day, month, year))


date = tuple(map(int, sys.stdin.readline().strip().split()))
printdate(date)
nextdate = getnextdate(date)
printdate(nextdate)
'''

'''
txt = 신경발달장애 Neurodevelopmental Disorders
조현병 스펙트럼 및 기타 정신병적 장애 Schizophrenia Spectrum and Other Psychotic Disorders
양극성 및 관련 장애 Bipolar and Related Disorders
우울장애 Depressive Disorders
불안장애 Anxiety Disorder
강박 및 관련 장애 Obsessive－Compulsive and Related Disorders
외상 및 스트레스 관련 장애 Trauma－and Stressor－Related Disorders
해리장애 Dissociative Disorders
신체증상 및 관련 장애 Somatic Symptom and Related Disorders
급식 및 섭식장애 Feeding and Eating Disorders
배설장애 Elimination Disorders
수면－각성 장애 Sleep－Wake Disorders
성기능부전 Sexual Dysfunctions
성별 불쾌감 Gender Dysphoria
파괴적, 충동조절 및 품행 장애 Disruptive, Impulse－Control, and Conduct Disorders
물질관련 및 중독 장애 Substance－Related and Addictive Disorders
신경인지장애 Neurocognitive Disorders
성격장애 Personality Disorders
변태성욕장애 Paraphilic Disorders
기타 정신질환 Other Mental Disorders
hos_dict = {}
is_eng = lambda x : ord('a') <= ord(str(x)) <= ord('z') or ord('A') <= ord(str(x)) <= ord('Z')

lines = txt.split('\n')
for line in lines:
    num = 0
    for word in line:
        if is_eng(word):
            hos_dict.update({line[:num-1:] : line[num::]})
            break;
        num += 1
print(hos_dict)
'''
'''
dict practice
#list
list1 = [1,2,3,4]
list2 = ['a','b','c','d']
dict1 = dict(zip(list1, list2))
#print(dict1)
#tuple
tp1 = 1,2
tp2 = 'a','b'
d1 = dict([tp1, tp2])
print(d1)
#dict
test = dict({1:2})
print(test)
test[2] = 3
print(test)
#add
'''
'''
리버스 반복
tlist = [1,2,3,4,5,6]
for i in tlist[len(tlist)//2::-1]:
    print(i)

ttuple = 1,2,3,4,5,6
for i in ttuple[2::-1]:
    print(i)
    
str1 = "python"
for i in reversed(str1):
    print(i)
print(str(reversed(str1)))
'''
'''
대각선 별 출력
for i in range(5):
    print(' ' * i, "*", sep='')
'''
'''
collections 라이브러리 활용 양뱡향 queue 구현
from collections import deque

a = deque([1,2,3,4,5])
a.append(500)
print(a)
a.pop()
print(a)
a.popleft()
print(a)
'''

'''
enumerate 를 활용한 index, value 동시출력
l = ['a','b','c','d']
for i,v in enumerate(l):
    print("index= ", i, "val= ", v)
'''

'''
최대 최솟값 구하기
l = [1,19,20,14,5,7]
l.sort()
#print("first= ", l[0], "last= ", l[len(l)-1])
#print(l)
print(min(l))
print(max(l))
'''

'''
comprehension (리스트 안에서 반복문 및 조건문 돌리기)
ex 홀수 구구단 한줄출력
l = list(i * j for i in range(1,10) if i % 2 != 0 for j in range(1,10) if j % 2 != 0)
print(l)
'''
'''
l = [1,2,3,4,5]
print(l.index(5))
'''

'''
리스트 표현식 안에서 0으로 초기화된 2차원 리스트 만들기
l = [[0 for i in range(2)] for j in range(3)]
print(l)
'''

'''
리스트간 덧셈 /곱셈 /뺄셈은 지원 안함
l1 = [1,2,3,4,5]
l2 = [1,2,3,4,5]
print(l1*l2)
'''

'''
문자열 -> 리스트
리스트 -> 문자열
tstr = 'python'.upper()
print(tstr)
tstr = list(tstr)
print(tstr)
strt = ''.join(tstr)
print(strt)
'''

'''
#dict update
#1
t = dict()
t['1'] = 3
print(t)
#2
#숫자는안됨
t = dict()
t.update(a = 32)
print(t)
#3
t = dict()
t.setdefault('a')
print(t)
t = dict()
t.update({1:23})
print(t)
'''

'''
dict 키 출력
dict 값 출력
dict 키 값 동시 출력
dict1 = dict({1:2,2:5,3:4,4:1,5:2})
# for i in dict1:
#     print(i)
# for i in dict1.values():
#     print(i)
# for key, value in dict1.items():
#     print(key, value)
'''
'''
list = list()
list.append

dict = dict()
dict.update

test = set()
test.add(5)
print(test)
'''

'''
file
lines = ['안녕하세요\n', '파이썬\n', '정상훈\n']

with open('hello.txt', 'w') as file:
    file.writelines((lines))


file = open('hello.txt', 'r')

line = None
while line != '':
    line = file.readline()
    print(line.strip())
    
file = open('hello.txt', 'r')
for line in file:
    print(line.strip())
file.close()

'''



'''
회문 판별하기
import sys

# word = sys.stdin.readline().strip()
# ish = True
#1 반복문 사용
# for i in range(len(word)//2):
#     if word[i] != word[-1 -i]:
#         ish = False
#         break;
# print(ish)
#2 [::] 사용
# if word == word[::-1]:
#     print('true')
#3 reverse 사용
# print(word)
# print(list(reversed(word)))
# strt = 'word'
# print(list(strt))
# l = list(reversed(list(strt)))
# print(l)
'''

'''
재귀 호출로 팩토리얼 구하기

def reculsive_fac(num):
    #종료조건
    if num == 1:
        return 1
    
    #어떤식이어야하는지
    return num * reculsive_fac(num - 1)
    
print(reculsive_fac(5))
'''

'''
커스텀 iter 만들기
class CustomIter:
    
    def __init__(self, stop):
        self.count = 0
        self.stop = stop
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count < self.stop:
            self.count += 1
            return self.count-1
        else:
            raise StopIteration
        
c_iter = CustomIter(5)

for i in c_iter:
    print(i)
'''

#최소공배수 최소의 연산 mod 로 풀기

import sys

num1, num2 =  map(int, sys.stdin.readline().strip().split())

while num1 != 0 and num2 != 0:
    if num1>num2:
        num1 = num1%num2
    else:
        num2 = num2%num1
print("최소 공배수: {}".format(num1+num2))

#최대 공약수 구하기
#세가지 방법이 있다 1. minus 연산 2. 나머지 연산 3. 재귀적 호출
# 나머지 연산을 사용하는것이 효율적이다

import sys
num1, num2 = map(int, sys.stdin.readline().strip().split())

while num1 != 0 and num2 != 0:
    if num1 > num2:
        num1 = num1%num2
    else:
        num2 = num2%num1

print("최대공약수 = {}".format(num1 + num2))