class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
        
class linkedList:
    def __init__(self):
        self.head=None
        
    def insert_biginning(self,data):
        node=Node(data,self.head)
        self.head=node
        
    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr=self.head
        listr=''
        while itr:
            listr+=str(itr.data)+'-->'
            itr=itr.next
            
        print(listr)
    
    def inserting_end(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next = Node(data,None)
    
    def insert_values(self, data_list):
        self.head=None
        for data in data_list:
            self.inserting_end(data)
        
    def get_length(self):
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next
        return count
    
    def remove_at(self,index):
        if index<0 or index>=self.get_length():
            raise Exception("invalid index")
        if index==0:
            self.head=self.head.next
            return
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                itr.next=itr.next.next
                break
            itr=itr.next
            count+=1
            
    def insert_at(self, index, data):
        if index<0 or index>=self.get_length():
            raise Exception("invalid index")
        
        if index==0:
            self.insert_biginning(data)
            return
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                node=Node(data,itr.next)
                itr.next=node
                break
        #if index==get_length()
        itr=itr.next
        count+=1
if __name__=='__main__':
    li=linkedList()
   #li.insert_biginning(6)
   #li.insert_biginning(92)
   #li.inserting_end(64)
   #li.inserting_end(55)
    li.insert_values(['banana','apple','grapes','pinapple'])
    li.print()
    #li.remove_at(3)
    li.insert_at(2,'orange')
    li.print()
    print("length", li.get_length())
    