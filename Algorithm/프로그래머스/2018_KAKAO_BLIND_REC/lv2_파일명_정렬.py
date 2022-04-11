# 이 코드 자꾸 일부 테케에서 런타임 에러가 발생해서
# 매우 고생했다;
# NUM 값을 구하는 과정에서 인터프리터마다 error를 잡는게 다른거같음
# 아마 list slice 할 때 문제인듯 NUM = file[start:end+1]
# 다시 푼 코드 아래 확인
def solution(files):
    dic = dict()
    for file in files:
        HEAD, NUM = '', 0
        for i, word in enumerate(file):
            if word.isnumeric():
                start = i
                #최초 발견 시점 부터 5 글자 확인
                for c in range(0, 5):
                    if i+c < len(file) and file[i+c].isnumeric():
                        end = i+c
                HEAD = file[:start]
                NUM = file[start:end+1]
                dic[file] = (HEAD.upper(), int(NUM))
                break
    return sorted(files, key=lambda x: (dic[x][0], dic[x][1]))

v = solution( ['F15','FFFFFFFFFF1'])
print(v)





# 최종코드

def solution(files):
    dic = dict()
    for file in files:
        HEAD, NUM = '', ''
        for i, word in enumerate(file):
            if word.isnumeric():
                start = i
                for c in file[start:]:
                    if not c.isnumeric():
                        break
                    NUM += c

                HEAD = file[:start]
                dic[file] = (HEAD.upper(), int(NUM))
                break
    return sorted(files, key=lambda x: (dic[x][0], dic[x][1]))

v = solution( ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"])
print(v)