class Stack:
	""" Simple Stack Data Structure"""
	def __init__(self):
		self.top = -1
		self.data = []
	  
	def isEmpty(self):
		""" Check for an empty Stack"""
		return self.top == -1

	def push(self, val):
		""" Add an element to the top of the Stack. """
		self.data.append(val)
		self.top += 1

	def pop(self):
		""" Pop the top element. """
		if self.isEmpty():
		  raise Exception('Can\'t pop from an empty Stack.')
		else:
		  self.top -= 1
		  return self.data.pop(self.top + 1)

	def size(self):
		""" Return the size of the stack."""
		return self.top + 1

	def peek(self):
		""" Get the value off the top without removing it."""
		if self.isEmpty():
		  return None
		else:
		  return self.data[self.top]


def test_Stack():
	import random
	stack = Stack()

	for i in range(10):
		stack.push(random.randrange(100))

	print("Stack contents:")
	for e in stack.data:
		print(e)

	print("-----------------------")
	print("Peek: {}".format(stack.peek()))
	print("Pop an element: {}".format(stack.pop()))
	print("Peek: {}".format(stack.peek()))
	print("Pop again: {}".format(stack.pop()))
	print("Push 0")
	stack.push(0)
	print("Peek: {}".format(stack.peek()))
	

if __name__ == '__main__':
	test_Stack()