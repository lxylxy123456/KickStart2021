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
from collections import Counter
# A = list(map(int, input().split()))

def factor(a):
	ans = Counter()
	while a % 2 == 0:
		ans[2] += 1
		a //= 2
	for i in range(3, a + 3):
		if a == 1:
			break
		if i**2 > a:
			ans[a] += 1
			break
		while a % i == 0:
			ans[i] += 1
			a //= i
	return sorted(ans.items())

def factors(factored, start=0):
	if not factored[start:]:
		yield 1
	else:
		a = 1
		for i in range(factored[start][1] + 1):
			for j in factors(factored, start + 1):
				yield a * j
			a *= factored[start][0]

T = int(input())
for test in range(T):
	G = int(input())
	# Find x s.t. exists i >= 0, x + (x+1) ... + (x+i) = G
	# (2*x + i) * (i + 1) = G * 2
	ans = 0
	for i_plus_1 in factors(factor(G * 2)):
		i = i_plus_1 - 1
		two_x = G * 2 // i_plus_1 - i
		if two_x % 2 == 0 and two_x >= 1:
			x = two_x // 2
			# print(x)
			ans += 1
	print('Case #%d:' % (test + 1), ans)

# 16 min, AC AC (1 attempts total)

