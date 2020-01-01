'''
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example 1:

Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = -2, b = 3
Output: 1
'''
class Solution:
    def getSum(self,x, y):
        import ctypes
        sum = 0
        carry = ctypes.c_int32(y)
        # Iterate till there is no carry
        while (carry.value != 0):
            
            sum = x ^ carry.value
            # carry now contains common
            # set bits of x and y
            carry = ctypes.c_int32(x & carry.value)

            # Sum of bits of x and y where at
            # least one of the bits is not set

            # Carry is shifted by one so that
            # adding it to x gives the required sum
            carry.value <<= 1
            x = sum

        return sum

res = Solution()
print(res.getSum(-2, 3))

# Above won't work for negetive
