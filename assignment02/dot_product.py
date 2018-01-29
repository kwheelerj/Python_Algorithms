#Uses python3
__author__ = 'kwheelerj'

import sys


def max_dot_product(a, b):
	res = 0
	for i in range(len(a)):
		_a = max(a);
		_b = max(b);
		res += (_a * _b)
		a.remove(_a)
		b.remove(_b)
	return res


if __name__ == '__main__':
	input = sys.stdin.read()
	# input = input()
	data = list(map(int, input.split()))
	n = data[0]
	a = data[1:(n + 1)]
	b = data[(n + 1):]
	print(max_dot_product(a, b))
