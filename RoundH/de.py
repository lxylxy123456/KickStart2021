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

def rev_solve(pb0, pb1, pc0, pc1):
	'''
	solve([
		pb0 * pb0c0 + pb1 * pb1c0 = pc0,
		pb0 * pb0c1 + pb1 * pb1c1 = pc1,
		pb0c0 + pb0c1 = 1,
		pb1c0 + pb1c1 = 1
		], [pb0c0, pb0c1, pb1c0, pb1c1]);

	solve([
		a * x + b * z = c,
		a * y + e * w = d,
		x + y = 1,
		z + w = 1
		], [x, z, y, x]);
	'''
	# Give up: impossible to solve

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
	prob0[0] = 1 - K
	prob1[0] = K
	t = 0
	enter = [None] * N
	leave = [None] * N
	def dfs(n):
		global t
		enter[n] = t
		t += 1
		for i in adj_list[n]:
			prob0[i] = prob0[n] * A[i] + (1 - prob0[n]) * B[i]
			prob1[i] = prob1[n] * A[i] + (1 - prob1[n]) * B[i]
			dfs(i)
		leave[n] = t
		t += 1
	dfs(0)
	# Index queries
	ans = []
	for index, (u, v) in enumerate(zip(U, V)):
		for jndex, (e, l) in enumerate(zip(enter, leave)):
			r = 0
			if (e <= enter[u] and e <= enter[v] and
				leave[u] <= l and leave[v] <= l):
				if enter[r] <= e:
					r = jndex
		print(r, u, v)
	ans = P
	print('Case #%d:' % (test + 1), ans)

