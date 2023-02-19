string1=input("Enter the first character")
string2=input("Enter the second character")
a=string1[0]
b=string2[0]
new_str1=string2[0]+string1[1:]
new_str2=string1[0]+string2[1:]
print(new_str1+" "+new_str2)
