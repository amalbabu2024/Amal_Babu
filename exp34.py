class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return(2*(self.length+self.breadth))
l=int(input("Enter the length : "))
b=int(input("Enter the breadth : "))
o=rectangle(l,b)
x=o.area()
y=o.perimeter()
print("The area is : ",x)
print("The Perimeter is : ",y)

l1=int(input("Enter the length: "))
b1=int(input("Enter the breadth: "))
o1=rectangle(l1,b1)
z=o1.area()
p=o.perimeter()
print("The area is :",z)
print("The Perimeter is :",p)

if(x>z):
    print("The First Rectangle is greater than Second Rectangle.")
else:
    print("The Second rectangle is greater than first rectangle")
