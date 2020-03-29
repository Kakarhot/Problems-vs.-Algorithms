## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.children = {}
        self.is_word = False
    
    def insert(self, char):
        ## Add a child node in this Trie
        if char not in self.children:
            self.children[char] = TrieNode()
        
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        parent_node = self.root 
        for char in word:
            parent_node.insert(char)
            parent_node = parent_node.children[char]
            
        parent_node.is_word = True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        
        return node

class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.children = {}
        self.is_word = False
    
    def insert(self, char):
        ## Add a child node in this Trie
        if char not in self.children:
            self.children[char] = TrieNode()
        
    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        words = []
        for char in self.children:
            if self.children[char].is_word:
                words.append(suffix + char)
                
            words.extend(self.children[char].suffixes(suffix + char))
                
        return words
    


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

print ("Pass" if (['un', 'unction', 'actory'] == MyTrie.find('f').suffixes()) else "Fail")
print ("Pass" if (['e', 'gger', 'gonometry', 'pod'] == MyTrie.find('tri').suffixes()) else "Fail")
print ("Pass" if ([] == MyTrie.find('function').suffixes()) else "Fail")
# from ipywidgets import widgets
# from IPython.display import display
# from ipywidgets import interact
# def f(prefix):
#     if prefix != '':
#         prefixNode = MyTrie.find(prefix)
#         if prefixNode:
#             print('\n'.join(prefixNode.suffixes()))
#         else:
#             print(prefix + " not found")
#     else:
#         print('')
# interact(f,prefix='');