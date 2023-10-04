class SinglyLinkedList:
	head = None
	lenght = 0

	class Node:
		def __init__(self, data, next=None):
			self.data = data
			self.next = next

	def append(self, data):
		if not self.head:
			self.head = self.Node(data, None)
			self.lenght += 1
			return
		node = self.head
		while node.next:
			node = node.next
		node.next = self.Node(data)
		self.lenght += 1

	def insert(self, index, data):
		if index == 0:
			self.head = self.Node(data, self.head)
			self.lenght += 1
			return
		node = self.head
		index -= 1
		while index != 0:
			node = node.next
			index -= 1
			if index == 0:
				node.next = self.Node(data, node.next)
				self.lenght += 1

	def replace(self, index, data):
		if index == 0:
			self.head.data = data
			return
		node = self.head
		while index != 0:
			index -= 1
			node = node.next
			if index == 0:
				node.data = data
				break

	def get(self, index):
		if index == 0:
			return self.head.data
		node = self.head
		while index != 0:
			node = node.next
			index -= 1
			if index == 0:
				return node.data

	def remove(self, data):
		if self.head.data == data:
			self.head = self.head.next
			self.lenght -= 1
			return
		node = self.head
		while node:
			if node.next.data == data:
				node.next = node.next.next
				self.lenght -= 1
				break
			node = node.next

	def delete(self, index):
		if index == 0:
			self.head = self.head.next
			self.lenght -= 1
			return
		node = self.head
		while index != 0:
			index -= 1
			if index == 0:
				node.next = node.next.next
				self.lenght -= 1
				break
			node = node.next

	def print(self):
		node = self.head
		while node.next:
			print(node.data, end=", ")
			node = node.next
		print(node.data)

if __name__ == "__main__":
	sll = SinglyLinkedList()
	sll.append(10)
	sll.append(56)
	sll.append(5657)
	sll.append(547)
	sll.print()
	print("len =", sll.lenght)
	for elt in range(0, 11):
		sll.insert(2, elt)
	sll.print()
	print("len =", sll.lenght)
	print(sll.get(1), sll.get(0), sll.get(13))
	sll.remove(7)
	sll.print()
	sll.delete(11)
	sll.replace(2, 10000)
	sll.print()
	print("len =", sll.lenght)