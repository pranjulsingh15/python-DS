import time

start_time = time.time()
n = int(input("Enter the input for which fibonacci to be calculated"))


def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 2) + fib(n - 1)


for i in range(n):
    print(fib(i), end=" ")

print("--- %s seconds ---" % (time.time() - start_time))
