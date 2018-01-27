# Given a column title as appear in an Excel sheet, return its corresponding column number.

# For example:

#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28 


class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0
        for i in range(len(s)):
        	#ord 将字符转换为ASCLL值
        	sum += (ord(s[len(s)-1-i])-ord('A')+1)*(26**i)

        return sum