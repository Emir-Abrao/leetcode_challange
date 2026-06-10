class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        node = self.trie
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node['$'] = True

    def search(self, word: str) -> bool:
        def search_in_node(word, node):
            for i, char in enumerate(word):
                if char == '.':
                    for key in node:
                        if key != '$' and search_in_node(word[i+1:], node[key]):
                            return True
                    return False
                else:
                    if char not in node:
                        return False
                    node = node[char]
            return '$' in node
        
        return search_in_node(word, self.trie)