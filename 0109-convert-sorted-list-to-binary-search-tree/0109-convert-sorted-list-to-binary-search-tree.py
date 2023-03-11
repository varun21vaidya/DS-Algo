# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
# convert linked list to array
    def sortedListToBST1(self, head):
        ls = []
        while head:
            ls.append(head.val)
            head = head.next
        return self.helper(ls, 0, len(ls)-1)

    def helper(self, ls, start, end):
        if start > end:
            return None
        if start == end:
            return TreeNode(ls[start])
        mid = (start+end) >> 1
        root = TreeNode(ls[mid])
        root.left = self.helper(ls, start, mid-1)
        root.right = self.helper(ls, mid+1, end)
        return root

    # top-down approach, O(n*logn)
    def sortedListToBST2(self, head):
        if not head:
            return 
        if not head.next:
            return TreeNode(head.val)
        dummy = ListNode(0)
        dummy.next = head
        slow, fast = dummy, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        root = TreeNode(slow.next.val)
        root.right = self.sortedListToBST(slow.next.next)
        slow.next = None
        root.left = self.sortedListToBST(head)
        return root

    # bottom-up approach, O(n)
    def sortedListToBST3(self, head):
        l, p = 0, head
        while p:
            l += 1
            p = p.next
        return self.convert([head], 0, l-1)

    def convert(self, head, start, end):
        if start > end:
            return None
        mid = (start + end) >> 1
        l = self.convert(head, start, mid-1)
        root = TreeNode(head[0].val)
        root.left = l
        head[0] = head[0].next 
        root.right = self.convert(head, mid+1, end)
        return root

    # bottom-up approach, O(n)    
    def sortedListToBST(self, head):
        l, p = 0, head
        while p:
            l += 1
            p = p.next
        self.node = head
        return self.convert(0, l-1)

    def convert(self, start, end):
        if start > end:
            return None
        mid = (start + end) >> 1
        l = self.convert(start, mid-1)
        root = TreeNode(self.node.val)
        root.left = l
        self.node = self.node.next 
        root.right = self.convert(mid+1, end)
        return root