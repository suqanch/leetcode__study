class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
head = ListNode(1, ListNode(2, ListNode(3)))
def print_lst(head):
    current = head
    while current.next:
        print(current.val)
        current = current.next
    print(current.val)
print_lst(head)

# 思路1： 递归
class Solution:
    def reverseList(self, head):
        if not head:
            return
        part1 = head
        if part1.next == None:
            return part1
        if part1.next.next != None:
            part2 = part1.next
            part2 = self.reverseList(part2)
        else:
            part2 = part1.next
        # part2 = reverseList(part2)
        # part1.next, part2.next = None, part1
        part1.next = None
        current_head = part2
        while current_head.next:
            current_head = current_head.next
        current_head.next = part1

        # head = part2
        return part2


#思路2 遍历
class Solution:
    def reverseList(self, head):
        part1 = None
        current = head
        part2 = None
        while current:
            part2 = current.next
            current.next = part1
            part1 = current
            current = part2

        return part1





a = Solution()
b = a.reverseList(head)
print('...........')
print_lst(b)