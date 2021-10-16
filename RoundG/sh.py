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
from collections import deque
# A = list(map(int, input().split()))

def solve_1d(Z1, Z2):
	# Interested in the start of each range
	st = deque(sorted(Z1))
	ed = deque(sorted(Z2))
	indices = []	# 0=index, 1=number of st, 2=number of ed
					# 3=sum of (ed's index) before, 4=number of ed before
					# 5=sum of (st's index) after, 6=number of st after
					# 7=total distance
	while st or ed:
		p = []
		if st:
			p.append(st[0])
		if ed:
			p.append(ed[0])
		i = min(p)
		a = [i, 0, 0, None, None, None, None, None]
		while st and st[0] == i:
			st.popleft()
			a[1] += 1
		while ed and ed[0] == i:
			ed.popleft()
			a[2] += 1
		indices.append(a)
	# print(indices)
	ed_sum = 0
	ed_count = 0
	for i in indices:
		i[3] = ed_sum
		i[4] = ed_count
		ed_sum += i[0] * i[2]
		ed_count += i[2]
	st_sum = 0
	st_count = 0
	for i in reversed(indices):
		i[5] = st_sum
		i[6] = st_count
		st_sum += i[0] * i[1]
		st_count += i[1]
	best = None
	best_index = None
	for i in indices:
		i[7] = (i[4] * i[0] - i[3]) + (i[5] - i[6] * i[0])
		if best is None or i[7] < best:
			best = i[7]
			best_index = i[0]
#		print(i)
#	print()
	return best_index

T = int(input())
for test in range(T):
	K = int(input())
	X1, Y1, X2, Y2 = [], [], [], []
	for i in range(K):
		x1, y1, x2, y2 = list(map(int, input().split()))
		X1.append(x1)
		X2.append(x2)
		Y1.append(y1)
		Y2.append(y2)
	# To get to a furniture, we need to go to its shadow in x axis
	# Then we need to go to its shadow in y axis. So x and y axis are separate
	x = solve_1d(X1, X2)
	y = solve_1d(Y1, Y2)
	print('Case #%d:' % (test + 1), x, y)

