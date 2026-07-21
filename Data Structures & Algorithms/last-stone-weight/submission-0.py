class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones)>1:
            stones.sort()
            currd=stones.pop()-stones.pop()
            if currd:
                stones.append(currd)
        return stones[0] if stones else 0

        
        