import time



def testtime(func):
    def wrapper (*args, **kwargs):
        start = time.time()
        func (*args,**kwargs)
        fin = time.time() - start
        print (f"Worktime = {fin}")
    return wrapper

@testtime
def nod(x,y):
    while x != y:
        if x > y:
            x -= y
        else:
            y -= x
    return x



nod(1000000,2)
