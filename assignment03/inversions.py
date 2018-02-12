# Uses python3
__author__ = 'kwheelerj'

import sys
import math


def get_number_of_inversions(a, b, left, right):

	for i in range(left + 1, right):
		if a[i] < a[i-1]:
			key = a[i]
			b += get_inv_helper(a[left:i], key)
	return b


def get_inv_helper(a, key):
	if not a:
		return 0
	if a[0] > key:
		return len(a)
	if len(a) == 1:
		if a[0] > key:
			return 1
		else:
			return 0

	mid = math.floor(len(a) / 2)
	b = get_inv_helper(a[0:mid], key)
	c = get_inv_helper(a[mid:], key)
	_a = b + c
	return _a


if __name__ == '__main__':
	input = sys.stdin.read()
	# input = input()
	n, *a = list(map(int, input.split()))
	b = 0
	print(get_number_of_inversions(a, b, 0, len(a)))
