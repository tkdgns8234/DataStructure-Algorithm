# 라디오에서 들은 멜로디와 동일한 멜로디를 가진 노래 출력하는 문제
# 노래가 반복재생될 수 있는게 포인트

def get_time(t):
    hour, minute = t.split(':')
    return int(hour)*60 + int(minute)

def get_melody(melody, time):
    rs = []
    now = 0
    while time >= 0:
        time -= 1

        if now == len(melody):
            now = 0

        if now + 1 < len(melody) and melody[now + 1] == '#':
            rs.append(melody[now]+'#')
            now += 2
        else:
            rs.append(melody[now])
            now += 1

    return "".join(rs)


def solution(m, musicinfos):
    answer = []

    for idx, info in enumerate(musicinfos):
        info = info.split(',')
        run_time = 0
        start = get_time(info[0])
        end = get_time(info[1])
        if start > end:
            # 00:00 시를 넘기지 않는다
            run_time = 24*60 - start
        else:
            run_time = end - start

        melody = get_melody(info[3], run_time).replace(m, '!')
        # C와 C# 구분
        for i, mel in enumerate(melody):
            if i < len(melody) - 1:
                if mel == '!' and melody[i+1] != '#':
                    answer.append((run_time, idx, info[2]))

    if not answer:
        return '(None)'
    else:
        answer.sort(key=lambda x: (-x[0], x[1]))
        return answer[0][2]

ans = solution("ABCDEFG", ["23:4,02:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"])
print(ans)


# 훨씬 더 좋은 코드
# 내 코드에 비해 개선된 점:
# 1. 00:00 시를 넘기지 않는다 라는 조건은 내가 처리하라는게 아니었어, 그냥 그런 입력 자체가 없다는거였어
# 2. c#, c 를 어떻게 처리할 것인가 -> 그냥 replace 떄려버리고 계산
# 3. 재생 시간만큼 멜로디를 만드는 방법 (아래 코드의 full_notes)

def shap_to_lower(s):
    s = s.replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a')
    return s

def solution(m,musicinfos):
    answer=[0,'(None)']   # time_len, title
    m = shap_to_lower(m)
    for info in musicinfos:
        split_info = info.split(',')
        time_length = (int(split_info[1][:2])-int(split_info[0][:2]))*60+int(split_info[1][-2:])-int(split_info[0][-2:])
        title = split_info[2]
        part_notes = shap_to_lower(split_info[-1])
        full_notes = part_notes*(time_length//len(part_notes))+part_notes[:time_length%len(part_notes)]
        if m in full_notes and time_length>answer[0]:
            answer=[time_length,title]
    return answer[-1]
