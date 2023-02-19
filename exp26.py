dict1={}
str1=input("Enter the string:")
print(str1)
for n in str1:
    if n in dict1:
        dict1[n]=dict1[n]+1
        print(dict1)
    else:
        dict1[n]=1
        print(dict1)
print("Character Frequency")
for i,v in dict1.items():
    print(i,v)
