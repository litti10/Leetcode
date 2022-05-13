class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        right = left+1
        max_l = 0
        while left < len(s):
            alphabet_list = [0 for x in range(256)]
            alphabet_list[ord(s[left])] = 1
            l = 1
            while right < len(s) and alphabet_list[ord(s[right])] !=1:
                alphabet_list[ord(s[right])] = 1
                l += 1
                right +=1
            left += 1
            right = left+1
            max_l = max(max_l, l)
        return max_l
