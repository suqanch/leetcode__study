# 还是需要“双指针”这个提示，一开始的错误点在把while写成if
#一开始考虑的是“滑动窗口这个概念”，没考虑窗口的尺寸需要变化，所以没想到缩减窗口尺寸
#经过调试发现问题才能做对

import math
def minSubArrayLen(target, nums):
    current = 0
    min_count = math.inf
    count = 0
    index = 0
    for i in range(0, len(nums)):
        current += nums[i]
        while current >= target and index < len(nums):
            count = i - index + 1
            current -= nums[index]
            index+=1
            if count < min_count:
                min_count = count
    if min_count == math.inf:
        return 0

    return min_count



print(minSubArrayLen(7, [2,3,1,2,4,3]))