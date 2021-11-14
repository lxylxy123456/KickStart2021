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

def dist(a, b):
	d = abs(ord(a) - ord(b))
	return min(26 - d, d)

T = int(input())
for test in range(T):
	S = input()
	F = input()
	ans = S, F
	import functools
	@functools.lru_cache(100)
	def dist_f(a):
		ans = 27
		for i in F:
			ans = min(ans, dist(a, i))
		return ans
	ans = 0
	for i in S:
		ans += dist_f(i)
	print('Case #%d:' % (test + 1), ans)

