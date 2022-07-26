class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

	# here taken an empty array with initial value num[0]
        ans = [nums[0]]
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
            ans.append(nums[i])
        return ans