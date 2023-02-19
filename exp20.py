n=int(input("Enter the elements:"))
print("Enter the elements")
list=[]
for i in range(0,n):
    ele=int(input())
    list.append(ele)
print(list)
for j in list:
    if(j%2==0):
        list.remove(j)
print(list)
