class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words=defaultdict(list)
        print(words)
        for char in strs:
            words[tuple(sorted(char))].append(char)
        return list(words.values())