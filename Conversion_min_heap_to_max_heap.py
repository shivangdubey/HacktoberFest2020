# return left child of A[i]
def LEFT(i):
	return 2 * i + 1


# return right child of A[i]
def RIGHT(i):
	return 2 * i + 2


# Utility function to swap two indices in the list
def swap(A, i, j):

	temp = A[i]
	A[i] = A[j]
	A[j] = temp


# Recursive Heapify-down algorithm. The node at index i and
# its two direct children violates the heap property
def Heapify(A, i, size):

	# get left and right child of node at index i
	left = LEFT(i)
	right = RIGHT(i)

	smallest = i

	# compare A[i] with its left and right child
	# and find smallest value
	if left < size and A[left] < A[i]:
		smallest = left

	if right < size and A[right] < A[smallest]:
		smallest = right

	# swap with child having lesser value and
	# call heapify-down on the child
	if smallest != i:
		swap(A, i, smallest)
		Heapify(A, smallest, size)


# Constructor (Build-Heap)
def Convert(A):

	# call heapify starting from last internal node all the
	# way up to the root node
	i = (len(A) - 2) // 2
	while i >= 0:
		Heapify(A, i, len(A))
		i = i - 1


if __name__ == '__main__':

	"""
				9

		 4		 7

		1	-2	6	 5

	"""

	# list representing max heap
	A = [9, 4, 7, 1, -2, 6, 5]

	# build a min heap by initializing it by given list
	Convert(A)

	# print the Min Heap
	"""
			-2

		1		 5

	9	 4	6	 7

	"""

	print(A)
