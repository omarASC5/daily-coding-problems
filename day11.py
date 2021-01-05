'''
This problem was asked by Twitter.

Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
'''
'''
def findMatches(prefix, q):
    matches = set()
    for word in q:
        if word.startswith(prefix):
            matches.add(word)

    return matches

def buildHashTable(q):
    hash_table = dict()

    for word in q:
        curr_str = ""
        for i in range(len(word) - 1):
            curr_str += word[i]
            matches_set = findMatches(curr_str, q)
            hash_table[curr_str] = matches_set

    return hash_table

def autoComplete(s, q):
    hash_table = buildHashTable(q)
    value = hash_table.get(s)
    if value == None:
        return set()
    return value
'''

class Node:
    def __init__(self, c = ''):
        self.c = c
        self.is_word = False
        self.children = [None] * 26

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node('\0')

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr = self.root
        for i in range(len(word)):
            c = word[i]
            # If the char is not in the Trie add it
            if not curr.children[ord(c) - ord('a')]:
                curr.children[ord(c) - ord('a')] = Node(c)
            
            # go to next node
            curr = curr.children[ord(c) - ord('a')]
            
        # The last character of any word being inserted is marked as word = true
        curr.is_word = True

    def getNode(self, word: str):
        curr = self.root
        for i in range(len(word)):
            c = word[i]
            if not curr.children[ord(c) - ord('a')]:
                return None
            
            # go to next node
            curr = curr.children[ord(c) - ord('a')]
            
        return curr
        
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.getNode(word)
        return node != None and node.is_word

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        return self.getNode(prefix) != None

obj = Trie()
obj.insert('apple')
param_2 = obj.search('apple')
print(param_2)
param_3 = obj.startsWith('b')
print(param_3)

#assert autoComplete("de", ["dog", "deer", "deal"]) == set(["deer", "deal"])
#assert autoComplete("ca", ["cat", "car", "cer"]) == set(["cat", "car"])
#assert autoComplete("ae", ["cat", "car", "cer"]) == set([])
#assert autoComplete("ae", []) == set([])
