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
	N, D, C, M = map(int, input().split())
	S = input()
	ans = N, D, C, M, S
	state = 0
	ans = 'YES'
	for i in S:
		if state == 0:
			if i == 'C':
				if not C:
					state = 1
				else:
					C -= 1
			elif i == 'D':
				if not D:
					state = 1
				else:
					D -= 1
					C += M
		if state == 1:
			if i == 'D':
				ans = 'NO'
	print('Case #%d:' % (test + 1), ans)

