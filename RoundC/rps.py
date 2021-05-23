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

import functools
from fractions import Fraction
# import math, sys
# sys.setrecursionlimit(100000000)
# from collections import defaultdict
# A = list(map(int, input().split()))

def fr(a, b):
	if b:
		return Fraction(a, b)
	else:
		return Fraction(1, 3)

@functools.lru_cache()
def solve(W, E):
	# dp[i][j][k] = maximum expectation when there are i r, j p, k s
	# prev[i][j][k] = how the maximum is reached
	dp = []
	prev = []
	for i in range(61):
		dp.append([])
		prev.append([])
		for j in range(61):
			dp[-1].append([None] * 61)
			prev[-1].append([None] * 61)
	dp[0][0][0] = 0
	final_candidates = []
	for i in range(61):
		for j in range(61):
			if i + j > 60:
				continue
			for k in range(61):
				s = i + j + k
				if s > 60 or s == 0:
					continue
				candidates = []
				if i:	# me = rock, E = rock (prev = sci), W = sci (prev = pap)
					candidates.append((
						dp[i-1][j][k] + E * fr(k, s - 1) + W * fr(j, s - 1),
						'r'))
				if j:	# me = pap, E = pap (prev = rock), W = rock (prev = sci)
					candidates.append((
						dp[i][j-1][k] + E * fr(i, s - 1) + W * fr(k, s - 1),
						'p'))
				if k:	# me = sci, E = sci (prev = pap), W = pap (prev = rock)
					candidates.append((
						dp[i][j][k-1] + E * fr(j, s - 1) + W * fr(i, s - 1),
						's'))
				assert candidates
				candidates.sort()
				score, choice = candidates[-1]
				dp[i][j][k] = score
				prev[i][j][k] = choice
				if s == 60:
					final_candidates.append((dp[i][j][k], (i, j, k)))
	final_candidates.sort()
	assert final_candidates
	ans_rev = []
	i, j, k = final_candidates[-1][1]
	for _ in range(60):
		p = prev[i][j][k]
		ans_rev.append(p)
		if p == 'r':
			i -= 1
		elif p == 'p':
			j -= 1
		elif p == 's':
			k -= 1
		else:
			raise ValueError
	assert not i and not j and not k
	return ''.join(reversed(ans_rev)).upper()

def solve_db(W, E):
	return {
		(1, 0): 'SPPPPPPPPPRRRRRRRRRRRRRRRRRRRRRRRRRRRSSSSSSSSSSSSSSSSSSSSSSS',
		(10, 1): 'RSSSSPPPPPPPPPPPPPPPRRRRRRRRRRRRRRRRRRRRRRRRRSSSSSSSSSSSSSSS',
		(2, 1): 'SPPRRRRSSSSSSSSPPPPPPPPPPPPPPPPRRRRRRRRRRRRRRRRRRRSSSSSSSSSS',
		(1, 1): 'PRSPRSPRSPRSPRSPRSPRSPRSPRSPRSPRSPRSPRSPRSPRSPRSPRSPRSPRSPRS',
	}[W, E]

T = int(input())
X = int(input())
for test in range(T):
	W, E = list(map(int, input().split()))
	if E == 0:
		ans = solve_db(1, 0)
	else:
		assert W % E == 0
		assert W // E in (1, 2, 10)
		ans = solve_db(W // E, 1)
	print('Case #%d:' % (test + 1), ans)

# 44 min, AC AC AC (2 attempts total)

