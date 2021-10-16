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
	N, A = map(int, input().split())
	if N == 3:
		print('Case #%d:' % (test + 1), 'POSSIBLE')
		print(0, 0)
		print(0, 1)
		print(A, 0)
	elif N == 4:
		if A == 1:
			print('Case #%d:' % (test + 1), 'IMPOSSIBLE')
		else:
			print('Case #%d:' % (test + 1), 'POSSIBLE')
			print(0, 0)
			print(1, 0)
			print(1, A - 1)
			print(0, 1)
	elif N == 5:
		if A <= 2:
			print('Case #%d:' % (test + 1), 'IMPOSSIBLE')
		else:
			print('Case #%d:' % (test + 1), 'POSSIBLE')
			print(0, 0)
			print(1, 0)
			print(1, 1)
			print(2, A - 1)
			print(0, 1)
	else:
		if A <= N - 3:
			print('Case #%d:' % (test + 1), 'IMPOSSIBLE')
		else:
			print('Case #%d:' % (test + 1), 'POSSIBLE')
			l = []
			r = []
			def gen(s):
				i = s
				while True:
					r.append((i, 1))
					yield
					l.append((i, 0))
					yield
					i += 1
					l.append((i, 1))
					yield
					r.append((i, 2))
					yield
					i += 1
			g = gen(A - N + 3)
			for _ in range(N - 1):
				next(g)
			print(0, 12)
			for i in l:
				print(*i)
			for i in reversed(r):
				print(*i)

