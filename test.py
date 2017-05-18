# for n in range(2, 100):
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, 'is not prime number')
#             #break
#         else:
#         # loop fell through without finding a factor
#             print(n, 'is a prime number')


def fib(n):
    result = []
    a,b=0,1
    while a < n:
        result.append(a)
        print(result)
        a,b=b,a+b
#
# fib(100)

# def increment(a):
#     return lambda x: x+a
#
#
# f=increment(4)
# print(f(100))

# vec = [-4, -2, 0, 2, 4]
# print( [x ** 2 for x in vec])

# knights = {'gallahad': 'the pure', 'robin': 'the brave'}
# for k, v in knights.items():
#     print(k,v)

# print((1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4))

# if __name__ == "__main__":
#     import sys
#     fib(int(sys.argv[1]))

# print(repr('hello'))

# def scope_test():
#     def do_local():
#         spam = "local spam"
#
#     def do_nonlocal():
#         nonlocal spam
#         spam = "nonlocal spam"
#
#     def do_global():
#         global spam
#         spam = "global spam"
#
#     spam = "test spam"
#     do_local()
#     print("After local assignment:", spam)
#     do_nonlocal()
#     print("After nonlocal assignment:", spam)
#     do_global()
#     print("After global assignment:", spam)
#
# scope_test()
# print("In global scope:", spam)

# import os
# def print_directory_contents(sPath):
#     import os
#     for sChild in os.listdir(sPath):
#         sChildPath = os.path.join(sPath,sChild)
#         if os.path.isdir(sChildPath):
#             print_directory_contents(sChildPath)
#         else:
#             print(sChildPath)
#
#
# def print_dir(sPath):
#     for sChild in os.listdir(sPath):
#         sChildPath=sPath+'/'+sChild
#         if os.path.isdir(sChildPath):
#             print_dir(sChildPath)
#         else:
#             print(sChildPath)
#
# print_dir(os.getcwd())

# A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
# A1 = range(10)
# A2 = sorted([i for i in A1 if i in A0])
# A3 = sorted([A0[s] for s in A0])
# A4 = [i for i in A1 if i in A3]
# A5 = {i:i*i for i in A1}
# A6 = [[i,i*i] for i in A1]
#
# print(A6)

# def f(x,l=[]):
#     for i in range(x):
#         l.append(i*i)
#     print(l)
#
# f(2)
# f(3,[3,2,1])
# f(3)

# class A(object):
#     def go(self):
#         print("go A go!")
#     def stop(self):
#         print("stop A stop!")
#     def pause(self):
#         raise Exception("Not Implemented")
#
# class B(A):
#     def go(self):
#         super(B, self).go()
#         print("go B go!")
#
# class C(A):
#     def go(self):
#         super(C, self).go()
#         print("go C go!")
#     def stop(self):
#         super(C, self).stop()
#         print("stop C stop!")
#
# class D(B,C):
#     def go(self):
#         super(D, self).go()
#         print("go D go!")
#     def stop(self):
#         super(D, self).stop()
#         print("stop D stop!")
#     def pause(self):
#         print("wait D wait!")
#
# class E(B,C): pass
#
# a = A()
# b = B()
# c = C()
# d = D()
# e = E()
#
# # a.go()
# # b.go()
# # c.go()
# d.go()

# class BinaryTree():
#
#     def __init__(self,rootid):
#       self.left = None
#       self.right = None
#       self.rootid = rootid
#
#     def getLeftChild(self):
#         return self.left
#     def getRightChild(self):
#         return self.right
#     def setNodeValue(self,value):
#         self.rootid = value
#     def getNodeValue(self):
#         return self.rootid

# def f1(lIn):
#     l1 = sorted(lIn)
#     l2 = [i for i in l1 if i<0.5]
#     return [i*i for i in l2]
#
# def f2(lIn):
#     l1 = [i for i in lIn if i<0.5]
#     l2 = sorted(l1)
#     return [i*i for i in l2]
#
# def f3(lIn):
#     l1 = [i*i for i in lIn]
#     l2 = sorted(l1)
#     return [i for i in l1 if i<(0.5*0.5)]
#
# import cProfile
# import random
# lIn = [random.random() for i in range(10)]
# # cProfile.run('f1(lIn)')
# # cProfile.run('f2(lIn)')
# # cProfile.run('f3(lIn)')

# def multipliers ():
#
#     return [lambda x: i * x for i in range (4)]
#
# print ([m (2) for m in multipliers ()])

#linearsearch
# def linearSearch(myItem,Mylist):
#     found =False
#     postion = 0
#     while ((postion<len(Mylist)) & (found ==False)) :
#         if (Mylist[postion] == myItem):
#             found = True;
#         postion = postion+1
#     print(postion)
#     return postion
#
# shopping =['apple','banana','orange','mango']
# item = 'mango'
#
# linearSearch(item,shopping)

#binarysearch

# def binarySearch(myItem,Mylist):
#     lo = 0
#     hi = len(Mylist)-1
#     postion = 0
#     while lo <= hi:
#         mid = (lo + hi) // 2
#         if Mylist[mid] < myItem:
#             lo = mid + 1
#         elif myItem < Mylist[mid]:
#             hi = mid - 1
#         else:
#             return mid
#     return None
#
# shopping =[1,2,3,4,5,6,7,8,9,10]
# item = 3
# print(binarySearch(item,shopping))


#bubblesort

# def bubbleSort(alist):
#     for passnum in range(len(alist)-1,0,-1):
#         for i in range(passnum):
#             if alist[i]>alist[i+1]:
#                 temp = alist[i]
#                 alist[i] = alist[i+1]
#                 alist[i+1] = temp
#     return alist
#
# alist = [54,26,93,17,77,31,44,55,20]
# print(bubbleSort(alist))


# def extendList(val, list=[]):
#     list.append(val)
#     return list
#
#
# list1 = extendList(10)
# # list2 = extendList(123, [])
# list3 = extendList('a')
#
# print("list1 = %s" % list1)
# # print("list2 = %s" % list2)
# # print("list3 = %s" % list3)

# import os
# print (os.path.expanduser('~'))



# output: sun mon
# weekdays = ['sun','mon','tue','wed','thu','fri','sun','mon','mon']
# print(dict(zip(weekdays[0::2],weekdays[1::2])))

# def Prime(n):
#     if n==1:
#         return False
#     for t in range(2,n):
#         if n%t==0:
#             return False
#         else:
#             return True
#
# print(Prime(234))


#print(''.join([str(n) for n in range(10)]))

# import os
# print(os.path.basename(os.getcwd()))

# a = ['Mary', 'had', 'a', 'little', 'lamb']
# for i in range(len(a)):
#     print(i, a[i])


# def Bubblesort(list):
#     for j in range(len(list)-1,0,-1):
#         for i in range(j):
#             if list[i]> list[i+1]:
#                 temp=list[i]
#                 list[i+1] = list[i]
#                 list[i] = temp
#     return list
#
# alist = [54,26,93,17,77,31,44,55,20]
# print(Bubblesort(alist))





# def Bubblesort(list):
#     for j in range(len(list)-1,0,-1):
#         for i in range(j):
#             if list[i] > list[i+1]:
#                 temp=list[i]
#                 list[i+1] = list[i]
#                 list[i] = temp
#     return list
#
# alist = [54,26,93,17,77,31,44,55,20]
# print(Bubblesort(alist))



#Selection sort:
# def selectionSort(list):
#     for slot in range(len(list)-1,0,-1):
#         pmax=0
#         for poz in range(1,slot+1):
#             if list[poz] > list[pmax]:
#                 pmax = poz
#         temp = list[slot]
#         list[slot] = list[pmax]
#         list[pmax] = temp
#     return list
#
#
#
# alist = [54,26,93,17,77,31,44,55,20]
# print(selectionSort(alist))

val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

# def roman():
#     string = str(input('Enter a roman numeral: '))
#     string = string.upper()
#     total = 0
#     while string:
#         if len(string) == 1 or val[string[0]] >= val[string[1]]:
#             total += val[string[0]]
#             string = string[1:]
#         else:
#             total += val[string[1]] - val[string[0]]
#             string = string[2:]
#     print(total)
#
# roman()


# def insertSort(list):
#     for index in range(1, len(list)):
#         cvalue = list[index]
#         poz = index
#
#         while (poz>0)&(list[poz]>cvalue):
#             list[poz]= list[poz-1]
#             poz = poz-1
#
#         list[poz] = cvalue
#     return list
#
# alist = [54,26,93,17,77,31,44,55,20]
# print(insertSort(alist))


# def int2bin(i):
#     if i == 0: return "0"
#     s = ""
#     while i:
#         if i & 1 == 1:
#             s = "1" + s
#         else:
#             s = "0" + s
#         i= i // 2
#     return s
#
# print(int2bin(100))


# def perms(s):
#     if(len(s)==1): return [s]
#     result=[]
#     for i,v in enumerate(s):
#         result += [v+p for p in perms(s[:i]+s[i+1:])]
#     return result
#
#
# print(perms('abc'))

# def fuzzbuzz():
#     for i in range(1,101):
#         if i % 15 == 0:
#             print('fuzzbuzz')
#         elif i % 3 == 0:
#             print('fuzz')
#         elif i % 5 == 0:
#             print('buzz')
#         else:
#             print(i)
#
# fuzzbuzz()

# def fac(n):
#     v=1
#     for i in range(1,n):
#         v*=i
#     print(v)
#
# fac(10)

# def moveTower(height,fromPole, toPole, withPole):
#     if height >= 1:
#         moveTower(height-1,fromPole,withPole,toPole)
#         moveDisk(fromPole,toPole)
#         moveTower(height-1,withPole,toPole,fromPole)
#
# def moveDisk(fp,tp):
#     print("moving disk from",fp,"to",tp)
#
# moveTower(3,"A","B","C")

# def BinaryTree(r):
#     return [r, [], []]
#
# def insertLeft(root,newBranch):
#     t = root.pop(1)
#     if len(t) > 1:
#         root.insert(1,[newBranch,t,[]])
#     else:
#         root.insert(1,[newBranch, [], []])
#     return root

