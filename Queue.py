class Queue:
	""" A Simple Queue Data Structure"""
	def __init__(self):
		self.data = []

	def isEmpty(self):
		""" Check whether the queue is empty."""
		if len(self.data) < 1:
			return True
		else:
			return False
		
	def enqueue(self, val):
		""" Add an element to the queue."""
		self.data.append(val)

	def dequeue(self):
		""" Remove the next element from the queue."""
		if self.isEmpty():
			return None
		else:
			return self.data.pop(0)

	def peek(self):
		""" Return the next element from the queue without removing it."""
		if self.isEmpty():
			return None
		else:
			return self.data[0]

def test_Queue():
	import random
	queue = Queue()

	for _ in range(10):
		queue.enqueue(random.randrange(100))

	print("Queue contents: ")
	for e in queue.data:
		print(e)

	print("---------------------")
	print("Dequeue: {}".format(queue.dequeue()))
	print("Enqueue 0")
	queue.enqueue(0)
	print("Dequeue: {}".format(queue.dequeue()))
	print("Last element in queue: {}".format(queue.data[-1]))

if __name__ == '__main__':
	test_Queue()
	