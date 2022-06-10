def sort(list,count):
    n=len(list)
    
    for i in range (n):
        minpos=i
        
        for j in range(i,n):
            
            if list[j]<list[minpos]:
                count+=1
                minpos=j
        list[i],list[minpos]=list[minpos],list[i]
    return (list)           
list=list(map(int,input().split()))        
#list=[45,89,74,23,78,96,41,75]
count=0


#for i in range(len(list)):
#    print('%d'%list[i],end=' ')
print(sort(list,count))
#len(list)-1
