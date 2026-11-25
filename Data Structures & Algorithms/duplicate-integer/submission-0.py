class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        store = set()
        for i in nums:
            if i in store:
                return True
            else:
                store.add(i)
        return False
   

    def hasDuplicate2(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(0, len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False


# Contains Duplicate: hash set, O(n) time, O(n) space. Sorting alternative: O(n log n) time, small space.