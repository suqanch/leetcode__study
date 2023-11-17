# def search(nums, target):
#     l = 0
#     r = len(nums) - 1
    
#     while r > l:
#         m = (l + r) // 2
#         # print(m)
#         if nums[m] >= target:   
#             r = m       # [l, m)     左闭右开   
#         else:   #nums[m] < target                   
#             l = m + 1 
    
#     if nums[l] == target:
#         return l 
#     return -1

def search(nums, target):
    l = 0
    r = len(nums)
    
    while r > l:           #[L ,R) [3, 4)  [3, 3)
        m = (l + r) // 2
        # print(m)
        if nums[m] > target:   #右开
            r = m  
        elif nums[m] == target:
            return m     
        else:   #nums[m] < target                   
            l = m + 1 

    return -1
print(search([-1,0,3,5,9,9,9,9,9,12], 9))
print(search([-1,0,3,5,9,12], 9))
print(search([9], 9))
# 