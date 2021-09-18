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

import math
# sys.setrecursionlimit(100000000)
# from collections import defaultdict
# A = list(map(int, input().split()))

T = int(input())
for test in range(T):
	N = int(input())
	XY = []
	for i in range(N):
		XY.append(list(map(int, input().split())))
	Xs, Ys = map(int, input().split())
	# print(XY, Xs, Ys)
	turn = []
	dist = []
	for i in range(N):
		turn.append([None] * N)
		dist.append([None] * N)
	for index, (xi, yi) in enumerate(XY):
		for jndex, (xj, yj) in enumerate(XY[:index]):
			a, b = xi - xj, yi - yj
			c, d = xi - Xs, yi - Ys
			cross = a * d - c * b
			turn[index][jndex] = cross
			turn[jndex][index] = -cross
			dis = math.sqrt((xi - xj)**2 + (yi - yj)**2)
			dist[index][jndex] = dis
			dist[jndex][index] = dis
		turn[index][index] = 0
	ans = 10000000000
	# print(*turn , sep='\n')
	# print(dist)
	for i in range(N):
		for j in range(i):
			if turn[i][j] == 0 and ((XY[i] < [Xs, Ys] and XY[j] > [Xs, Ys]) or
									(XY[i] > [Xs, Ys] and XY[j] < [Xs, Ys])):
				# Handle the case of same line
				ansp = 10000000000
				ansn = 10000000000
				for k in range(N):
					if turn[i][k] > 0:
						ansp = min(ansp, dist[i][k] + dist[j][k])
					elif turn[i][k] < 0:
						ansn = min(ansn, dist[i][k] + dist[j][k])
				ans = min(ans, ansp + ansn)
			else:
				# Triangle case
				for k in range(j):
					t1, t2, t3 = turn[i][j], turn[j][k], turn[k][i]
					if ((t1 > 0 and t2 > 0 and t3 > 0) or
						(t1 < 0 and t2 < 0 and t3 < 0)):
						ans = min(ans, dist[i][j] + dist[j][k] + dist[k][i])
	if ans == 10000000000:
		ans = 'IMPOSSIBLE'
	print('Case #%d:' % (test + 1), ans)

