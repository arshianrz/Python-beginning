#!/usr/bin/python

counter = 100
total = 139.1853
name = "arshia"

print(counter,total,name,"testing print func")
a,b,c = 96.22 , "mood" , [1,2,3]
print(a,b,c)

del a,b,c

#print(a,b,c) #occurs to an error

print(name[0:])
print(name*2)

list_variable = ['john',18 ,[0,3]]

print(list_variable[2])

tuple_variable = (1,3,"str")

list_variable.append(tuple_variable)

p = print(list_variable)

p

print((tuple_variable[2])[-1]) #-1 returns last element

minidict = {'user' : 'mamad' , 'code' : 1239 , 'car' : 'peikan' , 'test' : 8698}

minidict.__delitem__('test')

print(minidict.fromkeys(minidict))

print(minidict.keys(),minidict.values())

print(minidict.items())

print(int("12",10),hex(128))

miniset = {'09335412416' , '0912666888' , '09112589669'}

print('09112589669' in miniset)
