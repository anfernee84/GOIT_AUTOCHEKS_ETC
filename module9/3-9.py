def caching_fibonacci():
    cache = {}
    def fibonacci(n):
        if n in cache:
            return cache[n]
        if n <= 1:
            return n
        fib = (fibonacci(n-1) + fibonacci(n-2))
        cache[n] = fib
        return fib
    return fibonacci


p = caching_fibonacci()
print(p(9))




# def make_cached_fib():
#     cache = {}
#     def _(n):
#         if n in cache:
#             return cache[n]
#         if n <= 1:
#             return n
#         fib = (_(n-1) + _(n-2)) % 10
#         cache[n] = fib
#         return fib
#     return _

# fib_last_digit_mem = make_cached_fib()
