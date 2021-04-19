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

import math, sys
from collections import defaultdict

sys.setrecursionlimit(100000000)

def gcd(nums):
	if len(nums) == 0:
		return 0
	if len(nums) == 1:
		return nums[0]
	else:
		ans = nums[0]
		for i in nums[1:]:
			ans = math.gcd(ans, i)
		return ans

T = int(input())
for test in range(T):
	N, Q = list(map(int, input().split()))
	X, Y, L, A = [], [], [], []
	for i in range(N - 1):
		x, y, l, a = list(map(int, input().split()))
		X.append(x - 1)
		Y.append(y - 1)
		L.append(l)
		A.append(a)
	QC = []
	QW = []
	for i in range(Q):
		c, w = list(map(int, input().split()))
		QC.append(c - 1)
		QW.append(w)
	# Build graph, adj list
	al = defaultdict(dict)
	for x, y, l, a in zip(X, Y, L, A):
		assert y not in al[x]
		assert x not in al[y]
		al[x][y] = (l, a)
		al[y][x] = (l, a)
	# Dfs
	fringe = []
	visited = [False] * N
	prev = [None] * N
#	def dfs_old(s):
#		visited[s] = True
#		for t, (l, a) in al[s].items():
#			if visited[t]:
#				continue
#			prev[t] = (s, l, a)
#			dfs(t)
	def dfs(s):
		fringe.append(s)
		while fringe:
			s = fringe.pop()
			visited[s] = True
			for t, (l, a) in al[s].items():
				if visited[t]:
					continue
				prev[t] = (s, l, a)
				fringe.append(t)
	dfs(0)
	ans = []
	for c, w in zip(QC, QW):
		tolls = []
		while c:
			s, l, a = prev[c]
			if w >= l:
				tolls.append(a)
			c = s
		ans.append(gcd(tolls))
	print('Case #%d:' % (test + 1), ' '.join(map(str, ans)))

