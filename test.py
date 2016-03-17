def test(nums):
    nums.sort()
    res=[]
    def bt(self,n):
        if not n:
            return []
        self.res+=[n[0]+s for s in bt(n[1:])]
    bt(nums)
    return res

nums=[1,1,2]
print test(nums)