pos=0
def search(lst,n):
    l=0
    u=len(lst)-1
    while l<=u:
        mid=l+u//2
        
        if lst[mid]<n:
            l=mid+1
            
            
        elif lst[mid]==n:
            globals() ['pos']=mid
            return True
            
        elif lst[mid]>n:
            u=mid-1
    return False        

import time
start_time=time.time()
     
list1=list(map(int, input().split()))
list1=sorted(list1)
n=int(input())   #number to be found

if search(list1,n):
    print("found at",pos)
else:
    print('not found')
print("%s seconds" %(time.time()-start_time))               