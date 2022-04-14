# lock 의 크기를 3배로 만들어
# key 를 회전 + 움직이며 들어맞는지 확인하는 방법


def get_new_lock(lock):
    m = len(lock)
    new_lock = [[0]*(m*3) for _ in range(m*3)]
    for i in range(m):
        for j in range(m):
            new_lock[m+i][m+j] = lock[i][j]
    return new_lock

def confirm(new_lock):
    rock_l = len(new_lock)//3
    for i in range(rock_l, rock_l+rock_l):
        for j in range(rock_l, rock_l + rock_l):
            if new_lock[i][j] != 1:
                return False
    return True

def set_key(i, j, n, key, new_lock):
    key_l = len(key)
    for r in range(key_l):
        for c in range(key_l):
            if key[r][c] == 1:
                new_lock[i+r][j+c] += n
    return


def rotate(key):
    key_l = len(key)
    temp = [[0] * key_l for _ in range(key_l)]
    for i in range(key_l):
        for j in range(key_l):
            temp[j][key_l-i-1] = key[i][j]
    return temp

def solution(key, lock):
    new_lock = get_new_lock(lock)

    lock_l = len(new_lock)
    key_l = len(key)

    for _ in range(4):
        key = rotate(key)
        for i in range(lock_l-key_l):
            for j in range(lock_l-key_l):
                set_key(i, j, 1, key, new_lock)
                if confirm(new_lock):
                    return True
                set_key(i, j, -1, key, new_lock)
    return False
# v = solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]])
# print(v)



# 원래 나의 풀이 이게 좀 더 간결
def rotation(key):
    col = len(key)
    row = len(key[0])
    new_key = [[0]*col for _ in range(row)]
    for i in range(row):
        for j in range(col):
            new_key[j][row-i-1] = key[i][j]
    return new_key

def is_correct(new_lock):
    length = len(new_lock)
    for i in range(length//3, length-length//3):
        for j in range(length // 3, length - length // 3):
            if new_lock[i][j] != 1:
                return False
    return True


def solution(key, lock):
    n = len(key)
    m = len(lock)
    new_lock = [[0]*(m*3) for _ in range(m*3)]
    # new_lock 초기화
    for i in range(m):
        for j in range(m):
            new_lock[i+m][j+m] = lock[i][j]

    # 회전4번
    for _ in range(4):
        key = rotation(key)

        # key 이동
        for i in range(m*2):
            for j in range(m*2):
                # key 대입
                for a in range(n):
                    for b in range(n):
                       new_lock[i+a][j+b] += key[a][b]

                if is_correct(new_lock):
                    return True
                # key 빼기
                for a in range(n):
                    for b in range(n):
                       new_lock[i+a][j+b] -= key[a][b]
    return False