def searchRange(nums, target):

    def left_bound(target):
        l = 0
        r = len(nums) - 1
        while r >= l:
            m = (l+r)//2
            # nums[l] <=  (target <= nums[m]) <= nums[r]
            #case1 小于target， 一次比较我们有三种操作，小于 等于 大于，为了不断逼近最左边的target
            #等于的时候应该是r = m - 1， 而target大于num[m]也是r = m - 1 
            #由于答案现在是左闭右闭区间内所以case1 我们选择加一
            if nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return l
    
    #问题：我的假设是答案在边界中，可是如果num[len(num) - 1] < targe， 我们将会返回数组长度的l
    # 在 [8, 8]， target = 9的情况下我们会返回 2
    left_bound1 = left_bound(target)
    print(left_bound1)
    #因此当l等于数组长度时，或者结果不等于target时则返回 -1
    if left_bound1 == len(nums) or nums[left_bound1] != target:
        return [-1, -1]
    right_bound1 = left_bound(target+1) - 1

    return [left_bound1, right_bound1]
    


print(searchRange([8, 8], 6))
# print(searchRange([5,7,7,8,8,10], 8))