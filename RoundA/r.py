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
	for xi in range(R):
		for yi in range(C):
			for xj in range(R):
				for yj in range(C):
					bound = n[xj][yj] - abs(xi - xj) - abs(yi - yj)
					n[xi][yi] = max(n[xi][yi], bound)
	ans = sum(map(sum, n)) - sum(map(sum, m))
	print('Case #%d:' % (index + 1), ans)

