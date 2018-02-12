# Uses python3
__author__ = 'kwheelerj'
import sys


def optimal_weight(W, w):
	# write your code here
	result = 0
	for x in w:
		if result + x <= W:
			result = result + x
	return result


def optimal_weight_correct(W, _w):
	# values = [[0 for y in range((W) + 1)] for x in range(len(_w) + 1)]
	values = [[0 for x in range(len(_w) + 1)] for y in range((W) + 1)]
	# print(values)
	# print(len(_w))
	for i in range(1, len(_w) + 1):
		for w in range(1, W+1):
			# print("values[{0}][{1}] = values[{0}][{2}]".format(w, i, i-1))
			values[w][i] = values[w][i-1]
			# print("if _w[{}] < {}:".format(i-1, w))
			if _w[i-1] <= w:
				val = values[w-_w[i-1]][i-1] + _w[i-1]
				if values[w][i] < val:
					values[w][i] = val
	# print(values)
	return values[W][len(_w)]


if __name__ == '__main__':
	input = sys.stdin.read()
	# input = input()
	W, n, *w = list(map(int, input.split()))
	# print(optimal_weight(W, w))
	print(optimal_weight_correct(W, w))
