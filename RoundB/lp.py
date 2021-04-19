try:
	import os, sys
	stdin = sys.stdin
	if len(sys.argv) > 1:
		stdin = open(sys.argv[1])
	else:
		# stdin = open('s.txt')
		stdin = open(os.path.splitext(__file__)[0] + '.txt')
	input = lambda: stdin.readline()[:-1]
except Exception:
	pass


T = int(input())
for test in range(T):
	N = int(input())
	# Need to find an arithmetic array in A, can change 1 number
	A = list(map(int, input().split()))
	# Need to find a constant array in d, can add sth to [i] and remove the
	# same amount to [i + 1]
#	d = []
#	for i, j in zip(A, A[1:]):
#		d.append(i - j)
	# The following are at the end of loop
#	change_pp = 0		# Best result by changing something earlier than prev
#	change_prev = 0		# Best result by changing prev
#	change_none = 0		# Best result by changing nothing
#	pp_slope = 0
#	prev_slope = 0
#	none_slope = 0
#	for index, i in enumerate(A):
#		candidates = []
#		# continue change_pp of prev
#		if index >= 1 and A[index - 1] + pp_slope == i:
#			candidates.append([change_pp + 1, pp_slope])
#		# continue change_prev of prev
#		if index >= 1 and A[index - 1] + prev_slope == i:
#			candidates.append([change_prev + 1, prev_slope])
#		# change prev
#		if index >= 2 and (i - A[index - 2]) % 2 == 0:
#			slope = (i - A[index - 2]) // 2
#			if none_slope == slope:
#		# don't change
#		if A[index - 1] > 0
	N = len(A)
	S = [0] * N		# Length of arithmetic array starting here
	E = [0] * N		# Length of arithmeric array ending here
	cur = 0
	for index, i in enumerate(A):
		if index <= 1 or A[index - 1] - A[index - 2] == i - A[index - 1]:
			cur += 1
		else:
			cur = 2
		E[index] = cur
	cur = 0
	for count, (index, i) in enumerate(reversed(list(enumerate(A)))):
		if count <= 1 or A[index + 1] - A[index + 2] == i - A[index + 1]:
			cur += 1
		else:
			cur = 2
		S[index] = cur
	ans = max(E)
#	print(S)
#	print(E)
	for index, i in enumerate(A):
		# Consider changing i
		prev_best = 0
		prev_slope = 0
		if index > 0:
			prev_best = E[index - 1]
			if index > 1:
				prev_slope = A[index - 1] - A[index - 2]
		next_best = 0
		next_slope = 0
		if index < N - 1:
			next_best = S[index + 1]
			if index < N - 2:
				next_slope = A[index + 2] - A[index + 1]
		# print(index, i, prev_best, next_best, prev_slope, next_slope, ans, sep='\t')
		if ((prev_slope == next_slope) and (index > 0 and index < N - 1) and
			(A[index - 1] + prev_slope * 2 == A[index + 1])):
			ans = max(ans, prev_best + next_best + 1)
		else:
			ans = max(ans, next_best + 1)
			ans = max(ans, prev_best + 1)
			if index > 0 and index < N - 1:
				if A[index - 1] == A[index + 1] - 2 * next_slope:
					ans = max(ans, next_best + 2)
				if A[index - 1] + 2 * prev_slope == A[index + 1]:
					ans = max(ans, prev_best + 2)
	print('Case #%d:' % (test + 1), ans)

