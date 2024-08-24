
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    root = None
    node = None
    carry = 0
    while True:
        l1Value = l1.val if l1 is not None else 0
        l2Value = l2.val if l2 is not None else 0
        indexValue = l1Value + l2Value + carry

        if indexValue >= 10:
            carry = 1
            indexValue = indexValue % 10
        else:
            carry = 0

        if node == None:
            node = ListNode(indexValue)
            root = node
        else:
            node = node.next = ListNode(indexValue)
        
        if l1 is not None: l1 = l1.next
        if l2 is not None: l2 = l2.next

        if l1 is None and l2 is None and carry == 0:
            break

    return root

l3 = ListNode(3)
l2 = ListNode(4, l3)
l1 = ListNode(2, l2)

l6 = ListNode(4)
l5 = ListNode(6, l6)
l4 = ListNode(5, l5)

l9 = addTwoNumbers(l1, l4)
print("l9", l9)




