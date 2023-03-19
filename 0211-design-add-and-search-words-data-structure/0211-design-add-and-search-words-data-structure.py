# class WordDictionary:
#     def __init__(self):
#         self.trie = {}

#     def addWord(self, word: str) -> None:
#         node = self.trie
#         for c in word:
#             node = node.setdefault(c, {})
#         node['$'] = True

#     def search(self, word: str) -> bool:
#         return self.searchNode(self.trie, word)

#     def searchNode(self, node, word: str) -> bool:
#         for i, c in enumerate(word):
#             if c == '.':
#                 return any(self.searchNode(node[w], word[i+1:]) for w in node if w != '$')
#             if c not in node: return False
#             node = node[c]
#         return '$' in node

import re
class WordDictionary:
    def __init__(self):
        self.d = {}
        
    def addWord(self, word: str) -> None:
        self.d[word]  = 1
        self.d[len(word)] = self.d.get(len(word),[]) + [word]
    
    def search(self, word: str) -> bool:
        if '.' not in word:
            if self.d.get(word) != None:
                return True
            else:
                return False
        else:
            if self.d.get(len(word)) != None:
                lis = self.d[len(word)]
                for string in lis:
                    if re.match(word,string):
                        return True
            return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)