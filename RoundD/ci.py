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
	N, C = map(int, input().split())
	L, R = [], []
	for i in range(N):
		l, r = map(int, input().split())
		L.append(l + 1)
		R.append(r)
	# Pairing between L and R is useless
	L.sort()
	R.sort()
	# since [i][0] (inclusive), the number of intervals is [i][1]
	li, ri = 0, 0
	range_info = [(0, 0)]
	cur = 0
	while li < N or ri < N:
		smallest = 10**20
		if li < N:
			smallest = min(smallest, L[li])
		if ri < N:
			smallest = min(smallest, R[ri])
		while li < N and L[li] == smallest:
			li += 1
			cur += 1
		while ri < N and R[ri] == smallest:
			ri += 1
			cur -= 1
		range_info.append((smallest, cur))
		# print(range_info[-1])
	range_info.pop(0)
	ranges = []	# [[1], [2]), number of intervals is [0]
	for (i, j), (k, _) in zip(range_info[0:], range_info[1:]):
		ranges.append((j, i, k))
	ranges.sort()
	# print(ranges)
	c = C
	ans = N
	while c and ranges:
		i, j, k = ranges.pop()
		ans += min(k - j, c) * i
		c -= min(k - j, c)
	print('Case #%d:' % (test + 1), ans)

