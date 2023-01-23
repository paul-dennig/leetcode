class TrieNode:

    def __init__(self, val, is_word):
        self.is_word = is_word
        self.value = val
        self.children = {}

class Trie:

    def __init__(self):
        self.root = TrieNode("*", False)

    def insert(self, word: str) -> None:
        current_node = self.root
        for character in word:
            if character not in current_node.children:
                current_node.children[character] = TrieNode(character, False)
            current_node = current_node.children[character]
        current_node.is_word = True

    def search(self, word: str) -> bool:
        current_node = self.root
        for character in word:
            if character not in current_node.children:
                return False
            current_node = current_node.children[character]
        return current_node.is_word

    def startsWith(self, prefix: str) -> bool:
        current_node = self.root
        for character in prefix:
            if character not in current_node.children:
                return False
            current_node = current_node.children[character]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
