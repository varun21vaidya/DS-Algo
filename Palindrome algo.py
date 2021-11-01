n=input()
def palindrome(n):
    n.replace(' ','') #for sentenses
    n=n.lower()
    if list(reversed(n))==list(n):
        print('True')
    else:
        print('False')
palindrome(n)
