def log(func):
    def wrapper(*args,**kwargs):
        print('before wrapper')
        return func(*args,**kwargs)
    return wrapper

class CLS():
    def __init__(self):
        print('init')

    
    
    @log # eqs under_wrapper = log(under_wrapper)
    def under_wrapper(self,*args,**kwargs):
        print('args',args)
        print('kwargs',kwargs)
        print(self.__class__.__name__)

f=CLS()
f.under_wrapper(1,2,3)
#under_wrapper(1,2,3) = log(under_wrapper)(1,2,3)