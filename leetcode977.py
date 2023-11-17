def sortedSquares(nums):
    l = 0
    r = len(nums) - 1
    #这种思路类似归并排序的合并部分
    res = []
    while r >= l:
        a = nums[l] **2
        b = nums[r] **2
        if a >= b:
            # nums[l], nums[r] = nums[r], a   #平方后交换位置
            res.append(a)
            l += 1
        else:
            # nums[l], nums[r] = a, b
            res.append(b)
            r -=1
    res.reverse()
    return res


#以下是升级版，免去了reverse操作
def sortedSquares(nums):
    l = 0
    r = len(nums) - 1
    pos = len(nums) - 1
    #这种思路类似归并排序的合并部分
    res = [0] * len(nums)
    while r >= l and pos >= 0:
        a = nums[l] **2
        b = nums[r] **2
        if a >= b:
            # nums[l], nums[r] = nums[r], a   #平方后交换位置
            res[pos] = a
            l += 1
        else:
            # nums[l], nums[r] = a, b
            res[pos] = b
            r -=1
        pos -= 1
    return res

print(sortedSquares([-7,-3,2,3,11]))