# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        tail = dummy

        while list1 and list2 :
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else: 
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next


solution_instance = Solution()
input_list1 = ListNode(1, ListNode(2, ListNode(4)))
input_list2 = ListNode(1, ListNode(3, ListNode(4)))
result = solution_instance.mergeTwoLists(input_list1, input_list2)
while result:
    print(result.val, end=" ")
    result = result.next
        