class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        dict = {}

        # fill dictionary for all letters with empty list
        for c in 'abcdefghijklmnopqrstuvwxyz':  
            dict[c] = []
        
        # fill lists occurance-indices in super string
        for i, c in enumerate(s):
            if c in dict.keys():
                dict[c].append(i)

        def firstOccuranceGreaterThanKey(arr, key):
            for j in arr:
                if j > key:
                    return j
            return None

        # pick words one by one, if match, increment the result count
        resultCount = 0
        for w in words:
            # try if the word is sub-sequence by comparing characters one by one moving right side
            last = -1
            for i, c in enumerate(w):
                ind = firstOccuranceGreaterThanKey(dict[c], last)
                # if character found at index
                if ind is not None:
                    # if we reached at end of word, increment count and break
                    if i == len(w)-1:
                        resultCount += 1
                    else:
                        last = ind 
                else:
                    break
        return resultCount