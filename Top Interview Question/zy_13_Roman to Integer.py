# Given a roman numeral, convert it to an integer.

# Input is guaranteed to be within the range from 1 to 3999.



class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        dic = {'I' : 1,
        	   'V' : 5,
        	   'X' : 10,
        	   'L' : 50, 
        	   'C' : 100, 
        	   'D' : 500, 
        	   'M' : 1000}

       	sum = dic[s[len(s)-1]]

        for i in range(len(s)-1)[::-1]:
        	if dic[s[i]] < dic[s[i+1]]:
        		sum = sum  - dic[s[i]]
        	else:
        		sum = sum + dic[s[i]]
    

        return sum
