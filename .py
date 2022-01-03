class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for elem1, a in enumerate(nums, start=0):
            for elem2, b in enumerate(nums[elem1+1:], start=0):
                if a+b==target:
                    return [elem1, elem2+elem1+1]
                    
if __name__ =="main"
  sol= Solution()
  sum= sol.twoSum()
