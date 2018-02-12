# Uses python3
__author__ = 'kwheelerj'

import sys
import math

def binary_search(a, low, high, x):
	left = low
	right = high - 1
	# print('x is ' + str(x))
	# print('left is ' + str(left))
	# print('right is ' + str(right))
	if right < left:
		return -1
	mid = math.floor(left + ((right - left)/2))
	# print('mid is ' + str(mid))
	# print('a[mid] is ' + str(a[mid]))
	# print(x > a[mid])
	if x == a[mid]:
		return mid
	elif x < a[mid]:
		return binary_search(a, low, mid, x)
	else:
		return binary_search(a, mid+1, high, x)

def linear_search(a, x):
	for i in range(len(a)):
		if a[i] == x:
			return i
	return -1

if __name__ == '__main__':
	input = sys.stdin.read()
	data = list(map(int, input.split()))
	# inp = input()
	# data = list(map(int, inp.split()))
	n = data[0]
	m = data[n + 1]
	a = data[1:n+1]
	# answers = []
	for x in data[n+2:]:
		# replace with the call to binary_search when implemented
		# print(linear_search(a, x), end=' ')
		print(binary_search(a, 0, n, x), end=' ')
		# answers.append(binary_search(a, 0, n, x))
	# print(answers)
