# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

# You may assume that the array is non-empty and the majority element always exist in the array.

# Credits:
# Special thanks to @ts for adding this problem and creating all test cases.

class Solution:
	#此题 特别好
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0

        for num in nums:
        	if count==0:
        		count += 1
        		majority = num
        	elif num==majority:
        		count += 1
        	else:
        		count -= 1

        return majority 




