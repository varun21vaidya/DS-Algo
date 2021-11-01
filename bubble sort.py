def sort(list,count):
    
    n=len(list)
    
    for i in range (n):
        
        for j in range(0,n):
            
            if list[j]>list[j+1]:
                count+=1
                
                list[j],list[j+1]=list[j+1],list[j]
    
    return (count)           

count=0
list=list(map(int,input().split()))        
#list=[45,89,74,23,78,96,41,75]


print(sort(list,count))


#for space saperated output
for i in range(len(list)):
    print(list[i],end=' ')

