class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split()
        if len(pattern) != len(words):
            return False
        pattern_to_word = {}
        word_to_pattern = {}
        for letter, word in zip(pattern, words):
            if (letter in pattern_to_word and pattern_to_word[letter] != word) or   (word in word_to_pattern and word_to_pattern[word] != letter):
                return False
            pattern_to_word[letter] = word
            word_to_pattern[word] = letter
        return True