class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        s=Counter(sentence)
        if len(s)==26:
            return True
        return False