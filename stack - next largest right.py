lst=list(map(int, input().split())) #take input of array

'''
#brute force
le=len(lst)
final=[0]*le
final[le-1]=-1
for i in range(0,le):
    print("i",lst[i])
    for j in range(i,le):
        print("j",lst[j])
        if lst[j]>lst[i]:
            print(lst[j],">",lst[i])
            final[i]= lst[j]
            print(final)
            break
        else:
            final[i] = -1
            print(final)

print(final)
'''


sta=[]
final=[]
it=0 #for checking iterations
for i in lst[::-1]:

    it+=1 #increase iteration value
    print(it,"iteration")


    #first check if stack is not empty ie
    #for checking there is next greater number exists
    
    if sta:
        print(i,sta, final)

        #while i is larger than last element of stack, pop the stack
        #to find greater value than i
        #while also checking if stack does not become empty
        
        while(sta and i>=sta[-1]):
            sta.pop()

        #if stack becomes empty after while loop,
        #it indicates no greater on right i array, append -1 to final
        #and for next iteration append i to stack
            
        if not sta:
            sta.append(i)
            final.append(-1)
            print("if not",i,sta, final)


            
        #if i is less than last ele of stack
        #we have found greater no on right, append it to final
        #and for next iteration append i to stack
            
        elif (i<sta[-1]):
            final.append(sta[-1])
            sta.append(i)
            print("if",i,sta, final)

                
    #if stack is empty there is no greater on right, return -1                         
    else:
        print(i,sta, final)
        final.append(-1)
        sta.append(i)
        print("main else",i,sta, final)

print("stack is ", sta)

print(final[::-1])
