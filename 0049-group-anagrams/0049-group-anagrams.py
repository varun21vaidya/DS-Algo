class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words=defaultdict(list)
        for char in strs:
            words[tuple(sorted(char))].append(char)
            # print(words)
        return list(words.values())