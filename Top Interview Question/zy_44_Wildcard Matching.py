class Solution:
	# 太难了 需要 背诵！！！

	# Implement wildcard pattern matching with support for '?' and '*'.
	# '?' Matches any single character.
	# '*' Matches any sequence of characters (including the empty sequence).
	# The matching should cover the entire input string (not partial).
	# The function prototype should be:
	# bool isMatch(const char *s, const char *p)
	# Some examples:
	# isMatch("aa","a") → false
	# isMatch("aa","aa") → true
	# isMatch("aaa","aa") → false
	# isMatch("aa", "*") → true
	# isMatch("aa", "a*") → true
	# isMatch("ab", "?*") → true
	# isMatch("aab", "c*a*b") → false

	def isMatch(self, s, p):
		sp = 0
		pp = 0
		match = 0
		star = -1


		while sp < len(s):
			if(pp < len(p) and (p[pp]==s[sp] or p[pp]=='?')):
				pp +=1
				sp +=1
			elif pp<len(p) and p[pp] == '*':
				star = pp
				pp +=1
				match = sp
			elif star != -1:
				pp = star + 1
				match+=1
				sp =match
			else:
				return False


		while pp<len(p) and p[pp] == '*':
			pp+=1
		

		return pp == len(p)





	# 自己的 写法 不对  
    # def isMatch1(self, s, p):
    #     """
    #     :type s: str
    #     :type p: str
    #     :rtype: bool
    #     """
    #     i = 0
    #     j = 0
    #     while i < len(s) and j < len(p):
    #     	if p[j]=='?':
    #     		i+=1
    #     		j+=1

    #     	elif p[j]=='*':
    #     		k = 0


    #     		while j<len(p) and (p[j]=='*' or p[j]== '?')
    #     			if p[j]=='?':
    #     				k+=1
    #     			j+=1

    #     		if j<len(p):
    #     			while i<len(s)-k and s[i]!=p[j]:
    #     				i+=1
    #     			if i!=len(s)-k:
    #     				i +=k+1
    #     				j +=1
        				

    #     		else:
    #     			if i+k < len(s):
    #     				i = len(s) 
        		      		

    #     	else:
    #     		if s[i]!=p[j]:
    #     			break
    #     		else:
    #     			i+=1
    #     			j+=1


    #    	if j==len(p) and i==len(s):
    #    		return True
    #    	else:
    #    		return False


    
        	


