class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert_node(self, word) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search_word(self, word) -> bool:
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end

    def search_pattern(self, pattern) -> bool:
        node = self.root
        for ch in pattern:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True

    def search_prefix(self, prefix) -> list:
        node = self.root
        # check for all chars in prefix first
        for ch in prefix:
            if ch not in node.children:
                return []
            node = node.children[ch]
        result  = []
        # do dfs to find all the possible paths and add to result arr
        def dfs(node : TrieNode, path : str) -> list:
            if node.is_end:
                result.append(path)
            for ch, next_node in node.children.items():
                dfs(next_node, path + ch)

        dfs(node, prefix)
        return result

if __name__ == "__main__":
    # init trie and insert words
    trie_test = Trie()
    words = ['apple', 'app', 'application', 'banana', 'banter', 'car', 'carting']
    for word in words:
        trie_test.insert_node(word)

    # test diff methods
    print(trie_test.search_word("apple"))
    print(trie_test.search_word("apsd"))
    print(trie_test.search_pattern("ap"))
    print(trie_test.search_pattern("cx"))
    print(trie_test.search_prefix("app"))
    print(trie_test.search_prefix('ca'))
    print(trie_test.search_prefix("cb"))