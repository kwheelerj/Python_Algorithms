#Uses python3
__author__ = 'kwheelerj'

import sys

def lcs3(a, b, c):
	m = len(a)
	n = len(b)
	o = len(c)
	distances = [[[0 for k in range(o+1)] for j in range(n+1)] for i in range(m+1)]

	for i in range(1, m+1):
		distances[i][0][0] = 0
	for j in range(0, n+1):
		distances[0][j][0] = 0
	for k in range(0, o+1):
		distances[0][0][k] = 0

	for i in range(1, m+1):
		for j in range(1, n+1):
			for k in range(1, o+1):
				if (a[i] == b[j]) and (b[j] == c[k]):
					distances[i][j][k] = distances[i-1][j-1][k-1] + 1
				elif distances[i-1][j][k] >= distances[i][j-1][k]:
					distances[i][j][k] = distances[i-1][j][k-1] + 1
				else:
					distances[i][j][k] = distances[i][j-1][k-1]


	# return min(len(a), len(b), len(c))
	return distances[m][n][o]

if __name__ == '__main__':
	# input = sys.stdin.read()
	input = input()
	data = list(map(int, input.split()))
	an = data[0]
	data = data[1:]
	a = data[:an]
	data = data[an:]
	bn = data[0]
	data = data[1:]
	b = data[:bn]
	data = data[bn:]
	cn = data[0]
	data = data[1:]
	c = data[:cn]
	print(lcs3(a, b, c))
