################################################################
##	Filename: 	LinkedListAdvanced.py				
##	Author: 	Charlotte
##	Email: 		cbgitek@gmail.com
##	Create:   	2016-07-27
##	Modified: 	2016-07-27
################################################################

import random;
import copy;
from LinkedListBasics import *;

class DoublyLinkedList:
	def __init__(self, name="", head=None):
		self.name = name
		self.head = head
		self.tail = head

	def insertAtEnd(self, data):
		newNode = Node(data)
		if not self.head:
			self.head = newNode
			self.tail = newNode
			return
		self.tail.next, newNode.prev, self.tail = newNode, self.tail, newNode
		return

	def insertAtFront(self, data):
		newNode = Node(data)
		if not self.head:
			self.head = newNode
			self.tail = newNode
			return
		newNode.next, self.head.prev, self.head = self.head, newNode, newNode
		return

	def insertNodeAtEnd(self, node):
		if not self.head:
			self.head, self.tail = node, node
			return
		self.tail.next, self.tail, node.prev = node, node, self.tail
		return

	def reverse(self):
		prev, curr = None, self.head
		while curr:
			curr.next, curr.prev, curr, prev = curr.prev, curr.next, curr.next, curr
		self.tail, self.head = self.head, prev
		return

	def printList(self):
		result = []
		runner = self.head
		while runner:
			result.append(str(runner.data))
			runner = runner.next
		print(self.name + ": " + '->'.join(result))		

	@staticmethod
	def ConvertToDoubly(alist):
		"""
		Destructive
		rtype: DoublyLinkedList
		"""
		prev, curr = None, alist.head
		while curr:
			curr.prev, curr, prev = prev, curr.next, curr
		result = DoublyLinkedList("Converted")
		result.head, result.tail = alist.head, prev
		return result

class Algorithm:

	@staticmethod
	def ThreeSumArray(nums, target):
		nums.sort()
		result = []
		for a in range(0, len(nums) - 3):
			b, c = a + 1, len(nums) - 1
			while b < c:
				# By pass duplicate
				if b > 1 and nums[b] == nums[b-1]:
					b += 1
					continue
				if c < len(nums) - 1 and nums[c] == nums[c+1]:
					c -= 1
					continue
				# Test sum
				suml = nums[a] + nums[b] + nums[c]
				if suml == target:
					result.append((a, b, c))
					b, c = b + 1, c - 1
				elif suml < target:
					b += 1
				else:
					c -= 1
		return result

	@staticmethod
	def ThreeSumLinkedList(alist, target):
		"""
		Convert to doubly linked list
		alist: LinkedList, target: int
		rtype: list
		"""
		alist = LinkedList.MergeSort(alist)
		dlist, result = DoublyLinkedList.ConvertToDoubly(alist), []
		aptr = dlist.head
		if not aptr or not aptr.next:
			return result
		while aptr.next.next:
			bptr, cptr = aptr.next, dlist.tail
			while bptr != cptr:
				# Bypass duplicate
				if bptr != dlist.head.next and bptr.data == bptr.prev.data:
					bptr = bptr.next
					continue
				if cptr != dlist.tail and cptr.data == cptr.next.data:
					cptr = cptr.prev
					continue
				# Check for target
				rawsum = aptr.data + bptr.data + cptr.data
				if rawsum == target:
					result.append((aptr.data, bptr.data, cptr.data))
					if bptr.next == cptr:
						break
					bptr, cptr = bptr.next, cptr.prev
				elif rawsum < target:
					bptr = bptr.next
				else:
					cptr = cptr.prev
			aptr = aptr.next
		return result

	@staticmethod
	def ThreeSumThreeList(alist, blist, clist, target):
		"""
		Sort blist, reverse sort clist
		alist, blist, clist: LinkedList
		target: int
		rtype: list
		"""
		if not alist.head or not blist.head or not clist.head:
			return []
		blist = LinkedList.MergeSort(blist)
		clist = LinkedList.MergeSort(clist)
		clist.reverse()

		aptr, result = alist.head, []
		while aptr:
			bptr, cptr = blist.head, clist.head
			while bptr and cptr:
				rawsum = aptr.data + bptr.data + cptr.data
				if rawsum == target:
					result.append([aptr.data, bptr.data, cptr.data])
					bptr, cptr = bptr.next, cptr.next
				elif rawsum < target:
					bptr = bptr.next
				else:
					cptr = cptr.next
			aptr = aptr.next
		return result

	@staticmethod
	def ReversedCopy(alist):
		dummy, aptr = Node(0), alist.head
		while aptr:
			newNode = Node(aptr.data)
			dummy.next, newNode.next = newNode, dummy.next
			aptr = aptr.next
		return LinkedList("Reversed Copy", dummy.next) 

	@staticmethod
	def RotateLinkedList(alist, offset):
		"""
		rtpye: None
		"""
		if not offset:
			return
		prev, curr = None, alist.head
		for i in range(offset):
			prev, curr = curr, curr.next
			if not curr:
				return
		newHead, newTail = curr, prev
		prev, curr = newTail, newHead
		while curr:
			prev, curr = curr, curr.next
		# Rotate
		alist.head, newTail.next, prev.next = newHead, None, alist.head
		return			

	@staticmethod
	def FlattenLinkedListHelper(ahead, bhead):
		"""
		Merge two linked lists
		rtype: Node (head of merged list)
		"""
		dummy_head = Node(0)
		aptr, bptr, dummy = ahead, bhead, dummy_head
		while aptr and bptr:
			adata, bdata = aptr.data, bptr.data
			if aptr.data <= bptr.data:
				aptr.next, aptr, dummy.next, dummy = None, aptr.next, aptr, aptr
			else:
				bptr.next, bptr, dummy.next, dummy = None, bptr.next, bptr, bptr
		if aptr:
			dummy.next = aptr
		else:
			dummy.next = bptr
		return dummy_head.next

	@staticmethod
	def FlattenLinkedList(mnode):
		"""
		mnode: Node
		rtpye: Node (head of flattened list)
		"""
		# rptr stores the result
		rptr, mptr = mnode, mnode.right
		while mptr:
			rptr = Algorithm.FlattenLinkedListHelper(rptr, mptr)
			mptr = mptr.right 
		return rptr

if __name__ == "__main__":
	pass
	# nums = [1, 2, 2, 3, 3, 3]
	# result = Algorithm.ThreeSumArray(nums, 6)
	# print("ThreeSumArray: " + ' '.join([str(x) for x in result]))

	# alist = LinkedList("alist")
	# alist.insertAtEnd(1)
	# alist.insertAtEnd(2)
	# alist.insertAtEnd(3)
	# alist.insertAtEnd(4)
	# alist.insertAtEnd(5)
	# alist.printList()
	# Algorithm.RotateLinkedList(alist, 2)
	# alist.printList()

	node5 = Node(5)
	node7 = Node(7)
	node8 = Node(8)
	node30 = Node(30)
	node10 = Node(10)
	node20 = Node(20)
	node19 = Node(19)
	node22 = Node(22)
	node50 = Node(50)
	node28 = Node(28)
	node35 = Node(35)
	node40 = Node(40)
	node45 = Node(45)
	alist = LinkedList("alist", node5)
	alist.insertNodeAtEnd(node7)
	alist.insertNodeAtEnd(node8)
	alist.insertNodeAtEnd(node30)
	blist = LinkedList("blist", node10)
	blist.insertNodeAtEnd(node20)
	clist = LinkedList("clist", node19)
	clist.insertNodeAtEnd(node22)
	clist.insertNodeAtEnd(node50)
	dlist = LinkedList("dlish", node28)
	dlist.insertNodeAtEnd(node35)
	dlist.insertNodeAtEnd(node40)
	dlist.insertNodeAtEnd(node45)
	node5.right = node10
	node10.right = node19
	node19.right = node28
	alist.printList()
	blist.printList()
	clist.printList()
	dlist.printList()
	result = Algorithm.FlattenLinkedList(alist.head)
	LinkedList.Print(result)

	# alist = LinkedList("alist")
	# alist.insertAtEnd(1)
	# alist.insertAtEnd(2)
	# alist.insertAtEnd(3)
	# alist.insertAtEnd(4)
	# alist.insertAtEnd(5)
	# blist = LinkedList("blist")
	# blist.insertAtEnd(1)
	# blist.insertAtEnd(2)
	# blist.insertAtEnd(3)
	# blist.insertAtEnd(4)
	# blist.insertAtEnd(5)
	# clist = LinkedList("clist")
	# clist.insertAtEnd(1)
	# clist.insertAtEnd(2)
	# clist.insertAtEnd(3)
	# clist.insertAtEnd(4)
	# clist.insertAtEnd(5)
	# threeSumResult = Algorithm.ThreeSumThreeList(alist, blist, clist, 5)
	# print("ThreeSumLinkedList: " + ', '.join([str(x) for x in threeSumResult]))

	# alist = LinkedList("alist")
	# alist.insertAtEnd(1)
	# alist.insertAtEnd(2)
	# alist.insertAtEnd(2)
	# alist.insertAtEnd(2)
	# alist.insertAtEnd(3)
	# alist.insertAtEnd(3)
	# alist.insertAtEnd(0)
	# alist.insertAtEnd(4)
	# threeSumResult = Algorithm.ThreeSumLinkedList(alist, 5)
	# print("ThreeSumLinkedList: " + ', '.join([str(x) for x in threeSumResult]))

