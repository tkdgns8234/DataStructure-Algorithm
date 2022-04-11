# # LRU: Least Recently Used 페이징 알고리즘 중 하나
# # 가장 오랫동안 사용되지 않은 페이지를 교체하는 방식
# # https://dailylifeofdeveloper.tistory.com/355
#
# import collections
#
# CACHE_HIT = 1
# CACHE_MISS = 5
#
# def solution(cacheSize, cities):
#     if cacheSize == 0:
#         return len(cities)*5
#
#     answer = 0
#     cache = collections.deque()
#
#     for city in list(map(str.upper, cities)):
#         # 캐시 적중이면
#         if city in cache:
#             cache.remove(city)
#             cache.append(city)
#             answer += CACHE_HIT
#         # 캐시 미적중
#         else:
#             # 캐시에 공간이 있는 경우
#             if len(cache) < cacheSize:
#                 cache.append(city)
#                 answer += CACHE_MISS
#             # 캐시가 꽉 찬 경우
#             else:
#                 cache.popleft()
#                 cache.append(city)
#                 answer += CACHE_MISS
#     return answer
#
# v = solution(0,["Jeju", "Pangyo", "Seoul", "NewYork", "LA"])
# print(v)


# deque의 maxlen을 이용한 더 좋은 코드
def solution(cacheSize, cities):
    import collections
    cache = collections.deque(maxlen=cacheSize)
    time = 0
    for i in cities:
        s = i.lower()
        if s in cache:
            cache.remove(s)
            cache.append(s)
            time += 1
        else:
            cache.append(s)
            time += 5
    return time
