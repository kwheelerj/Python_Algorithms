# Uses python3
__author__ = 'kwheelerj'

import sys


def get_change(m):
	coin_count = 0
	if m // 10 >= 1:
		# print('m // 10 = ' + str(m // 10))
		coin_count += (m // 10)
		# print('coin_count: ' + str(coin_count))
		m = m - (m//10) * 10
		# print('m = ' + str(m))
	if m // 5 >= 1:
		# print('m // 5 = ' + str(m // 5))
		coin_count += (m // 5)
		# print('coin_count: ' + str(coin_count))
		m = m - (m//5) * 5
		# print('m = ' + str(m))
	if m // 1 >= 1:
		# print('m // 1 = ' + str(m // 1))
		coin_count += (m // 1)
		# print('coin_count: ' + str(coin_count))
		m = m - (m//1) * 1
		# print('m = ' + str(m))
	return coin_count


# print(get_change(2))
# print(get_change(28))
# print(get_change(999))


if __name__ == '__main__':
	m = int(sys.stdin.read())
	# m = int(input())
	print(m)
	print(get_change(m))
