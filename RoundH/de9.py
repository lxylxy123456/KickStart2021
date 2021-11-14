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

MOD = 10**9 + 7

def invmod(x):
	return pow(x, MOD - 2, MOD)

T = int(input())
for test in range(T):
	N, Q = map(int, input().split())
	inv10e6 = invmod(1000000)
	K = int(input()) * inv10e6
	P, A, B = [None], [None], [None]
	U, V = [], []
	adj_list = [[]]
	for i in range(N - 1):
		p, a, b = map(int, input().split())
		P.append(p - 1)
		A.append(a * inv10e6)
		B.append(b * inv10e6)
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
	depth = [None] * N
	def dfs(n, st, p0, p1, d=0):
		st.append(n)
		depth[n] = d
		for i in adj_list[n]:
			p0[i] = (p0[n] * A[i] + (1 - p0[n]) * B[i]) % MOD
			p1[i] = (p1[n] * A[i] + (1 - p1[n]) * B[i]) % MOD
			dfs(i, st, p0, p1, d + 1)
		assert st.pop() == n
	dfs(0, [], prob0, prob1)
	# Index queries
	ans = []
	for u, v in zip(U, V):
		r = None
		ur = u
		vr = v
		while depth[ur] > depth[vr]:
			ur = P[ur]
		while depth[ur] < depth[vr]:
			vr = P[vr]
		while ur != vr:
			ur = P[ur]
			vr = P[vr]
		r = ur
		def rel_prob(a, d):
			# Return: (P(d | !a), P(d | a))
			if a == d:
				return (0, 1)
			p = P[d]
			pa0p, pa1p = rel_prob(a, p)
			pa0d = pa0p * A[d] + (1 - pa0p) * B[d]
			pa1d = pa1p * A[d] + (1 - pa1p) * B[d]
			return pa0d, pa1d
		pr0u, pr1u = rel_prob(r, u)
		pr0v, pr1v = rel_prob(r, v)
		a0 = (K * prob1[r] + (1 - K) * prob0[r]) % MOD * (pr1u * pr1v) % MOD
		a1 = ((K * (1 - prob1[r]) + (1 - K) * (1 - prob0[r])) % MOD *
				(pr0u * pr0v) % MOD)
		a = a0 % MOD + a1 % MOD
		# import libnum
		# assert invmod(a.denominator) == libnum.invmod(a.denominator, MOD)
		ans.append((invmod(a.denominator) * a.numerator) % MOD)
	print('Case #%d:' % (test + 1), *ans)

