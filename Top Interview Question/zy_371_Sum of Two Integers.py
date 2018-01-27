#  Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

# Example:
# Given a = 1 and b = 2, return 3.

# Credits:
# Special thanks to @fujiaozhu for adding this problem and creating all test cases.

class Solution:
# 下面两种方案 都是 时间超限 ， java 可以 原因不明很可能是 Python 的内部原因
    # def getSum1(self, a, b):
    #     """
    #     :type a: int
    #     :type b: int
    #     :rtype: int
    #     """
    #     if b==0:
    #     	return a
    #     else:
    #     	return self.getSum(a^b, (a&b)<<1)

    # def getSum(self, a, b):
    # 	#b其实就是 进位 a是值 当b为0既没有进位时 结束
    # 	if a == 0:
    # 		return b
    # 	if b == 0:
    # 		return a

    # 	while b!=0:
    # 		carry = a&b
    # 		a = a ^b
    # 		b = carry << 1

    # 	return a


#Python 的正确写法
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # 32 bits integer max
        MAX = 0x7FFFFFFF
        # 32 bits interger min
        MIN = 0x80000000
        # mask to get last 32 bits
        mask = 0xFFFFFFFF
        while b != 0:
            # ^ get different bits and & gets double 1s, << moves carry
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        # if a is negative, get a's 32 bits complement positive first
        # then get 32-bit positive's Python complement negative
        return a if a <= MAX else ~(a ^ mask)