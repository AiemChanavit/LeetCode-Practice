package main

import (
	"fmt"
)

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

func main() {
	fmt.Println(twoSum([]int{2, 7, 11, 15}, 9))
}
