from array import *

array1=array('i',[10,20,30])
for i in array1:
    print(i)
    print(array1[0])
array1.insert(1,60)

print (array1[1])

array1.remove(60)
print(array1[1])
print(array1.index(20))

li=[]

li.append(5)

m=[5]*4
print(li)
del li[0]
print(m)

tu=(50,)
print(tu)
print(type(tu))

print(tu)

print(tu.count(50))


dic={1:"hllo",2:"hhh"}
print(dic[1])
print("tuple is ",tu)


M={"Mon","Tue","Wed","Thu","Fri","Sat","Sun"}
print(type(M))



