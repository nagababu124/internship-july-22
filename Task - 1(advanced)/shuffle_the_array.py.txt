class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        a = []
        b = []
        for i in range(len(nums)-n):
            a.append(nums[i])
            
        for j in range(len(nums)-n,len(nums)):
            b.append(nums[j])
            
        return [sub[item] for item in range(len(b)) 
                          for sub in [a, b]]