class Solution(object):
    def removeDuplicates(self, nums):
        counter = 1
        current_num = nums[0]
        for idx in range (1,len(nums)):
            if nums[idx] == current_num:
                nums[idx] = '_'
            else:
                current_num = nums[idx]
                counter += 1
        nums.sort()  
        print()
        return counter
