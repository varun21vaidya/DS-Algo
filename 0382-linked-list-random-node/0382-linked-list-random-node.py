import random
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.len=0
        self.head=head
        track=self.head
        while track:
            track=track.next
            self.len+=1
        # print("total length",self.len)

    def getRandom(self) -> int:
        x= random.randint(0,self.len-1)
        # print("x",x)
        go=self.head
        while x:
            go=go.next
            x-=1
        return go.val
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()