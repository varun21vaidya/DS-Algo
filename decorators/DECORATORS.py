#DECORATORS

def my_decorator(func):     #defining the decorator
    def wrapper():          #wrapping func
        print("upward func actions")
        func()              #calling the func to be wrapped
        print("downward to func actions")

    return wrapper

def wrapped_func():
    print("YAY!!")

wrapped_func=my_decorator(wrapped_func)

print(wrapped_func())
