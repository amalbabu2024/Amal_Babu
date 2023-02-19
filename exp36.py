class rectangle():
    def __init__(self):
        self._length = int(input("Enter the Length:"))
        self._breadth = int(input("Enter the Breadth:"))
        self.area = self._length * self._breadth
    def greaterThan(self,rectangle):
        if self.area < rectangle.area:
            print("1 is Greater")
        else:
            print("2 is Greater")
r1=rectangle()
print("1:",r1.area)
r2=rectangle()
print("2:",r2.area)
r2.greaterThan(r1)
