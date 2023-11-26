#Example of using list#


myList=[1, 2, 'a', 4, 5]
print(myList) 
myList[2]=3
print(myList)
print("---------------------")

#Sort the list
v= [1, 2, 3, 44, 5, 7, 9]
v.sort()
print(v)

print("---------------------")

#append and insert
fr=['a','c','d']
fr.insert(1, 'b')
fr.append('e')
print(fr)

print("---------------------")

#pop (remove last elemnt of list) and remove
fr=['a','b','c','d']
fr.pop()
fr.remove('b')
print(fr)

print("---------------------")

#more example for pop (important)
fr=['a','b','c','d']
old_valu = fr.pop(-1)
print(old_valu)
print(fr)

print("---------------------")

#To know the index
fr=['a','c','d']
n = fr.index('c')
print(n)

print("---------------------")

l=[8, 11, 2, 4]
for i in range(len(l)):
    print(i)
print("---------------------")

ll=[8, 11, 2, 4]
for i in range(len(ll)):
    print(ll[i])
    
print("---------------------")

lll=[8, 11, 2, 4]
for i in lll:
    print(i)
    
print("---------------------")

#for

lll=[8, 11, 2, 4]
for i in lll:
    print(i ,end=" ")
    
print()
print("---------------------") 


lll=[8, 11, 2, 4]
total=0
for i in lll:
    total +=i
print(total)

print("---------------------")

##split: take the information to split##
s= "a,b,c"
list_ = s.split(',')
print(list_)

print("---------------------")

##copy list and change new copy
list_=[1 ,2 ,3 ,4]
x = list_
x[2] = 5
print(x)

print("---------------------")

##copy list and change new copy
list_=[1 ,2 ,3 ,4]
x = list_.copy()
x[2] = 5
print(x)
print(list_)

print("---------------------")

lll=[1, 2, 3]
total=1
for i in lll:
    i *=2
    print(i)

print("---------------------")
print("---------------------")

##Pos and Neg numbers
x= [-1, 2 , 3 , -5, 6]
c=0
cP=0
for i in x:
    if(i < 0 ):
        c +=1
    else:
        cP +=1
print("Negative elemnts: ",c)
print("Postive or zero elemnts: ",cP)

print("---------------------")

#List > 100
x=[100, 9,201, 99, 101]

for i in x:
    if (i > 100):
        print(i)
        print(x.index(i))
        break