# Uses python3
__author__ = 'kwheelerj'

import sys


# def optimal_summands(n):
# 	summands = []
# 	if n == 2:
# 		summands.append(2)
# 	else:
# 		summands = optimal_summands_helper(n, n, 1, summands)
# 	return summands
#
#
# def optimal_summands_helper(n, k, L, summands):
#
# 	if k <= (2 * L):
# 		# Represent k as sum of distinct integers, each greater than L
# 		# And each subsequent greater than the previous
# 		min = L
# 		summands = one_summand_creation(n, k, min, summands)
# 	else:
# 		summands.append(L)
# 		summands = optimal_summands_helper(n, k-1, L+1, summands)
# 		print(summands)
#
# 	return summands
#
# def one_summand_creation(n, k, min, summands):
# 	_sum = 0
# 	for i in range(0, len(summands)):
# 		_sum += summands[i]
# 	need = n - _sum
# 	if (need <= summands[len(summands)-1]):
# 		summands[len(summands)-1] += need
# 	else:
# 		summands.append(need)
# 	return summands

def optimal_summands(n):
	summands = []
	_sum = 0
	L = 0

	while (_sum < n):
		L = L+1
		if (_sum + (L)) > n:
			edit = n - _sum
			summands[len(summands)-1] += edit
			_sum += edit
		else:
			summands.append(L)
			_sum += L

	return summands


if __name__ == '__main__':
	input = sys.stdin.read()
	n = int(input)
	# n = coursint(input())
	summands = optimal_summands(n)
	print(len(summands))
	for x in summands:
		print(x, end=' ')
