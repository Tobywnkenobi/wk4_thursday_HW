# decorator, with a wrapper


def count_calls(f):
    def biggie_smalls(*args):
        biggie_smalls.call_count += 1
        return f(*args)
    
    biggie_smalls.call_count = 0
    return biggie_smalls




#the fib memo below, using the decorator count_calls


fib_cache = {}

@count_calls
def fib_memo(num):
    if num <= 1:
        return 1
    if num not in fib_cache:
        fib_cache[num] = fib_memo(num - 1) + fib_memo(num - 2)
    return fib_cache[num]

# print(fib_memo(9))

for t in range(1, 11):
    test_result = fib_memo(t)
    print(f"fib({t}) = {test_result}, Function Calls = {fib_memo.call_count}")

