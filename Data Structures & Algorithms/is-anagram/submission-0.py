class Solution:

    # def isAnagram(self, s: str, t: str) -> bool:     
    #     if sorted(s) == sorted(t):
    #         return True
    #     return False
        
    def isAnagram(self, s: str, t: str) -> bool: 
        dict1 = {}
        dict2 = {}

        for letter in s:
            dict1[letter] = dict1.get(letter, 0) + 1

        for letter in t:
            dict2[letter] = dict2.get(letter, 0) + 1

        return dict1 == dict2


# Valid Anagram: count letters with a dict, O(n) time, O(1) space (26 letters). Sorting alternative: O(n log n) time, O(n) space.