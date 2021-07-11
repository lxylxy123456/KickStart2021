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

# import math, sys
# sys.setrecursionlimit(100000000)
# from collections import defaultdict
# A = list(map(int, input().split()))
import bisect

T = int(input())
for test in range(T):
	N, M = map(int, input().split())
	AB = []
	for i in range(N):
		AB.append(list(map(int, input().split())))
	S = list(map(int, input().split()))
	AB.sort()
	A = []
	B = []
	for a, b in AB:
		A.append(a)
		B.append(b)
	ans = []
	for s in S:
		i = bisect.bisect(A, s)
		j = bisect.bisect_left(B, s)
		# print(s, i, j, A, B)
		if i == 0:
			ans.append(A[0])
			A[0] += 1
			if A[0] > B[0]:
				A.pop(0)
				B.pop(0)
			continue
		if j == len(A):
			ans.append(B[-1])
			B[-1] -= 1
			if A[-1] > B[-1]:
				A.pop()
				B.pop()
			continue
		if i - 1 == j:
			ans.append(s)
			if A[j] == s:
				A[j] += 1
				if A[j] > B[j]:
					A.pop(j)
					B.pop(j)
			elif B[j] == s:
				B[j] -= 1
				if A[j] > B[j]:
					A.pop(j)
					B.pop(j)
			else:
				b = B[j]
				B[j] = s - 1
				A.insert(j, s + 1)
				B.insert(j, b)
			continue
		if 1:
			assert i == j
			db = s - B[j - 1]
			da = A[i] - s
			# print(db, da)
			if db <= da:
				# Use B[j - 1]
				ans.append(B[j - 1])
				B[j - 1] -= 1
				if A[j - 1] > B[j - 1]:
					A.pop(j - 1)
					B.pop(j - 1)
			else:
				# Use A[i]
				ans.append(A[i])
				A[i] += 1
				if A[i] > B[i]:
					A.pop(i)
					B.pop(i)
	print('Case #%d:' % (test + 1), *ans)

