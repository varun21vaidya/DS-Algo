def mergesort(lst):
    if len(lst)<=1:
        return lst
    middle=len(lst)//2
    left=mergesort(lst[:middle])
    right=mergesort(lst[middle:])
    return merge(left,right)


def merge(left, right):
    i,j=0,0
    res=[]
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            res.append(left[i])
            i+=1
        else:
            res.append(right[j])
            j+=1

    res=res+right[j:]
    res=res+left[i:]
    
    return res



#lst=[2,6,-8,36,14,25,98,74,23]
#for remaining numbers in either list after any list is over

from random import randint
lst=[]
for _ in range(10):
    lst.append(randint(0,100))
    
print(lst)  
print(mergesort(lst))