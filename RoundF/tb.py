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

T = int(input())
for test in range(T):
	N = int(input())
	S = list(map(int, input()))
	l = []
	r = []
	cur = N
	for i in range(N):
		if S[i]:
			cur = i
		l.append(cur)
	cur = -1
	for i in range(N - 1, -1, -1):
		if S[i]:
			cur = i
		r.append(cur)
	r = list(reversed(r))
	ans = 0
	if 0:
		print(l)
		print(r)
	for index, (i, j) in enumerate(zip(l, r)):
		ans += min(abs(i - index), abs(j - index))
	if 0:
		ans2 = 0
		for i in range(N):
			j = 0
			while True:
				if ((i + j in range(N) and S[i + j]) or
					(i - j in range(N) and S[i - j])):
					break
				j += 1
				# print(i, j)
			ans2 += j
		assert ans == ans2
	print('Case #%d:' % (test + 1), ans)

