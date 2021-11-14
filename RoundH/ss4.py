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
	from collections import deque
	nxt = []
	prv = []
	ind = []
	for i in range(10):
		ind.append(set())
	s = list(map(int, S))
	for index, i in enumerate(s):
		nxt.append(index + 1)
		prv.append(index - 1)
		if index < N - 1 and (i + 1) % 10 == s[index + 1]:
			ind[i].add(index)
	prv[0] = None
	nxt[-1] = None
	fst = 0
	lst = N - 1
	# Start
	found = True
	while found:
		found = False
		for i in range(10):
			for j in ind[i]:
				found = True
				assert s[j] == i and s[nxt[j]] == (i + 1) % 10
				if prv[j] is not None and (s[prv[j]] + 1) % 10 == i:
					ind[(i - 1) % 10].remove(prv[j])
				if nxt[nxt[j]] is not None and (i + 2) % 10 == s[nxt[nxt[j]]]:
					ind[(i + 1) % 10].remove(nxt[j])
				s[j] = (i + 2) % 10
				# drop s[nxt[j]]
				if nxt[nxt[j]] is not None:
					nxt[j] = nxt[nxt[j]]
					prv[nxt[j]] = j
				else:
					nxt[j] = None
					lst = j
				if nxt[j] is not None and s[nxt[j]] == (i + 3) % 10:
					ind[(i + 2) % 10].add(j)
				if prv[j] is not None and s[prv[j]] == (i + 1) % 10:
					ind[(i + 1) % 10].add(prv[j])
			ind[i].clear()
	ans = []
	i = fst
	while i is not None:
		ans.append(s[i])
		i = nxt[i]
	ans = ''.join(map(str, ans))
	print('Case #%d:' % (test + 1), ans)

'''
1
4
8912
'''
