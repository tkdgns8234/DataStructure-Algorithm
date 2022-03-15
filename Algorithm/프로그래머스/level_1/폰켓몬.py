def solution(nums):
    answer = len(nums)//2
    if answer > len(set(nums)):
        answer = len(set(nums))
    return answer