list1=[1,2,3,4]
list2=[5,3,7,8]
total=0
final=0
a=len(list1)
b=len(list2)
if(a==b):
    print("list1 and list2 are same length")
for i in range(0,len(list1)):
    total=total+list1[i]
print(total)
for j in range(0,len(list2)):
    final=final+list2[j]
print(final)
z=total+final
print("sum of 2 lists:",z)
if(total==final):
    print("lists sum to the same value")
else:
    print("sum of both list haven't the same")
c=list(set(list1).intersection(list2))
print(c)
