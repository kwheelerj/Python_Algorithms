# Uses python3
__author__ = 'kwheelerj'


def edit_distance(s, t):
	# print(len(t))
	distances = [[0 for x in range(len(t)+1)] for y in range(len(s)+1)]
	for i in range(0, len(t)+1):
		distances[0][i] = i
	for j in range(0, len(s)+1):
		distances[j][0] = j

	# print(distances)

	for i in range(1, len(t)+1):
		for j in range(1, len(s) + 1):
			# print("if t[{0}] == s[{1}]:".format(i-1, j-1))
			# print(t[i-1] == s[j-1])
			if t[i-1] == s[j-1]:
				distances[j][i] = min(distances[j][i-1]+1, distances[j-1][i]+1, distances[j-1][i-1])
			else:
				distances[j][i] = min(distances[j][i-1]+1, distances[j-1][i]+1, distances[j-1][i-1]+1)

	# print(distances)
	return distances[len(s)][len(t)]


if __name__ == "__main__":
	# print(edit_distance("editing", "distance"))
	print(edit_distance(input(), input()))
