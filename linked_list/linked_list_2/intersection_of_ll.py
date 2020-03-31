# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, A, B):
        hasher = {}
        not_found = True
        found_at = None
        if A is None or B is None:
            return None
        while A is not None and B is not None and not_found:
            if B in hasher:
                not_found = False
                found_at = B
            else:
                hasher[B] = True

            if A in hasher:
                not_found = False
                found_at = A
            else:
                hasher[A] = True

            if A is not None:
                A = A.next
            if B is not None:
                B = B.next

        if A is not None:
            while A is not None:
                if A in hasher:
                    not_found = False
                    found_at = A
                else:
                    hasher[A] = True
                A = A.next

        if B is not None:
            while B is not None:
                if B in hasher:
                    not_found = False
                    found_at = B
                else:
                    hasher[B] = True
                B = B.next

        return found_at


# a_5 = ListNode(5)
# a_8 = ListNode(8)
# a_26 = ListNode(20)
#
# b_4 = ListNode(4)
# b_11 = ListNode(11)
# b_15 = ListNode(15)
#
# c_23 = ListNode(23)
# c_25 = ListNode(25)
# c_27 = ListNode(27)
#
# a_5.next = a_8
# a_8.next = a_26
# a_26.next = c_23
#
# b_4.next = b_11
# b_11.next = b_15
# b_15.next = c_23
#
# c_23.next = c_25
# c_25.next = c_27
# c_27.next = None


a_1 = ListNode(1)
a_2 = ListNode(2)
b_3 = ListNode(3)
c_4 = ListNode(4)
a_1.next = a_2
a_2.next = c_4
b_3.next = c_4
c_4.next = None


sol = Solution()

inter = sol.getIntersectionNode(a_1, b_3)

print(inter.val)
