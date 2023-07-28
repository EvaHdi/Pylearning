"""
# -*- coding:utf-8 -*-
@Project : littletest
@File : 005.py
@Author : hongbo.zhang
@Time : 2023/7/28 10:49

递增子序列
给你一个整数数组 nums ，找出并返回所有该数组中不同的递增子序列，递增子序列中 至少有两个元素 。你可以按 任意顺序 返回答案。
数组中可能含有重复元素，如出现两个整数相等，也可以视作递增序列的一种特殊情况。
示例 1：
输入：nums = [4,6,7,7]
输出：[[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]
示例 2：
输入：nums = [4,4,3,2,1]
输出：[[4,4]]
"""
"""
leetcode原题：491递增子序列
可以使用回溯算法来解决这个问题。回溯算法通过遍历数组中的每个元素，以不同的方式构建递增子序列。
具体的步骤如下：
定义一个辅助函数来进行回溯，函数参数包括当前的索引index、当前的递增子序列curSeq和结果集result。
在回溯函数中，首先判断当前的递增子序列的长度。如果curSeq的长度大于等于2，则将其添加到结果集result中。
接下来，在当前索引index的基础上遍历数组中的其他元素，判断是否可以将元素加入到当前的递增子序列中。
如果当前元素大于等于递增子序列的最后一个元素，说明可以将当前元素加入到递增子序列中。然后递归调用回溯函数，继续向后遍历数组。
注意，由于输入数组中可能含有重复元素，为了避免重复的递增子序列，需要在同一层级中跳过相同的元素。
回溯完成后，返回结果集result。
"""


def fsubsequences(nums):
    result = []
    backtrack(0, [], nums, result)
    return result


def backtrack(index, curSeq, nums, result):
    if len(curSeq) >= 2:
        result.append(curSeq[:])  # 添加备份防止后续对curSeq修改导致结果集中也改变

    used = set()  # 记录当前层级中已经使用过的元素，避免重复
    for i in range(index, len(nums)):  # 遍历从索引 index 开始到列表末尾的元素。
        if nums[i] in used:
            continue

        # 判断是否可以将当前元素加入到递增子序列中
        if not curSeq or nums[i] >= curSeq[-1]:
            used.add(nums[i])
            curSeq.append(nums[i])
            backtrack(i + 1, curSeq, nums, result)
            curSeq.pop()


if __name__ == '__main__':

    nums = [4, 6, 7, 7]
    print(fsubsequences(nums))  # [[4, 6], [4, 6, 7], [4, 6, 7, 7], [4, 7], [4, 7, 7], [6, 7], [6, 7, 7], [7, 7]]

    nums = [4, 4, 3, 2, 1]
    print(fsubsequences(nums))  # [[4, 4]]
    # 经过回溯算法的处理，得到了符合要求的所有不同递增子序列。每个子序列都至少包含两个元素，并且结果集中可以按任意顺序返回答案。
