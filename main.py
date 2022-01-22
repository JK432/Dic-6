# Write a python program to read two dictionaries and print a new dictionary, concatenating the other two dictionary 
l= {"name","age"}
j= {"phoneno","adress"}
dict1 = {}
dict2 = {}

for k in j:
  print("enter ",k)
  dict1[k]= input()
for k in l:
  print("enter ",k)
  dict2[k]= input()
print("dict1 =")
print(dict1)
print("dict2 =")
print(dict2)
print("After merging")
dict2.update(dict1)
 

print(dict2)