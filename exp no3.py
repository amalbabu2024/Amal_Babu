list1=[1,-2,3,-4,5,6,-7,8,-9,10]
lsta=[]
print("list:",list1)
for num in list1:
    if num>=0:
        lsta.append(num)
print("the list of positive numbers are {}\n".format(lsta))

list2=[1,2,3,4,5,34,6,78,4,8]
lstb=[]
print("list:",list2)
for n in list2:
    lstb.append(n**2)
print("square of list:{}\n".format(lstb))
n=input("Enter a word:")
vowels=['a','e','i','o','u']
lst=[]
for x in n:
    if x in vowels and x not in lst:
        lst.append(x)
print("vowels from list are:",lst)