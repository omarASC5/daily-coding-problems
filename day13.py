'''
This problem was asked by Amazon.

Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is def getNumOfDistinctLetters(s):
    return len(set(s))
'''

def addToCharMap(char_map, key):
    if key in char_map:
        char_map[key] += 1
    else:
        char_map[key] = 1

def get_longest_sub_with_k_dist(s, k):
    # Edge Case
    if not s:
        return ""
    elif k >= len(s):
        return s
    elif k == 1:
        return s[0]

    # set to store distinct characters in window
    window = set()

    # sliding window boundaries
    low = 0
    high = 0

    # longest substring boundaries
    begin = 0
    end = 0

    char_map = {}

    while high < len(s):

        window.add(s[high])
        addToCharMap(char_map, s[high])

        # if window size > k, remove characters from the left
        while len(window) > k:
            # if the frequency of the leftmost character becomes 0
            # remove it from the window set too
            char_map[s[low]] -= 1

            if char_map[s[low]] == 0:
                window.remove(s[low])

            low += 1

        # update max window size when necessary
        if high - low > end - begin:
            end = high
            begin = low

        high += 1


assert get_longest_sub_with_k_dist("abcba", 2) == "bcb"
assert get_longest_sub_with_k_dist("abccbba", 2) == "bccbb"
assert get_longest_sub_with_k_dist("abcbbbabbcbbadd", 2) == "bbbabb"
assert get_longest_sub_with_k_dist("abcbbbaaaaaaaaaabbcbbadd", 1) == "a"
assert get_longest_sub_with_k_dist("abccbba", 3) == "abccbba"
