# Uses python3
__author__ = 'kwheelerj'

import sys


def get_optimal_value(capacity, weights, values):
	value = 0.
	# print(capacity)
	# print(values)
	# print(weights)

	weighted_values = []

	for i in range(0, len(weights)):
		weighted_values.append((values[i], weights[i], values[i] / weights[i]))
	weighted_values = sorted(weighted_values, key=lambda tup: tup[2], reverse=True)
	# print(weighted_values)

	for i in range(0, len(weighted_values)):
		if capacity == 0:
			return value
		a = min(weighted_values[i][1], capacity)
		value += a*(weighted_values[i][2])
		capacity -= a

	return value


if __name__ == "__main__":
	data = list(map(int, sys.stdin.read().split()))
	# data = list(map(int, input().split()))
	n, capacity = data[0:2]
	values = data[2:(2 * n + 2):2]
	weights = data[3:(2 * n + 2):2]
	opt_value = get_optimal_value(capacity, weights, values)
	print("{:.10f}".format(opt_value))
