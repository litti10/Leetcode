# It is more effecient to use dictionary in this kind of problem
class Solution(object):
    def twoSum1(self, nums, target):
        for NUM1 in range (len(nums)):
            for NUM2 in range (NUM1+1,len(nums)):
                if nums[NUM1]+nums[NUM2] == target:
                    return [NUM1,NUM2]

    def twoSum2(self, nums, target):
        ANS_DIC = {}
        COUNTER = 0
        for n in nums:
            ANS_DIC[target-n] = COUNTER
            COUNTER += 1
        for IDX in range(len(nums)):
            if nums[IDX] in ANS_DIC and IDX != ANS_DIC[nums[IDX]]:
                return [IDX,ANS_DIC[nums[IDX]]]
                
    # Fastest Answer
        # for i, x in enumerate(nums):
        #     find = target - x
        #     if find in d:
        #         return [d[find], i]
            
        #     d[x] = i