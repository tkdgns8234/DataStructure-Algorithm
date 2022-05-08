N = int(input())
burst_time = sorted(map(int, input().split()))

turn_around_time = 0
ans = 0
for time in burst_time:
    turn_around_time += time
    ans += turn_around_time
print(ans)

