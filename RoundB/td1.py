import math
# from collections import defaultdict
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
	# al = defaultdict(dict)
	al = {}
	for x, y, l, a in zip(X, Y, L, A):
		if x not in al:
			al[x] = {}
		if y not in al:
			al[y] = {}
		assert y not in al[x]
		assert x not in al[y]
		al[x][y] = (l, a)
		al[y][x] = (l, a)
	# Dfs
	visited = [False] * N
	prev = [None] * N
	def dfs(s):
		visited[s] = True
		for t, (l, a) in al[s].items():
			if visited[t]:
				continue
			assert prev[t] is None
			prev[t] = (s, l, a)
			dfs(t)
	dfs(0)
	assert all(visited)
	ans = []
	for c, w in zip(QC, QW):
		tolls = []
		while c:
			s, l, a = prev[c]
			if w >= l:
				tolls.append(a)
			c = s
		ans.append(math.gcd(*tolls))
	print('Case #%d:' % (test + 1), ' '.join(map(str, ans)))

