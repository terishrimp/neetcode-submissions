import string
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Loop through all strings in the list and hashmap each
        to store their anagram data

        Loop once more to add each anagram matching a hashmap
        to an array

        return that array

        I want to generate a hashmap for each string. If any strings
        hashmaps match, then they are in the same array.

        O(m*n) allows us to do a loop through each string in the list
        and look at each character
        """

        setlist = {}
        for s in strs:
            alphabet = [0] * 27
            for c in s:
                    alphabet[ord(c)-ord('a')] += 1
            alphabet_tuple = tuple(alphabet)
            if alphabet_tuple not in setlist:
                setlist[alphabet_tuple] = [s]
            else:
                setlist[alphabet_tuple].append(s)

        return list(setlist.values())