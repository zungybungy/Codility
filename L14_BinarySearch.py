def binarySearch(myItem,Mylist):
    lo = 0
    hi = len(Mylist)-1
    postion = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        if Mylist[mid] < myItem:
            lo = mid + 1
        elif myItem < Mylist[mid]:
            hi = mid - 1
        else:
            return mid
    return None


def linearSearch(myItem,Mylist):
    found =False
    postion = 0
    while ((postion<len(Mylist)) & (found ==False)) :
        if (Mylist[postion] == myItem):
            found = True;
        postion = postion+1
    print(postion)
    return postion



shopping =[1,2,3,4,5,6,7,8,9,10]
item = 3
print(binarySearch(item,shopping))

# shopping =['apple','banana','orange','mango']
# item = 'mango'
#
# linearSearch(item,shopping)