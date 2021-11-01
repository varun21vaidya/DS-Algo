pos=0
def search(lst,n):
    i=0
    while i<len(lst):
        if n==lst[i]:
            globals()['pos']=i
            return True
        i+=1
    return False
import time
start_time=time.time()

list1=list(map(int, input().split()))
n=int(input())   #number to be found
if search(list1,n):
    print("found at",pos)
else:
    print('not found')
print(  "%s seconds" %(time.time()-start_time))