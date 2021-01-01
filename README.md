1. Two Sum

# 题目描述

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

# 示例

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

# 题目大意

给定一个由整数组成的数组和一个整数的目标值，在数组中找到两个数，它们的和等于给定的目标值，最后返回两个数在数组中的下标。

# 解题思路

最优解法：时间复杂度为 O(n)

顺序遍历数组的每一项，同时获取到对应项的下标，在字典中找到当前项的另一个数值，如果找到了就直接返回两个数的下标；如果找不到，就把这一项的值作为 key，索引为 value 存入字典中，再次遍历下一项。

# 代码

```python
def twoSum(self, nums: List[int], target: int) -> List[int]:
    obj = {}
    for idx, value in enumerate(nums):
        another = target - value
        if another in obj:
            return [obj[another], idx]
        obj[value] = idx
```
