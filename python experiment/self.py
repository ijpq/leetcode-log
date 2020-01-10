class A():
    def __init__(self):
        print(self.__class__)
        self.x = 1
        pass
    def me(self):
        print(self.__class__)
class B(A):
    def __init__(self):
        
        super().__init__()
        print(self.__class__)
    
    def me(self):
        print(self.__class__)


if __name__ == '__main__':
    b = B()
    # A的self是b