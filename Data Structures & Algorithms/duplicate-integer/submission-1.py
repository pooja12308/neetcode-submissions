class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        test=set()
        for x in nums:
            if x in test:
                return True
            test.add(x)
        

        return False
        
        