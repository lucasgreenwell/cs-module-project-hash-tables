import math
import random
# Your code here

cache = {}
def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v


# def cache_factorial(num, cache):
#     if num in cache:
#         return cache[num]
#     if num is 0:
#         return 1
#     else:
#         # print(num)
#         x = num * cache_fa%= 982451653l(num - 1, cache)
#         cache[num] = x
#         return [cache[num]]

powers = {}
factorials = {}
results = {}

def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    input = (x, y)
    if input not in results:
        if input in powers:
            power = powers[input]
        else:
            powers[input] = math.pow(x,y)
            power = powers[input]
        if power in factorials:
            factorial = factorials[power]
        else:
            factorials[power] = math.factorial(power)
            factorial =  factorials[power]
        res = factorial // sum(input)
        res %= 982451653
        results[input] = res
        return results[input]
    else:
        return results[input]





# Do not modify below this line!

for i in range(5000000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
