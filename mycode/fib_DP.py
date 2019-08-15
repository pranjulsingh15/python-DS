import time

start_time = time.time()
n = int(input("Enter the input for which fibonacci to be calculated"))
memo = [0] * (n +1)


def fib(n):
    memo[0], memo[1] = 0, 1
    for i in range(2, n + 1):
        memo[n] = memo[n - 1] + memo[n - 2]
    return memo[n]


if __name__ == '__main__':
    for i in range(100):
        print(fib(i), end=" ")
print()
print("--- %s seconds ---" % (time.time() - start_time))
