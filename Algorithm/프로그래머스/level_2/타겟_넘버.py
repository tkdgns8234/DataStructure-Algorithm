# 정석풀이로 잘 풀었다
# itertools로 짜보는건 다시 해보는게 좋을거같다
def solution(numbers, target):
    answer = 0

    def btk(depth, total):
        if depth == len(numbers):
            if total == target:
                nonlocal answer
                answer += 1
            return

        btk(depth + 1, total + numbers[depth])
        btk(depth + 1, total - numbers[depth])

    btk(0, 0)
    return answer

v = solution([1, 1, 1, 1, 1], 3)
print(v)

# 좋은 풀이
# 와.. 이건 감탄스럽고 아름답다
def solution(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])


# 와.. itertools도 될거라 예상은 했지만 가능하네
# 이것 또한 아름답다
from itertools import product
def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)