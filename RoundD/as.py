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
from collections import defaultdict, Counter
# A = list(map(int, input().split()))

def get_ap_b(a, c):
	if (a + c) % 2 == 0:
		return (a + c) // 2
	return None

T = int(input())
for test in range(T):
	square = []
	square.append(list(map(int, input().split())))
	square.append(list(map(int, input().split())))
	square.append(list(map(int, input().split())))
	square[1].insert(1, None)
	# print(square)
	base = 0
	base += int(get_ap_b(square[0][0], square[0][2]) == square[0][1])
	base += int(get_ap_b(square[2][0], square[2][2]) == square[2][1])
	base += int(get_ap_b(square[0][0], square[2][0]) == square[1][0])
	base += int(get_ap_b(square[0][2], square[2][2]) == square[1][2])
	vote = Counter()
	vote[get_ap_b(square[0][0], square[2][2])] += 1
	vote[get_ap_b(square[2][0], square[0][2])] += 1
	vote[get_ap_b(square[1][0], square[1][2])] += 1
	vote[get_ap_b(square[0][1], square[2][1])] += 1
	vote[None] = 0
	ans = base + max(vote.values())
	print('Case #%d:' % (test + 1), ans)

