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

MOD = 10**9 + 7

def powm(a, b):
	ans = 1
	while b:
		if b % 2 == 1:
			ans *= a
			ans %= MOD
		b //= 2
		a *= a
	return ans

T = int(input())
for test in range(T):
	N, K = list(map(int, input().split()))
	S = input()
	ans = 0
	M = N // 2
	if len(S) % 2 == 1:
		S = S[0: M + 1] + S[-M - 1: ]
		M += 1
	ans = 0
	for i in range(M + 1):
		# Suppose T[0: i] = S[0: i] and T[i] != S[i]
		if i == M:
			if ''.join(reversed(S[:M])) < S[-M:]:
				ans += 1
				# print(i, 1)
		else:
			ans += (ord(S[i]) - ord('a')) * powm(K, (M - i - 1))
			ans %= MOD
	ans %= MOD
	print('Case #%d:' % (test + 1), ans)

