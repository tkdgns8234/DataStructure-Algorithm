# 제대로 설계하지 않고 풀이해서 어려웠다.
# action, uid 저장
# dict 형태로 uid 를 key 로 가지는 name 관리

def solution(record):
    answer = []
    actions = []
    user_db = {}

    for event in record:
        info = event.split()
        action, uid = info[0], info[1]
        if action in ['Enter', 'Change']:
            name = info[2]
            user_db[uid] = name
        actions.append((action, uid))

    for action_info in actions:
        action, uid = action_info[0], action_info[1]
        if action == 'Enter':
            answer.append(f'{user_db[uid]}님이 들어왔습니다.')
        elif action == 'Leave':
            answer.append(f'{user_db[uid]}님이 나갔습니다.')

    return answer