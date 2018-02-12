# Uses python3
__author__ = 'kwheelerj'
import sys


def optimal_sequence(n):
	sequence = []
	while n >= 1:
		sequence.append(n)
		if n % 3 == 0:
			n = n // 3
		elif n % 2 == 0:
			n = n // 2
		else:
			n = n - 1
	return reversed(sequence)


def optimal_sequence_correct(n):
	number_of_moves_for = [0]

	for i in range(1, n):
		number_of_moves_for.append(99999999)

		if (i+1) % 3 == 0:
			# print("({}) % 3 == 0".format(i+1))
			index = (i+1) // 3
			val = number_of_moves_for[index-1] + 1
			if val < number_of_moves_for[i]:
				number_of_moves_for[i] = val

		if (i+1) % 2 == 0:
			# print("({}) % 2 == 0".format(i+1))
			index = (i+1) // 2
			val = number_of_moves_for[index-1] + 1
			# print(val)
			if val < number_of_moves_for[i]:
				number_of_moves_for[i] = val

		# print("{} - 1 = ".format(i+1, i))
		val = number_of_moves_for[i-1] + 1
		# print(val)
		if val < number_of_moves_for[i]:
			number_of_moves_for[i] = val


	sequence = []
	while n >= 1:
		sequence.append(n)
		moves = [99999999, 9999999, 9999999]
		# moves = [val//3, val//2, val-1]
		if n % 3 == 0:
			moves[0] = number_of_moves_for[(n // 3) - 1]
		if n % 2 == 0:
			moves[1] = number_of_moves_for[(n // 2) - 1]
		moves[2] = number_of_moves_for[n - 2]

		# print(moves)
		# print(min(moves))
		min_moves = moves.index(min(moves))
		if min_moves == 0:
			n = n // 3
		elif min_moves == 1:
			n = n // 2
		else:
			n = n-1

	return reversed(sequence)



# input = sys.stdin.read()
input = input()
n = int(input)
# sequence = list(optimal_sequence(n))
sequence = list(optimal_sequence_correct(n))
print(len(sequence) - 1)
for x in sequence:
	print(x, end=' ')
