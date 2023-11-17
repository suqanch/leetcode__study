# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def print_lst(head):
    current = head
    while current.next:
        print(current.val)
        current = current.next
    print(current.val)


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
# head = ListNode(1)
print_lst(head)


#第一种
# def removeNthFromEnd(head, n):
#     slow = 0
#     fast = 0
#     fixhead = ListNode(0, head)
#     current = fixhead
#     slow_node = fixhead
#     while current:
#         if fast - slow == n:
#             if current.next == None:
#                 slow_node.next = slow_node.next.next
#                 break
#             slow_node = slow_node.next
#             slow += 1
#         current = current.next
#         fast += 1
#     return fixhead.next


#更好的方法，右指针先走n步，再左右指针一起走
def removeNthFromEnd(head, n):
    fixhead= ListNode(next=head)

    right = fixhead
    for _ in range(n):
        right = right.next

    left = fixhead
    while right.next:
        right = right.next
        left = left.next
    left.next = left.next.next
    return fixhead.next



print('\n')
print_lst(removeNthFromEnd(head, 1))        


