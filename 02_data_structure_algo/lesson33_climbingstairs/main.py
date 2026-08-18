def climb_stairs(n):
    if n <= 2:
        return n
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]


def climb_stairs_save_memory(n):
    if n<=2:
        return n
    first = 1
    second = 2

    for i in range(3, n+1):
        current = first + second
        first = second
        second = current

    return current

print(climb_stairs(5))
print(climb_stairs_save_memory(5))
