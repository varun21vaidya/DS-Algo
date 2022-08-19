class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        
        # create two counter dictionaries one for tracking occurances of nums
        # and other for next number in the already filled subsequence
        # if number is not in freq or has lost all its occurance move ahed
        # if number is present and its also in nextMap reduce its occurance from it
        # and put next number in nextMap 
        # if not both conditions then it will check if it can create new subsequence
        # for that check if its next and further next values ie i+1, i+2 values are present
        # if yes then reduce their occurance also and put their next number in nextMap
        # if nothing works its False
        # but in either true cases, current number will lose its frequency
        # finally return True
        
        freqMap=Counter(nums)
        nextMap=Counter()
        for i in nums:
            if not freqMap[i]:
	            continue
            if nextMap[i]:
                nextMap[i]-=1
                nextMap[i+1]+=1
            elif (freqMap[i+1] and freqMap[i+2]):
                freqMap[i+1]-=1
                freqMap[i+2]-=1
                
                nextMap[i+3]+=1
            else:
                return False
            freqMap[i]-=1
        return True
                