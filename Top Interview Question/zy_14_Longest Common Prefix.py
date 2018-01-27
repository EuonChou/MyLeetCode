# Write a function to find the longest common prefix string amongst an array of strings.


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        ans = ""
        flag = True
        if len(strs) == 0:
        	return ""
        for i in range(len(strs[0])):
        	ch = strs[0][i]
        	
        	for str in strs:
        		if i >= len(str) or str[i] != ch:
        			flag = False
        			break;
        	if flag == False:
        		break
        	else:
        		ans += ch
        
        return ans

# 大神的答案
# class Solution:
#     def longestCommonPrefix(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: str
#         """
#         if not strs:
#             return ''
#         for i, chars in enumerate(zip(*strs)):			
#             if len(set(chars)) > 1:
#                 return strs[0][:i]
#         return min(strs)

#zip的 使用方法
# >>>a = [1,2,3]
# >>> b = [4,5,6]
# >>> c = [4,5,6,7,8]
# >>> zipped = zip(a,b)     # 打包为元组的列表
# [(1, 4), (2, 5), (3, 6)]
# >>> zip(a,c)              # 元素个数与最短的列表一致
# [(1, 4), (2, 5), (3, 6)]
# >>> zip(*zipped)          # 与 zip 相反，可理解为解压，返回二维矩阵式
# [(1, 2, 3), (4, 5, 6)]

#enumerate的 使用方法
# >>>seasons = ['Spring', 'Summer', 'Fall', 'Winter']
# >>> list(enumerate(seasons))
# [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
# >>> list(enumerate(seasons, start=1))       # 小标从 1 开始
# [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]