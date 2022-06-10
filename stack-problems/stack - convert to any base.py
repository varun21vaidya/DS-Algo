class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

#decnp- decimal number
def ConvertToBase(decno, base):
    digits="0123456789ABCDEF"
    remainstack=Stack()
    
    while decno>0:
        rem=decno%base
        remainstack.push(rem)
        decno=decno//base

    Str=""
    while not remainstack.isEmpty():
        Str=Str+digits[remainstack.pop()]

    return Str

print("binary: ", ConvertToBase(26,2))
print("octal: ", ConvertToBase(26,8))
print("Hex: ", ConvertToBase(26,16))
