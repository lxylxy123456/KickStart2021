try:
	import sys
	stdin = sys.stdin
	stdin = open('c.txt')
	input = lambda: stdin.readline()[:-1]
except Exception:
	pass


# 0 0 1 1
# 0 0 1 1
# 1 1 1 0 <
# 1 1 0 0
#     ^     Should not remove this

from collections import defaultdict
T = int(input())
for index in range(T):
	C = R = int(input())
	# m is the original data
	A = []
	for i in range(R):
		A.append(list(map(int, input().split())))
	B = []
	for i in range(R):
		B.append(list(map(int, input().split())))
	# Ignore checksum data
	input()
	input()
	# row_to_vir_col
	# TODO: use defaultdict if TLE, or use C++ priority queue etc.
	virs = {}
	r2vir = defaultdict(set)
	c2vir = defaultdict(set)
	for i in range(R):
		for j in range(C):
			if A[i][j] == -1:
				virs[(i, j)] = B[i][j]
				r2vir[i].add((i, j))
				c2vir[j].add((i, j))
#	r2c = []
#	for i in range(R):
#		r2c.append(set())
#		for j in range(C):
#			if A[i][j] == -1:
#				r2c[-1].add(j)
#	c2r = []
#	for j in range(C):
#		c2r.append(set())
#		for i in range(R):
#			if A[i][j] == -1:
#				c2r[-1].add(i)
	def remove_virus(x, y):
		global virs, r2vir, c2vir
		del virs[(x, y)]
		r2vir[x].remove((x, y))
		if not r2vir[x]:
			del r2vir[x]
		c2vir[y].remove((x, y))
		if not c2vir[y]:
			del c2vir[y]

	ans = 0
#	if index == 1: import pdb; pdb.set_trace()
	while virs:
#		cheapest = None
		price = 10000000000
		for (x, y), p in virs.items():
			if len(r2vir[x]) <= 1 or len(c2vir[y]) <= 1:
				remove_virus(x, y)
				price = -1
				break
#			if p < price:
#				cheapest = x, y
#				price = p
		if price == -1:
			continue
#		if cheapest is None:
#			break
#		ans += price
#		remove_virus(*cheapest)
		# Find a cheapest way to expose a 1 virus
		direction = None
		num = None
		for x, vs in r2vir.items():
			prices = sorted(map(virs.__getitem__, vs))
			if price > sum(prices[:-1]):
				price = sum(prices[:-1])
				direction = 'r'
				num = x
		for y, vs in c2vir.items():
			prices = sorted(map(virs.__getitem__, vs))
			if price > sum(prices[:-1]):
				price = sum(prices[:-1])
				direction = 'c'
				num = y
		assert direction is not None
		to_remove_virs = list(r2vir[num] if direction == 'r' else c2vir[num])
		to_remove_virs.sort(key=virs.__getitem__)
		for i in to_remove_virs[:-1]:
			ans += virs[i]
			remove_virus(*i)
		# print(direction, num, to_remove_virs)
		# 0/0
	print('Case #%d:' % (index + 1), ans)

