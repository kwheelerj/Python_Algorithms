# Uses python3
__author__ = 'kwheelerj'

import sys
import random


def partition3(a, l, r):
	x = a[l]
	j = l
	k = j + 1
	for i in range(l + 1, r + 1):
		if a[i] < x:
			a[i], a[k] = a[k], a[i]
			j += 1
			a[j], a[k] = a[k], a[j]
			k += 1
		elif a[i] == x:
			a[i], a[k] = a[k], a[i]
			k += 1
	a[l], a[j] = a[j], a[l]
	return j+1, k-1


def partition2(a, l, r):
	x = a[l]
	j = l
	for i in range(l + 1, r + 1):
		if a[i] <= x:
			j += 1
			a[i], a[j] = a[j], a[i]
	a[l], a[j] = a[j], a[l]
	return j


def randomized_quick_sort(a, l, r):
	if l >= r:
		return
	k = random.randint(l, r)
	a[l], a[k] = a[k], a[l]
	m1, m2 = partition3(a, l, r)
	# m = partition2(a, l, r)
	randomized_quick_sort(a, l, m1 - 1)
	randomized_quick_sort(a, m2 + 1, r)


if __name__ == '__main__':
	input = sys.stdin.read()
	# input = input()
	n, *a = list(map(int, input.split()))
	randomized_quick_sort(a, 0, n - 1)
	for x in a:
		print(x, end=' ')
