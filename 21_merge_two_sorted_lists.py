from ListNode import ListNode

def mergeTwoLists(list1, list2):
    header = currentNode = ListNode()
    while (list1 and list2):
        if (list1.val <= list2.val):
            currentNode.next = list1
            list1 = list1.next
        else:
            currentNode.next = list2
            list2 = list2.next
        currentNode = currentNode.next
    if list1:
        currentNode.next = list1
    if list2:
        currentNode.next = list2
    return header.next

def test():
    input1a = ListNode(1, None)
    input1a.next = ListNode(2, None)
    input1a.next.next = ListNode(4, None)
    input1b = ListNode(1, None)
    input1b.next = ListNode(3, None)
    input1b.next.next = ListNode(4, None)
    res1 = mergeTwoLists(input1a, input1b)
    print()
    print("Final: ")
    while not (res1 == None):
        print(res1.val)
        res1 = res1.next

test()
