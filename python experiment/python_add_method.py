class CLS():
    def __init__(self):
        pass

    def method1(self):
        print('method1 declaried within class')
    
def method1():
    print('method1 declaried out from class')

if __name__ == '__main__':
    obj = CLS()
    obj.method1()
    obj.method1=method1
    obj.method1()