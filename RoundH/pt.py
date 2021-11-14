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
	P = input()
	ans = 0
	last_r = 0
	last_y = 0
	last_g = 0
	for i in P:
		r, y, g = {
    		'U': (0, 0, 0),	# Uncolored
    		'R': (1, 0, 0),	# Red
    		'Y': (0, 1, 0),	# Yellow
    		'B': (0, 0, 1),	# Blue
    		'O': (1, 1, 0),	# Orange
    		'P': (1, 0, 1),	# Purple
    		'G': (0, 1, 1),	# Green
    		'A': (1, 1, 1),	# Gray
		}[i]
		if r:
			if not last_r:
				ans += 1
				last_r = 1
		else:
			last_r = 0
		if y:
			if not last_y:
				ans += 1
				last_y = 1
		else:
			last_y = 0
		if g:
			if not last_g:
				ans += 1
				last_g = 1
		else:
			last_g = 0
	print('Case #%d:' % (test + 1), ans)

