class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        adjacent = defaultdict(list)
        def bridges(w):
            for i in range(len(w)):
                yield w[:i] + '_' + w[i+1:]
        for w in wordList:
            for b in bridges(w):
                adjacent[b].append(w)
        
        ans = []
        levels = [{beginWord: []}]
        def backtrack(a, i, child):
            if i:
                a[i] = child
                parents = iter(levels[i][child])
                i -= 1
                _p = next(parents)
                for p in parents:
                    backtrack(a[:], i, p)
                backtrack(a, i, _p)
            else:
                a[0] = beginWord
                ans.append(a)
        
        for _ in range(len(wordList)):
            done = False
            parents = defaultdict(list)
            for parent in levels[-1].keys():
                for b in bridges(parent):
                    for child in adjacent[b]:
                        done |= child == endWord
                        parents[child].append(parent)
            levels.append(parents)
            if done:
                l = len(levels)
                backtrack([None]*l, l-1, endWord)
                break
        return ans