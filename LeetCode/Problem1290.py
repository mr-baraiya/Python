class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        res = 0
        while head:
            res = (res << 1) | head.val
            head = head.next
        return res
