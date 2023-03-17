class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}
        
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        
        
        # update new word into trie
        table = self.trie
        for char in word:

            if char not in table:
                table[char] = {}

            table = table[char]
        
        # use '@' as ending symbol
        table['@'] = {}
        
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        
        # search word in trie
        table = self.trie
        
        for char in word:
            table = table.get(char, None)
            
            if table is None:
                return False
        
        # use ending symbol to judge whether current word exist in our trie or not
        return ( '@' in table )
        
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        
        # check the prefix exist in trie or not
        table = self.trie
        
        for char in prefix:
            table = table.get(char, None)
            
            if table is None:
                return False
        
        return True