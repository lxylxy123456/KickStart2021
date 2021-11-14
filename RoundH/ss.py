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
	pre = deque([])
	post = deque(map(int, S))
	ans = S
	found = True
	while found:
		found = False
		while post:
			p1 = post.popleft()
			if post:
				p2 = post.popleft()
				if (p1 + 1) % 10 == p2:
					p2 = (p2 + 1) % 10
					post.appendleft(p2)
					if pre:
						post.appendleft(pre.pop())
					found = True
				else:
					post.appendleft(p2)
					pre.append(p1)
			else:
				pre.append(p1)
		post, pre = pre, post
	ans = ''.join(map(str, post))
	print('Case #%d:' % (test + 1), ans)

'''
1
4
8912
'''
