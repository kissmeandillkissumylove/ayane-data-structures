class Stack:

	head = None
	lenght = 0

	class Node:

		def __init__(self, data, next=None):

			self.data = data
			self.next = next

	def add(self, data):

		self.lenght += 1
		if not self.head:
			self.head = self.Node(data, None)
			return
		else:
			new_node = self.Node(data, self.head)
			self.head = new_node
			return

	def pop(self):

		self.lenght -= 1
		if not self.head:
			return
		else:
			poped = self.head
			self.head = self.head.next
			return poped

	def print(self):

		node = self.head
		while node:
			print(node.data, end=" ")
			node = node.next
		print()
		return

if __name__ == "__main__":
	stack = Stack()
	for elt in range(0, 31):
		stack.add(elt)
	stack.print()
	print(stack.lenght)
	stack.pop()
	stack.print()
	print(stack.lenght)