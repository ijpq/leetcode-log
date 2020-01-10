class CLS():
    def x(self,a):
        self.aa=a

c = CLS()
c.x(1)
print(dir(c))
print(c.__dict__)