import sys
stdin = sys.stdin
stdin = open('l.txt')
input = lambda: stdin.readline()[:-1]


T = int(input())
for index in range(T):
	R, C = map(int, input().split())
	# m is the original data
	m = []
	for i in range(R):
		m.append(list(map(int, input().split())))
	# n[i][j] is number of 1 (counting self) at the direction of
	#  [up, left, down, right]
	n = []
	for i in range(R):
		n.append([])
		for j in range(C):
			n[-1].append([None] * 4)
	for j in range(C):
		# up
		cnt = 0
		for i in range(R):
			if m[i][j]:
				cnt += 1
			else:
				cnt = 0
			n[i][j][0] = cnt
		# down
		cnt = 0
		for i in reversed(range(R)):
			if m[i][j]:
				cnt += 1
			else:
				cnt = 0
			n[i][j][2] = cnt
	for i in range(R):
		# left
		cnt = 0
		for j in range(C):
			if m[i][j]:
				cnt += 1
			else:
				cnt = 0
			n[i][j][1] = cnt
		# right
		cnt = 0
		for j in reversed(range(C)):
			if m[i][j]:
				cnt += 1
			else:
				cnt = 0
			n[i][j][3] = cnt
	ans = 0
	for i in range(R):
		for j in range(C):
			u, l, d, r = n[i][j]
			for a, b in [(u, l), (u, r), (d, l), (d, r),
						(l, u), (l, d), (r, u), (r, d)]:
				# a is long edge, b is short edge
				upper = min(a // 2, b)
				ans += len(range(2, upper + 1))
#	for i in (m):
#		print(i)
#	for i in (n):
#		print(i)
	print('Case #%d:' % (index + 1), ans)

