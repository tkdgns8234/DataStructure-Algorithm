# 좌표입력, 좌표출력 형태의 문제의 경우
# 직접 배열을 만들지 않고 계산, return 할 수도있다.
# 때론 그렇게 구현하는게 훨씬 간결하다
REMOVE = 0
BUILD = 1

G = 0 # 기둥
B = 1 # 보

def confirm(y, x, a, answer):
    if a == G:  # 기둥인 경우
        if x == 0 or [y, x - 1, G] in answer or ([y - 1, x, B] in answer or [y, x, B] in answer):
            return True
    elif a == B: # 보인 경우
        if [y, x-1, G] in answer or [y+1, x-1, G] in answer or ([y-1, x, B] in answer and [y+1, x, B] in answer):
            return True
    return False

def build(y, x, a, b, answer):
    if b == BUILD:
        if confirm(y,x,a,answer):
            answer.append([y,x,a])
    elif b == REMOVE:
        answer.remove([y,x,a])
        for ans in answer:
            if confirm(*ans, answer) == False:
                answer.append([y,x,a]) #없어지면 안되는 경우 다시 짓기
                break


def solution(n, build_frame):
    answer = []
    for y,x,a,b in build_frame: #x,y,0기동1보,0삭제1설치
        build(y, x, a, b, answer)

    return sorted(answer)
#
# print(solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))



# 원래 코드
# Q12 기둥과 보 설치
def condition(answer):
    for ans in answer:
        x, y, what = ans
        # 기둥
        if what == 0:
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
                continue
            return False
        # 보
        elif what == 1:
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or [x-1, y, 1] in answer and [x+1, y, 1] in answer:
                continue
            return False
    return True


def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        # x, y, 기둥/보, 삭제/설치
        x, y, what, action = frame
        # 삭제
        if action == 0:
            answer.remove([x, y, what])
            if not condition(answer):
                answer.append([x, y, what])
        # 설치
        elif action == 1:
            answer.append([x, y, what])
            if not condition(answer):
                answer.remove([x, y, what])
    answer.sort()
    return answer