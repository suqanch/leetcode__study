# def removeElement(nums, val):
#         count = 0
#         current = 1
#         current_val = 0
#         nums.insert(0,val)
#         while current < len(nums):
#             if nums[current] != val:
#                 nums[current], nums[current_val]= nums[current_val],nums[current]
#                 current_val += 1
#                 count +=1
#             current +=1
            
#         print(nums)
#         return count

#由分割算法改良的快慢指针
def removeElement(nums, val):
        count = 0
        # fast = 0
        slow = 0
        for fast in range(0, len(nums)):
            if nums[fast] != val:
                nums[fast], nums[slow] = nums[slow], nums[fast]
                slow += 1
                count +=1
            
        print(nums)
        return count


# print(removeElement([3,2,2,3], 3))
print(removeElement([0,1,2,2,3,0,4,2], 2))
   