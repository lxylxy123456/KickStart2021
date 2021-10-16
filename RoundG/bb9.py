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

import heapq
# import math, sys
# sys.setrecursionlimit(100000000)
from collections import defaultdict
# A = list(map(int, input().split()))

T = int(input())
for test in range(T):
	N, K = map(int, input().split())
	B = list(map(int, input().split()))
	s = [0]	# [i] = sum of B[:i]
	ans = N + 10
	for i in B:
		s.append(s[-1] + i)
		if i == K:
			ans = 1
	best = [N + 10] * K
	best[0] = 0
	for i in range(N):	# left boundary of second range
		# Update left
		for j in range(i):
			k = s[i] - s[j]
			if k in range(K):
				best[k] = min(best[k], i - j)
		# Match with right
		for j in range(i + 1, N + 1):
			k = K - (s[j] - s[i])
			if k in range(K):
				ans = min(ans, best[k] + j - i)
	if ans > N:
		ans = -1
	print('Case #%d:' % (test + 1), ans)

