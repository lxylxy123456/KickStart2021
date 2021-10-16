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

import heapq
# import math, sys
# sys.setrecursionlimit(100000000)
from collections import defaultdict
# A = list(map(int, input().split()))

T = int(input())
for test in range(T):
	N, K = map(int, input().split())
	B = list(map(int, input().split()))
	s = [0]	# [i] = sum of B[:i]
	for i in B:
		s.append(s[-1] + i)
	ans = (N, K, B, s)
	poss1 = []	# try early
	poss2 = []	# try late
	for i in range(K + 1):
		poss1.append([])
		poss2.append([])
	ans = None
	poss1[0].append((-1, 0))
	for i in range(N):
		for j in range(i + 1, N + 1):
			d = s[j] - s[i]
			if d <= K:
				poss1[d].append((j, j - i))
				poss2[d].append((i, j - i))
#	print(s)
#	print(poss1)
#	print(poss2)
	for i in range(K):
		p1 = poss1[i]
		p2 = poss2[K - i]
		events = []	# 0: remove p2, 1: add p1
		right = []
		right_neg = defaultdict(int)
		for t, j in p1:
			events.append((t, 1, j))
		for t, j in p2:
			events.append((t, 0, j))
			right.append(j)
		heapq.heapify(right)
		events.sort()
#		print(i, p1, p2)
#		print(events, right)
		for t, act, num in events:
			if act == 0:
				right_neg[num] += 1
#				print(right_neg, right)
			else:
				while right and right_neg.get(right[0]):
					right_neg[right[0]] -= 1
					heapq.heappop(right)
				# calculate answer
				if right:
					if ans is None or ans > num + right[0]:
						ans = num + right[0]
#		print()
	if ans is None:
		ans = -1
	print('Case #%d:' % (test + 1), ans)

