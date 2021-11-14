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
sys.setrecursionlimit(100000000)
# from collections import defaultdict
# A = list(map(int, input().split()))

from fractions import Fraction
MOD = 10**9 + 7

def invmod(x):
	return pow(x, MOD - 2, MOD)

T = int(input())
for test in range(T):
	N, Q = map(int, input().split())
	K = Fraction(int(input()), 1000000)
	P, A, B = [None], [None], [None]
	U, V = [], []
	adj_list = [[]]
	for i in range(N - 1):
		p, a, b = map(int, input().split())
		P.append(p - 1)
		A.append(Fraction(a, 1000000))
		B.append(Fraction(b, 1000000))
		adj_list.append([])
	for i in range(Q):
		u, v = map(int, input().split())
		U.append(u - 1)
		V.append(v - 1)
	for index, i in enumerate(P):
		if i is not None:
			adj_list[i].append(index)
	# Simulate DFS 1
	prob0 = [None] * N	# P(E[i] | !E[0])
	prob1 = [None] * N	# P(E[i] | E[0])
	prob0[0] = 0
	prob1[0] = 1
	parents = [None] * N
	print('.')
	def dfs(n, st, p0, p1, pr):
		st.append(n)
		if pr is not None:
			pr[n] = list(st)
		print(end='<', flush=True)
		for i in adj_list[n]:
			p0[i] = (p0[n] * A[i] + (1 - p0[n]) * B[i]) % MOD
			p1[i] = (p1[n] * A[i] + (1 - p1[n]) * B[i]) % MOD
			dfs(i, st, p0, p1, pr)
		print(end='>', flush=True)
		assert st.pop() == n
	print('.')
	dfs(0, [], prob0, prob1, parents)
	print('.')
	# Index queries
	ans = []
	for u, v in zip(U, V):
		r = None
		for i, j in zip(parents[u], parents[v]):
			if i == j:
				r = i
		pr0 = [None] * N
		pr1 = [None] * N
		pr0[r] = 0
		pr1[r] = 1
		dfs(r, [], pr0, pr1, None)
		assert pr0[u] is not None
		assert pr0[v] is not None
		assert pr1[u] is not None
		assert pr1[v] is not None
		a0 = (K * prob1[r] + (1 - K) * prob0[r]) % MOD * (pr1[u] * pr1[v]) % MOD
		a1 = ((K * (1 - prob1[r]) + (1 - K) * (1 - prob0[r])) % MOD *
				(pr0[u] * pr0[v]) % MOD)
		a = a0 % MOD + a1 % MOD
		# import libnum
		# assert invmod(a.denominator) == libnum.invmod(a.denominator, MOD)
		ans.append((invmod(a.denominator) * a.numerator) % MOD)
	print('Case #%d:' % (test + 1), *ans)

