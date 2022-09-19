
def rotation(array):
    x = len(array)
    y = len(array[0])

    temp = [[0] * y for _ in range(x)]

    for i in range(x):
        for j in range(y):
            temp[j][x - i - 1] = array[i][j]

    return temp

def isMatched(newLock):
    length = len(newLock) // 3

    for i in range(length, length * 2):
        for j in range(length, length * 2):
            if newLock[i][j] != 1:
                return False

    return True


def solution(key, lock):
    l = len(lock)
    kl = len(key)

    newLock = [[0] * l * 3 for _ in range(l * 3)]

    for i in range(l):
        for j in range(l):
            newLock[i + l][j + l] = lock[i][j]

    for _ in range(4):
        key = rotation(key)

        for i in range(l * 2):
            for j in range(l * 2):

                for k in range(kl):
                    for m in range(kl):
                        newLock[k + i][m + j] += key[k][m]

                if isMatched(newLock):
                    return True

                for k in range(kl):
                    for m in range(kl):
                        newLock[i + k][j + m] -= key[k][m]

    return False


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
