# assignment-2.-23-02-22
Write a program to print reverse of a elements in list
  

a=[]
n=int(input('Enter n:'))
for i in  range(n):
    d=int(input())
    a.append(d)
print('mylist before reverse:',a)
a2=a
a2.reverse()
print('mylist after reverse',a2)


Enter n:4
23
25
36
56
mylist before reverse: [23, 25, 36, 56]
mylist after reverse [56, 36, 25, 23]
