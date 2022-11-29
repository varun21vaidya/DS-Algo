"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        # Method 1 : hashmap TC: O(n), SC:O(n)
        
        # create a linkedlist similar to input given
        # but why, because we cant get input list directly
        # so store its nodes in hashmap
        
        
        # clone the list without random
        # use a hashmap which will link og list with clone list
        # now traverse both list at same time and get random pointer.
        # first get its random node from og list then with key as value to it get its clone value from hashmap
        # and assign clone.random to that value
        # more clear explanation: https://leetcode.com/problems/copy-list-with-random-pointer/solutions/258935/detailed-explanation-with-pictures-c-javascript/

        mapp={}
        op=res=Node(0)
        temp=head

        # first pass to create a clone and allocate clone nodes as values
        # to its og list nodes as keys in a hashmap
        while temp:
            res.next=Node(temp.val)
            mapp[temp]=res.next
            temp=temp.next
            res=res.next

        temp=head   # og list
        res=op.next # clone list

        # 2nd pass to allocate the random pointers to clone list
        while temp:
            res.random= mapp[temp.random] if temp.random else None
            temp,res=temp.next, res.next
        
        return op.next


        # Method 2 : 3 Pass solution TC- O(n) SC: O(1)
        
        # now instead of using hashmap to store the clones
        # we can just store them in the same linked list 
        # ie each clone node ahead of its og node
        # so it will take O(1) space complexity 
        # (auxillary ie neglecting extra space in linked list)

        # so steps are as below
        # first traverse and store the clone nodes ahead of og nodes
        # just nodes dont consider random here
        # then traverse and assign random to next of random nodes of og nodes 
        # so it will be assigned to clone nodes only
        # now saperate the lists by creating a clone list
        # and removing the clone nodes from it

         
        # traverse and assign clone to next of it
        traverse=head
        while traverse:
            temp=traverse.next
            traverse.next=Node(traverse.val)
            traverse.next.next=temp
            traverse=traverse.next.next
            
        # assign clone node random to next of og random ie clone of og random

        traverse=head
        while traverse:
            traverse.next.random=traverse.random.next if traverse.random else None
            traverse=traverse.next.next
        
        # create a res node and assign every clone node to it
        # then from the og list remove clone nodes

        op=res=Node(0)
        traverse=head
        while traverse:
            res.next=traverse.next
            
            traverse.next=traverse.next.next
            
            traverse=traverse.next
            res=res.next
        
        return op.next
