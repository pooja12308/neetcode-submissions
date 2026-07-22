class Solution:
    def isHappy(self, n: int) -> bool:
        seen=set()
        while n!=1 and n not in seen:
            seen.add(n)
            n=self.ish(n)
        return n==1
    
    def ish(self,num:int)->int:
        s=0
        while num>0:
            s+=(num%10)**2
            num=num//10
        return s
