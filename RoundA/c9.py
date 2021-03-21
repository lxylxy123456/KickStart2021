try:
	import sys
	stdin = sys.stdin
	stdin = open('c.txt')
	input = lambda: stdin.readline()[:-1]
except Exception:
	pass


# 0 0 1 1
# 0 0 1 1
# 1 1 1 0 <
# 1 1 0 0
#     ^     Should not remove this

from collections import defaultdict
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
	virs = []
	for i in range(R):
		for j in range(C):
			if A[i][j] == -1:
				virs.append((B[i][j], i, j))

	disj = {}
	def find(x):
		if x in disj:
			disj[x] = find(disj[x])
			return disj[x]
		else:
			return x

	def union(x, y):
		disj[find(x)] = find(y)

	virs.sort()

	ans = 0

	for p, i, j in reversed(virs):
		if find((0, i)) == find((1, j)):
			ans += p
		else:
			union((0, i), (1, j))

	print('Case #%d:' % (index + 1), ans)

