# Uses python3
__author__ = 'kwheelerj'
import sys

def get_majority_element(a, left, right):
	if left == right:
		return -1
	if left + 1 == right:
		return a[left]

	# countArray = [0] * n
	countDict = {}
	for i in range(left, right):
		if str(a[i]) not in countDict.keys():
			countDict[str(a[i])] = 0
		countDict[str(a[i])] += 1
	# print(countDict)
	_max = 0
	key = ''
	for _key in countDict.keys():
		if countDict[_key] > _max:
			_max = countDict[_key]
			key = _key
	# print('majority must be greater than ' + str(right // 2))
	# print('max is ' + str(_max))
	if _max > right // 2:
		return countDict[key]
	return -1

if __name__ == '__main__':
	input = sys.stdin.read()
	n, *a = list(map(int, input.split()))
	# inp = input()
	# n, *a = list(map(int, inp.split()))
	if get_majority_element(a, 0, n) != -1:
		print(1)
	else:
		print(0)
