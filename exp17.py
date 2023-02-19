d={1:3,4:2,8:7,6:5}
print(d)
sorted_d=sorted(d.items())
print("the dct in ascending order by value:",sorted_d)
sorted_d=sorted(d.items(),reverse=True)
print("the dict in descending order by value:",sorted_d)
