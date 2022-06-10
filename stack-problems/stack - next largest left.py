lst=list(map(int,input().split()))

'''
#brute Force
le=len(lst)
final=[0]*le
final[0]=-1
for i in range(le-1,-1,-1):
    print("i",lst[i])
    for j in range(i-1,-1,-1):
        print("j",lst[j])
        if lst[j]>lst[i]:
            print(lst[j],">",lst[i])
            final[i]= lst[j]
            print(final)
            break
        else:
            final[i] = -1
            print(final)

print(final[::-1])
'''

sta,final=[],[]
it=0
for i in lst: #only change from right is normal traverse
    it+=1
    print("iteration is",it)
    if sta:
        print(sta, final)
        while(sta and i>=sta[-1]):
            sta.pop()
        
        print(sta, final)
        
        if not sta:
            final.append(-1)
        
        elif (i<sta[-1]):
            final.append(sta[-1])

        print(sta, final)
    else:
        print(sta, final)
        final.append(-1)

    sta.append(i)


print(final)#only change from right is print final as it is

        
