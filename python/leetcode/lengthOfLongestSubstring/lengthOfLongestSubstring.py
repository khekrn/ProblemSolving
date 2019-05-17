'''
Given a string, find the length of the longest substring without repeating characters.

Example 1:
----------
Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 

Example 2:
----------
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
----------
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''
def lengthOfLongestSubstring(s):
        """
        :type s: str
        :rtype: int        
        """
        left_word = 0
        max_size = 0
        last_seen = {}
        for i, char in enumerate(s):
            if char in last_seen:
                left_word = max(left_word, last_seen[char]+1)
            last_seen[char] = i
            max_size = max(max_size, i-left_word+1)
        return max_size

print(lengthOfLongestSubstring("au"))
print(lengthOfLongestSubstring(" "))
print(lengthOfLongestSubstring("bb"))
print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("pwwkazw"))
print(lengthOfLongestSubstring("dvdf"))
print(lengthOfLongestSubstring("dvdfabcdefghijklmmooppqrstuvwxyz"))