def log(func):
    def wrapper(*args,**kwargs):
        print('before wrapper')
        print('args', args)
        print('kwargs', kwargs)
        return func(*args,**kwargs)
    return wrapper

class CLS():
    def __init__(self):
        print('init')

    
    
    @log # eqs under_wrapper = log(under_wrapper)
    def under_wrapper(self,*args,**kwargs):
        print('within function under_wrapper')
        print(self.__class__.__name__)
if __name__ == '__main__':
    f=CLS()
    f.under_wrapper()
    ##############################
    # 请检查运行结果是否与理解一致:
    # 理解:
    # f.under_wrapper 等价于 log(under_wrapper) 等价于 wrapper(under_wrapper) 等价于 print(),print(),print(), under_wrapper(*args,**kwargs)
    # 运行结果:
    # init
    # before wrapper
    # args (<__main__.CLS object at 0x1038eed68>,)
    # kwargs {}
    # within function under_wrapper
    # CLS
    # before wrapper
    # args (<__main__.CLS object at 0x1038eed68>, 1, 2, 3)
    # kwargs {}
    # within function under_wrapper
    # CLS
    ##############################
    f.under_wrapper(1,2,3)
    #under_wrapper(1,2,3) = log(under_wrapper)(1,2,3)
