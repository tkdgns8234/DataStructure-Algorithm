def solution(s):
    answer = len(s)

    for jump in range(1, len(s) // 2 + 1):
        result = ""
        before = s[0:jump]
        cnt = 1

        for i in range(jump, len(s), jump):
            word = s[i:i + jump]

            if before == word:
                cnt += 1
            else:
                result += (str(cnt) + before) if cnt > 1 else before
                cnt = 1
                before = word

        result += (str(cnt) + before) if cnt > 1 else before

        answer = min(answer, len(result))
    return answer


print(solution("a"))
