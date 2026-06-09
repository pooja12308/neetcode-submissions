class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        set1=set()
        for i in nums:
            if i not in set1:
                set1.add(i)
            else:
                return i
        