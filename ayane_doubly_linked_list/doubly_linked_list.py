class DoublyLinkedList:
	head = None
	tail = None
	lenght = 0

	class Node:

		def __init__(self, data, prev=None, next=None):
			self.data = data
			self.prev = prev
			self.next = next

	def add_in_top(self, data):
		if not self.head:
			self.head = self.Node(data=data)
			self.tail = self.head
			self.lenght += 1
			return
		else:
			new_head = self.Node(data=data, next=self.head)
			self.head.prev = new_head
			self.head = new_head
			self.lenght += 1
			return

	def add_in_end(self, data):
		if not self.tail:
			self.add_in_top(data=data)
		else:
			new_tail = self.Node(data=data, prev=self.tail)
			self.tail.next = new_tail
			self.tail = new_tail
			self.lenght += 1
			return

	def insert(self, index, data):
		if index == 0:
			self.add_in_top(data=data)
		elif index == self.lenght:
			self.add_in_end(data=data)
		else:
			if index >= (self.lenght - 1) // 2:
				node, ii = self.tail, self.lenght - 1
				while True:
					if ii == index:
						new_node = self.Node(data=data, prev=node.prev, next=node)
						node.prev.next = new_node
						node.prev = new_node
						self.lenght += 1
						break
					node = node.prev
					ii -= 1
				return
			else:
				node, ii = self.head, 0
				while True:
					if ii == index:
						new_node = self.Node(data=data, prev=node.prev, next=node)
						node.prev.next = new_node
						node.prev = new_node
						self.lenght += 1
						break
					node = node.next
					ii += 1
				return

	def replace(self, index, data):
		if index == 0:
			self.head.data = data
			return
		elif index == self.lenght - 1:
			self.tail.data = data
			return
		else:
			if index >= (self.lenght - 1) // 2:
				node, ii = self.tail, self.lenght - 1
				while True:
					if ii == index:
						node.data = data
						break
					node = node.prev
					ii -= 1
				return
			else:
				node, ii = self.head, 0
				while True:
					if ii == index:
						node.data = data
						break
					node = node.next
					ii += 1
				return

	def get(self, index):
		if index == 0:
			return self.head.data
		if index == self.lenght - 1:
			return self.tail.data
		else:
			if index >= (self.lenght - 1) // 2:
				node, ii = self.tail, self.lenght - 1
				while True:
					if ii == index:
						return node.data
					node = node.prev
					ii -= 1
			else:
				node, ii = self.head, 0
				while True:
					if ii == index:
						return node.data
					node = node.next
					ii += 1

	def delete(self, index):
		if index == 0:
			self.head = self.head.next
			self.head.prev = None
			self.lenght -= 1
			return
		elif index == self.lenght - 1:
			self.tail = self.tail.prev
			self.tail.next = None
			self.lenght -= 1
			return
		else:
			if index >= (self.lenght - 1) // 2:
				node, ii = self.tail, self.lenght - 1
				while True:
					if ii == index:
						node.prev.next = node.next
						node.next = node.prev
						self.lenght -= 1
						return
					node = node.prev
					ii -= 1
			else:
				node, ii = self.head, 0
				while True:
					if ii == index:
						node.prev.next = node.next
						node.next = node.prev
						self.lenght -= 1
						return
					node = node.next
					ii += 1

	def print(self):
		print("___doubly-linked-list___________")
		print("lenght =", self.lenght, end=", ")
		print("head =", self.head.data, end=", ")
		print("tail =", self.tail.data)
		print("data = ", end="")
		current_node = self.head
		while current_node:
			print(current_node.data, end=" ")
			current_node = current_node.next
		print("\n" + "\u203e"*28)
		return


if __name__ == "__main__":
	dll = DoublyLinkedList()
	dll.add_in_top(16)
	dll.add_in_top(9)
	dll.add_in_end(25)
	dll.insert(0, 1)
	dll.insert(4, 49)
	dll.insert(4, 36)
	dll.insert(1, 4)
	for elt in range(2, dll.lenght+1):
		dll.replace(elt-1, elt**3)
	dll.print()
	print(dll.get(0), dll.get(2), dll.get(5), dll.get(6))
	dll.delete(0)
	dll.delete(5)
	dll.delete(2)
	dll.print()