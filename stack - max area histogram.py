'''
#MAX AREA HISTOGRAM
#cal Max area covered by histogram heights
#heights given in array, width=1 for each
#APPROACH: we take one ele ie height and
#look if it can be expanded ie
#it have => ele besides it on left and right
#ie continues ele width

#SO indirectly we are finding upto next Smallest ele on both sides
#so find their index, calculate total width
#total width=NSR-NSL-1 and multiply with height=arr[i] to get area
#and from that list of areas find max
'''

lst=list(map(int,input().split()))

sta,finalL=[],[]
it=0
for i in lst:               #code for next smallest left
    it+=1
    if sta:
        while(sta and i<=sta[-1][1]):
            sta.pop()
        
        if not sta:
            finalL.append(-1)
        
        elif (i>sta[-1][1]):
            finalL.append(sta[-1][0]-1)

    else:
        finalL.append(-1)

    sta.append([it,i])
    
print("finalL",finalL)
 
#it=7 ie in general len(lst) as for reverse
it,sta,finalR=len(lst),[],[]   #code of Next smallest right
for i in lst[::-1]:     #change is it=7, it-=1 for counting index
    it-=1               #as it process in reverse    
    if sta:
        while(sta and i<=sta[-1][1]):
            sta.pop()
            
        if not sta:
            #if array empty 1 index ahead of last index ie here 7
            finalR.append(len(lst))
        
        elif (i>sta[-1][1]):
            finalR.append(sta[-1][0])

    else:
        finalR.append(len(lst))

    sta.append([it,i])
    
finalR=finalR[::-1]   
print("finalR",finalR)

final=[]        #calculate width=NSR-NSL-1 and area=width*height[k] ie arr[k]
                    
for k in range(len(lst)):
    final.append( (finalR[k] - finalL[k] -1) *lst[k])

print("area",final)
print (max(final))
