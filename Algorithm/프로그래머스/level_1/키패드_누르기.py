pos = [(3, 1),
       (0, 0), (0, 1), (0, 2),
       (1, 0), (1, 1), (1, 2),
       (2, 0), (2, 1), (2, 2)]

def diff(start, target):
    x, y = start
    return abs(x-pos[target][0]) + abs(y-pos[target][1])

def solution(numbers, hand):
    answer = ''

    pos_L = (3, 0) # * 왼손 엄지의 첫 위치
    pos_R = (3, 2) # # 오른손 엄지의 첫 위치

    for num in numbers:
        if num in [1, 4, 7]:
            answer += 'L'
            pos_L = pos[num]
        elif num in [3, 6, 9]:
            answer += 'R'
            pos_R = pos[num]
        else:
            l_len = diff(pos_L, num)
            r_len = diff(pos_R, num)

            if r_len > l_len:
                answer += 'L'
                pos_L = pos[num]
            elif r_len < l_len:
                answer += 'R'
                pos_R = pos[num]
            else:
                answer += hand[0].upper()
                if answer[-1] == 'L':
                    pos_L = pos[num]
                else:
                    pos_R = pos[num]

    return answer

# 상하좌우 이동, 거리만 생각해서 bfs 로 풀려했으나,
# 좌표간의 거리를 x,y 기준으로 계산만 하면 되는것이었다
# bfs로 짜려다가 수정하는 과정에서 시간을 좀 잡아먹었다
