n = int(input())
h = list(map(int, input().split()))
dp = [0] * n
for i in range(1, n):
    one_jump = dp[i - 1] + abs(h[i] - h[i - 1])
    if i > 1:
        two_jump = dp[i - 2] + abs(h[i] - h[i - 2])
        dp[i] = min(one_jump, two_jump)
    else:
        dp[i] = one_jump
print(dp[-1])