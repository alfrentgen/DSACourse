from common_utils import generate_random_int_array

def bubble_sort(arr):
    moved = True
    while moved:
        moved = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                a = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = a
                moved = True
    return arr

for l in range(100):
    arr1 = generate_random_int_array(l)
    arr2 = arr1.copy()
    arr1 = bubble_sort(arr1)
    arr2.sort()
    assert(arr1 == arr2)

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
    
def mergeTwoLists1(list1, list2):
    """
    :type list1: Optional[ListNode]
    :type list2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """

    if not list1 or not list2:
        return list1 or list2
    
    cur, ins_head = (list1, list2) if list1.val < list2.val else (list2, list1)
    res = cur
    while cur.next is not None and ins_head:
        if ins_head.val > cur.next.val:
                cur = cur.next
                continue

        ins_tail = ins_head

        while ins_tail.next and ins_tail.next.val <= cur.next.val:
            ins_tail = ins_tail.next
        
        right = cur.next
        cur.next = ins_head
        ins_head = ins_tail.next
        ins_tail.next = right
        cur = right

    if ins_head:
        cur.next = ins_head
    return res

    def mergeTwoLists2(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        if not list1 or not list2:
            return list1 or list2
        
        target, inserter = (list1, list2) if list1.val < list2.val else (list2, list1)
        res = target
        while target.next and inserter:
            while target.next and target.next.val <= inserter.val:
                target = target.next
            
            new_inserter = target.next
            target.next = inserter
            inserter = new_inserter
        
        if inserter:
            while target.next:
                target = target.next
            target.next = inserter

        return res
