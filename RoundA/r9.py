import sys
stdin = sys.stdin
stdin = open('r.txt')
input = lambda: stdin.readline()[:-1]


T = int(input())
for index in range(T):
	R, C = map(int, input().split())
	# m is the original data
	m = []
	for i in range(R):
		m.append(list(map(int, input().split())))
	ans = 0
	# n is the final data
	n = list(map(list, m))
	for i in range(R):
		req = -1
		for j in range(C):
			n[i][j] = max(n[i][j], req)
			req = n[i][j] - 1
	for i in range(R):
		req = -1
		for j in reversed(range(C)):
			n[i][j] = max(n[i][j], req)
			req = n[i][j] - 1
	for j in range(C):
		req = -1
		for i in range(R):
			n[i][j] = max(n[i][j], req)
			req = n[i][j] - 1
	for j in range(C):
		req = -1
		for i in reversed(range(R)):
			n[i][j] = max(n[i][j], req)
			req = n[i][j] - 1
	ans = sum(map(sum, n)) - sum(map(sum, m))
	print('Case #%d:' % (index + 1), ans)

