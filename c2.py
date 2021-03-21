try:
	import sys
	stdin = sys.stdin
	stdin = open('c.txt')
	input = lambda: stdin.readline()[:-1]
except Exception:
	pass


from collections import defaultdict, Counter
import functools

T = int(input())
for index in range(T):
	C = R = int(input())
	# m is the original data
	A = []
	for i in range(R):
		A.append(list(map(int, input().split())))
	B = []
	for i in range(R):
		B.append(list(map(int, input().split())))
	# Ignore checksum data
	input()
	input()
	# row_to_vir_col
	# TODO: use defaultdict if TLE, or use C++ priority queue etc.
	virs = {}
	for i in range(R):
		for j in range(C):
			if A[i][j] == -1:
				virs[(i, j)] = B[i][j]
	# @functools.lru_cache(10000000)
	def solve(virs, level=0):
		while True:
			c_count = Counter()
			v_count = Counter()
			for x, y in virs:
				c_count[x] += 1
				v_count[y] += 1
			virs_new = {}
			for (x, y), p in virs.items():
				if c_count[x] > 1 and v_count[y] > 1:
					virs_new[x, y] = p
			if len(virs) == len(virs_new):
				virs = virs_new
				break
			else:
				virs = virs_new
		if not virs:
			return 0
		best = 10000000000000
		virs_next = virs.copy()
		for (x, y), p in virs.items():
			del virs_next[x, y]
			best = min(best, solve(virs_next, level + 1) + p)
			virs_next[x, y] = p
		return best

	ans = solve(virs)
	print('Case #%d:' % (index + 1), ans)

