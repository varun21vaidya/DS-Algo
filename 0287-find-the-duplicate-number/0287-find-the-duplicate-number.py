class Solution:
    def findDuplicate(self, arr: List[int]) -> int:
        while True:
            if arr[arr[0]]!=arr[0]:
                arr[arr[0]],arr[0]=arr[0],arr[arr[0]]
            else:
                return arr[0]