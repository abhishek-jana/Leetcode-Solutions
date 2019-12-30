'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

'''


class Solution:
    def __init__(self,nums,target):
        self.nums = nums
        self.target = target

    def solve(self):
        index_map = {}
        for i,num in enumerate(self.nums):
            pair = self.target - num
            if pair in index_map:
                return [index_map[pair],i]
            index_map[num] = i
        return None
    def hashsolve(self):
        hashMap = dict()
        for i, item in enumerate(self.nums):
            sub_code = hash(self.target - item)
            if sub_code in hashMap:
                return [hashMap[sub_code], i]
            else:
                hash_code = hash(item)
                if hash_code not in hashMap:
                    hashMap[hash_code] = i
    

sol = Solution(list(range(1,10000000,2)),9000)

print (sol.hashsolve())


'''
Complexity Analysis:

Time complexity : O(n)O(n). We traverse the list containing nn elements only once. Each look up in the table costs only O(1) time.

Space complexity : O(n). The extra space required depends on the number of items stored in the hash table, which stores at most n elements.
'''
