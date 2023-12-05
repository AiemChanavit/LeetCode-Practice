class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        stop = len(nums) - 1 

        while start <= stop:

            mid = start + (stop - start) //2
            print(mid)

            if target == nums[mid]:
                return mid

            elif target > nums[mid]:
                start = mid + 1

            elif target < nums[mid]:
                stop = mid - 1

        return -1

solution_instance = Solution()
nums = [-1,0,3,5,9,12]
target = 9
result = solution_instance.search(nums, target)
print(result)