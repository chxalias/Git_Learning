################################################################
# Filename: 	LinkedListBasics.py
# Author: 		Charlotte
# Email: 		cbgitek@gmail.com
# Create:   	2016-07-23
# Modified: 	2016-07-23
################################################################

import random;
import copy;

class Node:

	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None
		self.right = None 	# special

class LinkedList:

	def __init__(self, name = "List", node = None):
		self.head = node
		self.name = name

	# Insertion
	def insertAtFront(self, data):
		newNode = Node(data)
		newNode.next = self.head
		self.head = newNode

	def insertAtEnd(self, data):
		runner = self.head
		if not runner:				# In case the list is empty
			self.head = Node(data)
			return
		while runner.next != None:
			runner = runner.next
		newNode = Node(data)
		runner.next = newNode

	def insertNodeAtEnd(self, node):
		runner = self.head
		if not runner:				# In case the list is empty
			self.head = node
			return
		while runner.next:
			runner = runner.next
		runner.next = node

	def insertAtIndex(self, index, data):
		runner = self.head
		if not runner:				# In case the list is empty
			self.head = Node(data)
			return
		if index == 0:
			newNode = Node(data)
			newNode.next = self.head
			self.head = newNode
			return
		for i in range(index - 1):
			runner = runner.next
		newNode = Node(data)
		newNode.next = runner.next
		runner.next = newNode

	# Deletion
	def deleteNode(self, data):
		if not self.head:
			return
		if self.head.data == data:
			self.head = self.head.next
			return
		runner = self.head
		while runner.next != None:
			if runner.next.data == data:
				runner.next = runner.next.next
				return
			runner = runner.next

	def deleteNodeAtIndex(self, index):
		if not self.head:
			return
		if index == 0:
			self.head = self.head.next
			return
		runner = self.head
		for i in range(index - 1):
			if not runner:		# Robustness
				return
			runner = runner.next
		if not runner.next:
			return
		runner.next = runner.next.next
		return

	# Length
	def findLengthIteratively(self):
		length = 0
		runner = self.head
		while runner:
			runner = runner.next
			length += 1
		print("Length: " + str(length))

	def findLengthRecursively(self):
		length = self.recursiveHelper(self.head)
		print("Length: " + str(length))

	def recursiveHelper(self, node):
		if not node:
			return 0
		else:
			return self.recursiveHelper(node.next) + 1

	# Search
	def searchForIndexIteratively(self, data):
		runner = self.head
		index = 0
		while runner:
			if runner.data == data:
				print("Index: " + str(index))
				return
			runner = runner.next
			index += 1
		print("Index: -1")
		return

	def searchForIndexRecursively(self, data):
		index = self.searchForIndexRecursivelyHelper(self.head, data, 0)
		print("Index: " + str(index))

	def searchForIndexRecursivelyHelper(self, node, data, index):
		if not node:
			return -1
		elif node.data == data:
			return index
		else:
			return self.searchForIndexRecursivelyHelper(node.next, data, index + 1)

	# Swap
	def swapNodesAtIndices(self, x, y):
		if x == y or x < 0 or y < 0:
			return
		if x > y:
			x, y = y, x
		xprev, xcur, xi = None, self.head, 0
		for i in range(x):
			xprev, xcur = xcur, xcur.next
			if not xcur:
				return
		yprev, ycur, yi = None, self.head, 0
		for i in range(y):
			yprev, ycur = ycur, ycur.next
			if not ycur:
				return
		if xprev == None:
			self.head = ycur
		else:
			xprev.next = ycur
		yprev.next = xcur
		xcur.next, ycur.next = ycur.next, xcur.next
		return

	def getNthNode(self, index):
		if index < 0:
			return -1
		runner, count = self.head, 0
		while runner:
			if count == index:
				return runner.data
			count, runner = count + 1, runner.next
		return -1
		
	def printMiddle(self):
		# find length
		runner, length = self.head, 0
		while runner:
			runner, length = runner.next, length + 1
		# print middle
		runner = self.head
		for i in range(length / 2):
			runner = runner.next
		print("Middle: " + str(runner.data))

	def nthNodeFromEnd(self, n):
		if not n:
			print("index out of bound")
			return
		mptr, rptr = self.head, self.head
		for i in range(n):
			if not rptr:
				print("index out of bound")
				return
			rptr = rptr.next
		while rptr:
			mptr, rptr = mptr.next, rptr.next
		print(str(n) + " th node from the end: " + str(mptr.data))

	def reverse(self):
		prev, curr = None, self.head
		while curr:
			curr.next, prev, curr = prev, curr, curr.next
		self.head = prev
		return

	def detectLoop(self):
		"""
		Check whether a loop exist on a linked list
		rtype: bool
		"""
		slow, fast = self.head, self.head
		while fast and fast.next:
			slow, fast = slow.next, fast.next.next
			if slow == fast:
				return True
		return False

	def detectLoopPosition(self):
		"""
		Return the start index of the loop
		rtype: (int from, int to)
		"""

		# Floyd's method
		slow, fast = self.head, self.head
		while fast and fast.next:
			slow, fast = slow.next, fast.next.next
			if slow == fast:
				break

		if not fast or not fast.next:
			return -1	# there isn't a loop

		# Find loop position
		slow, toPos = self.head, 0
		while slow != fast:
			slow, fast = slow.next, fast.next
			toPos += 1
		fast, fromPos = fast.next, toPos
		while slow != fast:
			fast = fast.next
			fromPos += 1
		return (fromPos, toPos)

	def makeLoop(self, fromIndex, toIndex):
		"""
		Assign from -> to
		"""
		if fromIndex < 0 or toIndex < 0:
			return
		fromNode, toNode = self.head, self.head
		for i in range(fromIndex):
			if not fromNode:
				return
			fromNode = fromNode.next
		for i in range(toIndex):
			if not toNode:
				return
			toNode = toNode.next
		fromNode.next = toNode

	@staticmethod
	def SortedMerge(Alist, Blist):
		"""
		Merge two sorted list (destructive)
		rtype: LinkedList
		"""
		clist = LinkedList()
		clist.head = Node(0)	# dummy head
		aptr, bptr, cptr = Alist.head, Blist.head, clist.head
		while aptr and bptr:
			if aptr.data <= bptr.data:
				cptr.next, aptr = aptr, aptr.next
			else:
				cptr.next, bptr = bptr, bptr.next
			cptr = cptr.next
		if aptr:
			cptr.next = aptr
		else:
			cptr.next = bptr
		clist.head = clist.head.next
		return clist

	def insertSorted(self, data):
		prev, curr = None, self.head
		while curr:
			if data > curr.data:
				prev, curr = curr, curr.next
			else:
				break
		newNode = Node(data)
		newNode.next = curr
		if not prev:
			self.head = newNode
		else:
			prev.next = newNode
		return

	def isPalindrome(self):
		"""
		Use a stack, O(n) time, O(n) space
		"""
		stack, runner = [], self.head
		while runner:
			stack.append(runner.data)
			runner = runner.next
		runner = self.head
		while runner:
			if runner.data != stack.pop():
				return False
			runner = runner.next
		return True

	def isPalindromeOptimized(self):
		"""
		Find the middle of list, reverse the second half,
		Compare the first half and second half,
		O(n) time, O(1) space, destructive
		"""
		if not self.head or not self.head.next:
			return True
		# Find the middle
		slow, fast = self.head, self.head
		while fast and fast.next:
			slow, fast = slow.next, fast.next.next
		# Reverse the second half
		prev, curr = None, slow
		while curr:
			curr.next, prev, curr = prev, curr, curr.next
		# Compare two lists
		first, result = self.head, True
		second = prev	# head of the reversed list
		while second:
			if first.data != second.data:
				result = False
				break
			first, second = first.next, second.next
		# Restore the list
		prev, curr = None, prev
		while curr:
			curr.next, prev, curr = prev, curr, curr.next
		return result

	@staticmethod
	def Intersection_Loop(alist, blist):
		"""
		Use two loops
		O(m*n) time, O(1) space
		rtype: Node
		"""
		aptr = alist.head
		while aptr:
			bptr = blist.head
			while bptr:
				if aptr == bptr:
					return aptr
				bptr = bptr.next
			aptr = aptr.next
		return None

	@staticmethod
	def Intersection_Set(alist, blist):
		"""
		Mark visited nodes
		O(m+n) time, O(n) space
		rtype: Node
		"""
		visited = set()
		runner = blist.head
		while runner:
			visited.add(runner)
			runner = runner.next
		runner = alist.head
		while runner:
			if runner in visited:
				return runner
			runner = runner.next
		return

	@staticmethod
	def Intersection_Dummy(alist, blist):
		"""
		Destroy one of the two lists
		O(m+n) time, O(1) space, destructive
		rtype: Node
		"""

		# Destroy blist
		runner, dummy = blist.head, Node(-1)
		while runner:
			runner.next, runner = dummy, runner.next
		# Go through alist
		prev, curr = None, alist.head
		while curr:
			if curr.data == -1:
				return prev
			prev, curr = curr, curr.next
		return None

	@staticmethod
	def Intersection_Optimized(alist, blist):
		"""
		Use the difference of node counts
		O(m+n) time, O(1) space
		rtype: Node
		"""

		# Get the length of both lists
		aLength, bLength, runner = 0, 0, alist.head
		while runner:
			runner, aLength = runner.next, aLength + 1
		runner = blist.head
		while runner:
			runner, bLength = runner.next, bLength + 1
		# Calculate the difference, swap if necessary
		if aLength < bLength:
			aLength, alist, bLength, blist = bLength, blist, aLength, alist
		diff = aLength - bLength
		# Advance the longer list
		runner = alist.head
		for i in range(diff):
			runner = runner.next
		# Advance both list until intersection is reached
		aptr, bptr = runner, blist.head
		while aptr:
			if aptr == bptr:
				return aptr
			aptr, bptr = aptr.next, bptr.next
		return None

	@staticmethod
	def Intersection_Optimized_Loop(alist, blist):
		"""
		Convert to list loop problem
		O(m+n) time, O(1) space
		rtype: Node
		"""

		# Make blist a loop
		bptr, loop_len = blist.head, 1
		while bptr.next:
			bptr, loop_len = bptr.next, loop_len + 1
		bEnd = bptr		# for restoring
		bptr.next = blist.head
		# Advance alist by loop_len
		aptr = alist.head
		for i in range(loop_len):
			aptr = aptr.next
		# Start another pointer from alist.head
		ref = alist.head
		while ref != aptr:
			ref, aptr = ref.next, aptr.next
		# Restore blist
		bEnd = None
		return ref

	def printReverse(self):
		self.printReverseHelper(self.head)
		print()

	def printReverseHelper(self, node):
		if not node.next:
			print(str(node.data), end="")
			return
		else:
			self.printReverseHelper(node.next)
			print("->" + str(node.data), end="")
			return

	def removeDuplicateSorted(self):
		prev, curr = self.head, self.head.next
		while curr:
			if prev.data == curr.data:
				prev.next, curr = curr.next, curr.next
			else:
				prev, curr = prev.next, curr.next
		return

	def removeDuplicateUnsorted(self):
		hashSet = set()
		hashSet.add(self.head.data)
		prev, curr = self.head, self.head.next
		while curr:
			if curr.data in hashSet:
				prev.next, curr = curr.next, curr.next
			else:
				hashSet.add(curr.data)
				prev, curr = prev.next, curr.next
		return

	def pairWiseSwap(self):
		"""
		Use dummy head
		"""
		if not self.head:
			return
		# Add dummy node
		dummy = Node(0)
		dummy.next, self.head = self.head, dummy
		# Swap
		xprev, x, y = dummy, dummy.next, dummy.next.next
		while y:
			xprev.next, y.next, x.next = y, x, y.next
			if not x.next:	# use x instead of y
				break
			xprev, x, y = x, x.next, x.next.next
		# Restore
		self.head = dummy.next
		return

	@staticmethod
	def MergeSort(alist):
		"""
		rtype: LinkedList
		"""
		# Base case
		head = alist.head
		if not head or not head.next:
			return alist
		if not head.next.next:
			if head.data > head.next.data:
				head.next.next, head.next, alist.head = head, None, head.next
			return alist
		# Divide
		# print("Processing list: ", end="")
		# alist.printList()
		slow, fast = head, head
		while fast.next and fast.next.next:
			slow, fast = slow.next, fast.next.next
		left_list, right_list = LinkedList("left_list"), LinkedList("right_list")
		left_list.head, right_list.head = head, slow.next
		slow.next = None  	# break into two lists
		left_list = LinkedList.MergeSort(left_list)
		right_list = LinkedList.MergeSort(right_list)
		# Merge
		dummy = Node(0)
		dummy_head, lptr, rptr = dummy, left_list.head, right_list.head
		while lptr and rptr:
			if lptr.data < rptr.data:
				dummy.next, dummy, lptr = lptr, lptr, lptr.next
			else:
				dummy.next, dummy, rptr = rptr, rptr, rptr.next
		if lptr:
			dummy.next = lptr
		else:
			dummy.next = rptr
		# Restore
		sorted_list = LinkedList("Sorted")
		sorted_list.head = dummy_head.next
		return sorted_list

	def reverseGroups(self, groupSize):
		# Attach dummy head
		dummy_head = Node(0)
		dummy_head.next = self.head
		# Loop
		dummy, prev, curr = dummy_head, dummy_head, self.head
		while True:
			for i in range(groupSize):
				if not curr:
					break
				curr.next, curr, prev = prev, curr.next, curr
			dummy.next.next, dummy.next, newDummy = curr, prev, dummy.next
			if curr:
				prev, dummy = newDummy, newDummy
			else:
				break
		self.head = dummy_head.next
		return

	def reverseAlternateGroups(self, k):
		"""
		Reverse every other k nodes by calling reverseHelper()
		"""
		# Attach dummy
		dummy_head = Node(0)
		dummy_head.next = self.head
		runner = dummy_head
		while True:
			runner.next = self.reverseHelper(runner.next, k)
			for i in range(2*k):
				if not runner.next:
					self.head = dummy_head.next
					return
				runner = runner.next


	def reverseHelper(self, head, k):
		"""
		Reverse k nodes starting from head
		rtype: Node (new head)
		"""
		# Attach dummy
		dummy_head = Node(0)
		dummy_head.next = head
		# Reverse
		prev, curr, i = dummy_head, head, 0
		while i < k and curr:
			curr.next, prev, curr = prev, curr, curr.next
			i += 1
		# Fix links
		dummy_head.next.next = curr
		return prev

	def deleteLesserNodes(self):
		"""
		Delete nodes which have a greater value on the right side
		"""
		dummy = Node(0)
		dummy.next = self.head
		prev, curr = dummy, dummy.next
		while curr.next:
			if curr.data < curr.next.data:
				prev.next, curr = curr.next, curr.next
			else:
				prev, curr = curr, curr.next
		self.head = dummy.next
		return

	def separateEvenOdd(self):
		"""
		Separate even and odd nodes
		"""
		even_dummy, odd_dummy = Node(0), Node(0)
		even_dummy.next = self.head
		prev, curr, optr = even_dummy, self.head, odd_dummy
		# Loop
		while curr:
			if curr.data % 2 != 0:
				prev.next, curr, optr.next, optr = curr.next, curr.next, curr, curr
				optr.next = None
			else:
				prev, curr = curr, curr.next
		# Attach odd list
		prev.next = odd_dummy.next
		self.head = even_dummy.next
		return

	@staticmethod
	def addTwoLists(alist, blist):
		"""
		Example: 5->6->3 + 8->4->2 = 3->1->6
		"""
		dummy, aptr, bptr, carry = Node(0), alist.head, blist.head, 0
		dummy_head = dummy
		while aptr and bptr:
			rawsum = aptr.data + bptr.data + carry
			dummy.next, carry = Node(rawsum % 10), rawsum // 10
			dummy, aptr, bptr = dummy.next, aptr.next, bptr.next
		remainder = aptr
		if not aptr:
			remainder = bptr
		while remainder:
			rawsum = remainder.data + carry
			dummy.next, carry = Node(rawsum % 10), rawsum // 10
			dummy, remainder = dummy.next, remainder.next
		if carry:
			dummy.next = Node(carry)
		result = LinkedList("Sum list", dummy_head.next)
		return result

	@staticmethod
	def Reversed(alist):
		prev, curr = None, alist.head
		while curr:
			curr.next, prev, curr = prev, curr, curr.next
		return LinkedList("Reversed list", prev)

	@staticmethod
	def DeleteNodeCondition(head, nodeToDelete):
		# If the node to delete is the first node
		if head == nodeToDelete:
			head.data = head.next.data
			head.next = head.next.next
			return
		# General case
		prev, curr = head, head.next
		while curr:
			if curr == nodeToDelete:
				prev.next, curr = curr.next, curr.next
				return
			prev, curr = curr, curr.next
		# No node deleted
		return

	@staticmethod
	def Union_Sort(alist, blist):
		if not alist.head or not blist.head:
			return alist
		clist = LinkedList.CombineList(alist, blist)
		sortedList = LinkedList.MergeSort(clist)
		dummy_head = Node(0)
		dummy_head.next = sortedList.head
		prev, curr = dummy_head, dummy_head.next
		while curr.next:
			if curr.data == curr.next.data:
				prev.next, curr = curr.next, curr.next
			else:
				prev, curr = curr, curr.next
		return LinkedList("Union List", dummy_head.next)

	@staticmethod
	def Intersection_Sort(alist, blist):
		# O(nlogn)
		alist = LinkedList.MergeSort(alist)
		blist = LinkedList.MergeSort(blist)
		dummy_head = Node(0)
		dptr, aptr, bptr = dummy_head, alist.head, blist.head
		# Add common nodes, O(min(m, n))
		while aptr and bptr:
			if aptr.data == bptr.data:
				aptr.next, aptr, dptr.next, dptr = None, aptr.next, aptr, aptr
				bptr = bptr.next
			elif aptr.data < bptr.data:
				aptr = aptr.next
			else:
				bptr = bptr.next
		# Get rid of duplicates, O(min(m, n))
		prev, curr = dummy_head, dummy_head.next
		while curr.next:
			if curr.data == curr.next.data:
				prev.next, curr = curr.next, curr.next
			else:
				prev, curr = curr, curr.next
		# Return list
		rlist = LinkedList("Intersection List", dummy_head.next)
		return rlist

	@staticmethod
	def CombineList(alist, blist):
		"""
		Destructive
		rtype: LinkedList
		"""
		aptr = alist.head
		if not aptr:
			return blist
		while aptr.next:
			aptr = aptr.next
		aptr.next = blist.head
		return alist

	@staticmethod
	def DeepCopy(alist):
		"""
		rtype: LinkedList
		"""
		dummy_head = Node(0)
		dptr, aptr = dummy_head, alist.head
		while aptr:
			dptr.next = copy.deepcopy(aptr)
			dptr.next.next, dptr = None, dptr.next
			aptr = aptr.next
		return LinkedList("Copy List", dummy_head.next)

	# Utilities
	def printList(self):
		result = []
		runner = self.head
		while runner:
			# print(str(runner.data))
			result.append(str(runner.data))
			runner = runner.next
		print(self.name + ": " + '->'.join(result))

	@staticmethod
	def Print(anode, name="List"):
		result = []
		while anode:
			result.append(str(anode.data))
			anode = anode.next
		print(name + ": " + '->'.join(result))
		return

if __name__ == "__main__":
	pass

	alist = LinkedList("alist")
	alist.insertAtEnd(7)
	alist.insertAtEnd(5)
	alist.insertAtEnd(9)
	alist.insertAtEnd(4)
	alist.insertAtEnd(6)
	alist.insertAtEnd(9)
	alist.insertAtEnd(4)
	alist.insertAtEnd(6)
	alist.printList()
	blist = LinkedList("blist")
	blist.insertAtEnd(8)
	blist.insertAtEnd(4)
	blist.insertAtEnd(6)
	blist.insertAtEnd(7)
	blist.insertAtEnd(5)
	blist.insertAtEnd(9)
	blist.insertAtEnd(4)
	blist.insertAtEnd(6)
	blist.printList()
	unionList = LinkedList.Union_Sort(LinkedList.DeepCopy(alist), LinkedList.DeepCopy(blist))
	intersectionList = LinkedList.Intersection_Sort(LinkedList.DeepCopy(alist), LinkedList.DeepCopy(blist))
	unionList.printList()
	intersectionList.printList()

	# node3 = Node(3)
	# node6 = Node(6)
	# node9 = Node(9)
	# node10 = Node(10)
	# node15 = Node(15)
	# node30 = Node(30)
	# alist = LinkedList("alist")
	# alist.insertNodeAtEnd(node3)
	# alist.insertNodeAtEnd(node6)
	# alist.insertNodeAtEnd(node9)
	# alist.insertNodeAtEnd(node10)
	# alist.insertNodeAtEnd(node15)
	# alist.insertNodeAtEnd(node30)
	# alist.printList()
	# LinkedList.DeleteNodeCondition(alist.head, node3)
	# alist.printList()


	# alist = LinkedList("alist")
	# alist.insertAtEnd(7)
	# alist.insertAtEnd(5)
	# alist.insertAtEnd(9)
	# alist.insertAtEnd(4)
	# alist.insertAtEnd(6)
	# alist.printList()
	# blist = LinkedList("blist")
	# blist.insertAtEnd(8)
	# blist.insertAtEnd(4)
	# blist.printList()
	# sumList = LinkedList.addTwoLists(alist, blist)
	# sumList.printList()
	# reversedList = LinkedList.Reversed(sumList)
	# reversedList.printList()

	# alist = LinkedList("alist")
	# alist.insertAtEnd(17)
	# alist.insertAtEnd(15)
	# alist.insertAtEnd(8)
	# alist.insertAtEnd(12)
	# alist.insertAtEnd(10)
	# alist.insertAtEnd(5)
	# alist.insertAtEnd(4)
	# alist.insertAtEnd(1)
	# alist.insertAtEnd(7)
	# alist.insertAtEnd(6)
	# alist.printList()
	# alist.separateEvenOdd()
	# alist.printList()

	# alist = LinkedList("alist")
	# alist.insertAtEnd(0)
	# alist.insertAtEnd(1)
	# alist.insertAtEnd(2)
	# alist.insertAtEnd(3)
	# alist.insertAtEnd(4)
	# alist.insertAtEnd(5)
	# alist.insertAtEnd(6)
	# # alist.insertAtEnd(7)
	# alist.printList()
	# alist.reverseAlternateGroups(4)
	# alist.printList()

	# alist = LinkedList("alist")
	# alist.insertAtEnd(random.randint(1, 9))
	# alist.insertAtEnd(random.randint(1, 9))
	# alist.insertAtEnd(random.randint(1, 9))
	# alist.insertAtEnd(random.randint(1, 9))
	# alist.insertAtEnd(random.randint(1, 9))
	# alist.insertAtEnd(random.randint(1, 9))
	# alist.insertAtEnd(random.randint(1, 9))
	# alist.insertAtEnd(random.randint(1, 9))
	# alist.printList()
	# sorted_list = LinkedList.MergeSort(alist)
	# sorted_list.printList()

	# node3 = Node(3)
	# node6 = Node(6)
	# node9 = Node(9)
	# node10 = Node(10)
	# node15 = Node(15)
	# node30 = Node(30)
	# alist = LinkedList("alist")
	# alist.insertNodeAtEnd(node3)
	# alist.insertNodeAtEnd(node6)
	# alist.insertNodeAtEnd(node9)
	# alist.insertNodeAtEnd(node15)
	# alist.insertNodeAtEnd(node30)
	# blist = LinkedList("blist")
	# blist.insertNodeAtEnd(node10)
	# blist.insertNodeAtEnd(node15)
	# alist.printList()
	# blist.printList()
	# print(str(LinkedList.Intersection_Optimized_Loop(alist, blist).data))

	# alist = LinkedList()
	# alist.insertAtEnd(1)
	# alist.insertAtEnd(2)
	# alist.insertAtEnd(3)
	# alist.insertAtEnd(4)
	# alist.insertAtEnd(4)
	# alist.insertAtEnd(3)
	# alist.insertAtEnd(1)
	# alist.printList()
	# print(str(alist.isPalindromeOptimized()))
	# alist.printList()

	# alist = LinkedList()
	# alist.insertAtEnd(1)
	# alist.insertAtEnd(3)
	# alist.insertAtEnd(5)
	# alist.insertAtEnd(6)
	# alist.printList()
	# alist.insertSorted(4)
	# alist.insertSorted(0)
	# alist.insertSorted(7)
	# alist.insertSorted(5)
	# alist.printList()

	# alist = LinkedList()
	# alist.insertAtEnd(1)
	# alist.insertAtEnd(2)
	# alist.insertAtEnd(5)
	# blist = LinkedList()
	# blist.insertAtEnd(1)
	# blist.insertAtEnd(4)
	# blist.insertAtEnd(8)
	# blist.insertAtEnd(12)

	# alist.printList()
	# blist.printList()
	# clist = LinkedList.SortedMerge(alist, blist)
	# clist.printList()

	# llist = LinkedList()
	# llist.insertAtEnd(1)
	# llist.insertAtEnd(2)
	# llist.insertAtEnd(3)
	# llist.insertAtEnd(4)
	# llist.insertAtEnd(5)
	# llist.printList()
	# llist.makeLoop(0, 1)
	# print("detectLoop(): " + str(llist.detectLoop()))
	# print("detectLoopPosition(): " + str(llist.detectLoopPosition()))
	# # llist.printList()


	# llist = LinkedList()
	# llist.insertAtEnd(2)
	# llist.insertAtEnd(3)
	# llist.insertAtEnd(4)
	# llist.insertAtEnd(5)
	# llist.printList()
	# llist.swapNodesAtIndices(3, 2)
	# llist.printList()

	# llist = LinkedList()
	# llist.insertAtFront(2)
	# llist.insertAtFront(3)
	# llist.insertAtFront(4)
	# llist.insertAtFront(5)
	# llist.printList()

	# llist = LinkedList()
	# llist.insertAtEnd(2)
	# llist.insertAtEnd(3)
	# llist.insertAtEnd(4)
	# llist.insertAtEnd(5)
	# llist.printList()

	# llist = LinkedList()
	# llist.insertAtIndex(0, 2)
	# llist.insertAtIndex(1, 3)
	# llist.insertAtIndex(0, 4)
	# llist.insertAtIndex(2, 5)
	# llist.printList()

	# llist = LinkedList()
	# llist.insertAtEnd(2)
	# llist.insertAtEnd(3)
	# llist.insertAtEnd(4)
	# llist.insertAtEnd(5)
	# llist.deleteNode(4)
	# llist.deleteNode(5)
	# llist.deleteNode(6)
	# llist.printList()

	# llist = LinkedList()
	# llist.insertAtEnd(2)
	# llist.insertAtEnd(3)
	# llist.insertAtEnd(4)
	# llist.insertAtEnd(5)
	# llist.deleteNodeAtIndex(0)
	# llist.deleteNodeAtIndex(2)
	# llist.deleteNodeAtIndex(1)
	# llist.printList()

	# llist = LinkedList()
	# llist.insertAtEnd(2)
	# llist.insertAtEnd(3)
	# llist.insertAtEnd(4)
	# llist.insertAtEnd(5)
	# llist.printList()
	# llist.findLengthIteratively()
	# llist.findLengthRecursively()

	# llist = LinkedList()
	# llist.insertAtEnd(2)
	# llist.insertAtEnd(3)
	# llist.insertAtEnd(4)
	# llist.insertAtEnd(5)
	# llist.printList()
	# llist.searchForIndexIteratively(2)
	# llist.searchForIndexIteratively(5)
	# llist.searchForIndexIteratively(10)
	# llist.searchForIndexIteratively(-2)
	# llist.searchForIndexRecursively(2)
	# llist.searchForIndexRecursively(5)
	# llist.searchForIndexRecursively(10)
	# llist.searchForIndexRecursively(-2)
