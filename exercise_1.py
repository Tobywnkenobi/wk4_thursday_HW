fib_cache = {}


# def memoize(f):
#     cache = {}
#     count = 0 
#     def kendrick_lamar(num):
#         if num not in cache:
#             cache[num] = f(num)
#         return cache[num], count
#     return kendrick_lamar





# @memoize
def fib_memo(num):
    if num <= 1:
        return 1
    if num not in fib_cache:
        fib_cache[num] = fib_memo(num - 1) + fib_memo(num - 2)
    return fib_cache[num]


print(fib_memo(19))
print(fib_memo(9))
print(fib_memo(6))
print(fib_memo(39))
print(fib_memo(41))
print(fib_memo(59))




