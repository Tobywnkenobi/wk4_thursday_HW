fib_cache = {}

def fib_memo(num):
    if num <= 1:
        return 1
    if num not in fib_cache:
        fib_cache[num] = fib_memo(num - 1) + fib_memo(num - 2)
    return fib_cache[num]

print(fib_memo(9))


