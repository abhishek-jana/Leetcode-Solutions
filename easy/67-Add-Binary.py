'''
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
'''

class Stack:
    def __init__(self,):
        self.items = []
    def push(self,item):
        self.items.insert(0,item)
    def pop(self):
        return self.items.pop(0)
    def is_empty(self):
        return self.items == []

class Solution:
    def addBinary(self, a, b):
        return InttoBinary(BinarytoInt(a) + BinarytoInt(b))
        
def BinarytoInt(bi_num):
    n = len(bi_num)-1
    int_num = 0
    for i,num in enumerate(bi_num):
        int_num += int(num)*2**(n - i)
    return int_num
def InttoBinary(integer):
    binary = Stack()
    if integer == 0:
        return str(0)
    else:
        while integer > 0:
            reminder = integer % 2
            binary.push(reminder)
            integer //= 2
        string = ""
        while not binary.is_empty():
            string = string + str(binary.pop())
        return string


#print (Solution().addBinary("11","1"))
#print (Solution().addBinary("1110","1011"))


# Better
# Time:  O(n)
# Space: O(1)

class Solution(object):
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        result, carry, val = "", 0, 0
        for i in range(max(len(a), len(b))):
            print (val,carry)
            val = carry
            if i < len(a):
                val += int(a[-(i + 1)])
            if i < len(b):
                val += int(b[-(i + 1)])
            carry, val = divmod(val, 2)
            result += str(val)
            #print (val,carry)
        if carry:
            #print (carry)
            result += str(carry)
        return result[::-1]
    
print (Solution().addBinary("1110","1011"))
