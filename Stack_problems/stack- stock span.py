#Stock Span Problem
#arr = 100 80 60 70 60 75 85

#find consecutive less numbers for each element, else return 1
#like for left of 70 there sre another 3 less consecutive terms
#hence line of 4 decreasing terms

#100 80 60 70 60 75 85  input
# |  |   |  |  |  |  |
# 1  1   1  2  1  1  6  output


#Soln:
#we can solve this by stack, see we are just determining
#the count till next greatest element left and printing diff of index

#100    80   60  70  60  75 85  input
# |     |     |  |   |    |  |
# -1    100  80  80  70  80  100  next gretest ele on left
# |     |     |  |   |    |  |
# 1   1-0   2-1 3-2 4-3  5-1 6-0 index (for 1st ele default 1)
# |     |     |  |   |    |  |
# 1     1     1  2   1    4  6  output


'''
lst=list(map(int, input().split()))
sta,final=[],[]
it=0
for i in (lst): #only change from right is normal traverse
    it+=1
    print("iteration is",it)
    if sta:
        print(sta, final)
        while(sta and i>=sta[-1][1]):
            sta.pop()
            print("popped")
        
        if not sta:
            final.append(it)
        
        elif (i<sta[-1][1]):
            print("i, index, sta[-1], its index", i, (it-1) , sta[-1], sta[-1][0])
            final.append(it-sta[-1][0])

    else:
        print(sta, final)
        final.append(it)

    sta.append([it,i])


print(final)
'''
lst=list(map(int, input().split()))
n=len(lst)
sta,final=[],[]
it=0
sta.append(0)
final.append(1)
for i in range(1,n): #only change from right is normal traverse
    print("iteration is",i+1)
    if sta:
        print(sta, final)
        while(sta and lst[i]>=lst[sta[-1]]):
            print("popped")
            sta.pop()
        
        if not sta:
            print("if not")
            final.append(i+1)
        
        else:
            print("i, index, sta[-1], index of stack ele", lst[i], i , lst[sta[-1]], sta[-1])
            final.append(i-sta[-1])

    else:
        print(sta, final)
        final.append(i+1)

    sta.append(i)


print(final)

