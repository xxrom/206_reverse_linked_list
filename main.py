# Definition for singly-linked list.
class Node:

  def __init__(self, value=None, next=None):
    self.val = value
    self.next = next


class Solution:

  # Create LinkedList from array with values
  def convertListToLinkedList(self, values: [int]) -> Node:
    head = None
    prev = None
    for value in values:
      node = Node(value)

      if prev is None:
        prev = node
        head = node
      else:
        prev.next = node
        prev = node

    return head

  # Get all values from Linked List and return array with them
  def printList(self, head: Node, allValues: [int] = []) -> [int]:

    if head != None and head.val != None:
      allValues.append(head.val)
      if head.next != None:
        return self.printList(head.next, allValues)

    return allValues

  # Get reversed Linked List
  def reverseList(self, head: Node) -> Node:
    list = self.printList(head, [])

    list.reverse()
    # Convert reversed list to Linked List
    reversedHead = self.convertListToLinkedList(list)

    # Get values of new linked list for checking
    # reversedList = self.printList(reversedHead)
    # print(reversedHead)

    return reversedHead


my = Solution()

l0 = Node(1, Node(2, Node(3, Node(4))))

ans = my.reverseList(l0)

# Runtime: 36 ms, faster than 54.91% of Python3 online submissions for Reverse Linked List.
# Memory Usage: 18.6 MB, less than 22.73% of Python3 online submissions for Reverse Linked List.