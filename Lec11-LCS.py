# https://leetcode.com/problems/longest-common-subsequence/
# Author: y0un9n132
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        l1,l2 = len(text1),len(text2)
        table = [[0 for x in range(l1+1)] for y in range(l2+1)]
        for y in range(1,l2+1):
            for x in range(1,l1+1):
                table[y][x] = table[y-1][x-1]+1 if text1[x-1] == text2[y-1] else max(table[y-1][x],table[y][x-1])
        return table[-1][-1]
