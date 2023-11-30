package main

func twoSum(nums []int, target int) []int {
	ans := []int{}
	for i := 0; i < len(nums); i++ {
		for j := i + 1; j < len(nums); j++ {
			if nums[i]+nums[j] == target {
				ans = append(ans, i, j)
				break
			}

		}
	}
	return ans
}
