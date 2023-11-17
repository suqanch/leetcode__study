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

print_lst(head)
def swapPairs(head):
    fixhead = ListNode(0, head)
    current = fixhead
    # index = 0
    while current.next:
        if current.next.next == None:
            break
        else:
            part1 = current.next
            part2 = current.next.next
            #1.next = 2.next
            part1.next= part2.next
            #2.next = 1
            part2.next = part1
            current.next = part2
            current = current.next.next
    return fixhead.next

print('\n')
print_lst(swapPairs(head))        


