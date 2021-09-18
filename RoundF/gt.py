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
from functools import lru_cache
# sys.setrecursionlimit(100000000)
# from collections import defaultdict
# A = list(map(int, input().split()))

T = int(input())
for test in range(T):
	N, M, K = map(int, input().split())
	X, Y = [], []
	L, R, A = [], [], []
	adj_list = []
	for i in range(N):
		adj_list.append([])
	adj_mask = [0] * N
	for i in range(N):
		l, r, a = map(int, input().split())
		L.append(l)
		R.append(r)
		A.append(a)
	for i in range(M):
		x, y = map(int, input().split())
		X.append(x)
		Y.append(y)
		adj_list[x].append(y)
		adj_list[y].append(x)
		adj_mask[x] |= 1 << y
		adj_mask[y] |= 1 << x
	# ans = N, M, K, X, Y, L, R, A
	ans = 0
	if sum(A) >= K:
		@lru_cache(1048576)
		def recu(pts, visited, can_visit):
			if pts == K:
				return 1
			if pts > K:
				return 0
			ans = 0
			for i in range(N):
				si = 1 << i
				if (can_visit & si) and L[i] <= pts and pts <= R[i]:
					v = visited | si
					cv = (can_visit | adj_mask[i]) & (~v)
					ans += recu(pts + A[i], v, cv)
			return ans
		for i in range(N):
			ans += recu(A[i], 1 << i, adj_mask[i])
	print('Case #%d:' % (test + 1), ans)

