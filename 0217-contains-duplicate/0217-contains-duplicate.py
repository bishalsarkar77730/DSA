class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False
        # length = len(nums)
        # if length <= 0:
        #     return False
        # else:
        #     for num in range(length):
        #         for i in range(num + 1, length):
        #             if nums[num] == nums[i]:
        #                 return True
        #     return False
