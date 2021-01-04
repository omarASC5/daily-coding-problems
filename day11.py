'''
This problem was asked by Twitter.

Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
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
    return hash_table[s]

print(autoComplete('de', ['dog', 'deer', 'deal']))
