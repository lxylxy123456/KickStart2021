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
	N = int(input())
	S = input()
	assert len(S) == N
	ans = S
	found = True
	while found:
		l = len(S)
		for i in range(10):
			j = (i + 1) % 10
			k = (j + 1) % 10
			S = S.replace(str(i) + str(j), str(k))
		found = len(S) != l
	ans = S
	print('Case #%d:' % (test + 1), ans)

