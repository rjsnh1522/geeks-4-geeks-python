# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, A, B):
        tortoise = A
        hare = A
        prev = None
        head = A
        for i in range((B-1)):
            hare = hare.next
        while hare.next is not None:
            prev = tortoise
            tortoise = tortoise.next
            hare = hare.next
        nextr = tortoise.next
        prev.next = nextr
        return head
# 1 2 3 4 5 6 7 8 9 10---> 5
#
# 1 5
# 2 6
# 3 7
# 4 8
# 5 9
# 6 10

a_14 = ListNode(14)
a_42 = ListNode(42)
a_98 = ListNode(98)
a_26 = ListNode(26)
a_36 = ListNode(36)
a_28 = ListNode(28)
a_57 = ListNode(57)
a_93 = ListNode(93)
a_14.next = a_42
a_42.next = a_98
a_98.next = a_26
a_26.next = a_36
a_36.next = a_28
a_28.next = a_57
a_57.next = a_93

sol = Solution()
header = sol.removeNthFromEnd(a_14, 2)
while header is not None:
    print(header.val)
    header = header.next
