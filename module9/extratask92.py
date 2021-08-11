import time

def memoize (func):
    memo = {}
    def wrapper (*args):
        start = time.time()
        if args in memo:
            fin = time.time() - start
            print(f"\nsquare root from {args[-1]} from memo {memo[args]}. it takes {fin}")
            
        else:
            result = args[-1] ** 0.5
            memo[args] = result
            fin = time.time() - start
            print(f"\nsquare root from {args[-1]} = {result}. it takes {fin}")    
          
    return wrapper    


@memoize
def listgen1(n):
    return [i for i in range(0,n) if i%2]


listgen1(13)
listgen1(13)
