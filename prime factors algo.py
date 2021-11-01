'''def print_prime(n,primes):   #method 1
    for num in range(1,n):
        if num > 1:
           for i in range(2, sqrt(num)):
               if (num % i) == 0:
                   break
           else:
               primes.append(num)

def prime_factor(n):
    
    for m in primes:
        if n%m==0:
            while n%m==0:
                n=n/m
                list1.append(m)
    if len(list1)==0:
        list1.append(n)
''' 
def prime_factor(n):    # method 2
    m=2                 # m is diviser which will be dividing n for factors
    while(m<=n):
        if n%m==0:
            n=n/m
            list1.append(m)   
        else:
            m+=1
#primes=[]  
#print_prime(n, primes)  
list1=[]    
n=int(input())
prime_factor(n)
print(list1)
 

        
            
            