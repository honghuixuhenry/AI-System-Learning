
# memo = {}

# def fib(n):
#     if n in memo:
#         return memo[n]
#     if n <= 1:
#         return n
#     memo[n] = fib(n-1) + fib(n-2)

#     return memo[n]


def fib_dp(n):
    if n<= 1:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

def fib_recur(n):
    if n <= 1:
        return n
    return fib_recur(n-2) + fib_recur(n-1)

print(fib_dp(10))
print(fib_recur(10))