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


T = int(input())
for test in range(T):
	N = int(input())
	S = input()
	assert len(S) == N
	ans = []
	prev = None
	cur = 0
	for index, i in enumerate(S):
		if prev is not None and prev < i:
			cur += 1
		else:
			cur = 1
		ans.append(cur)
		prev = i
	print('Case #%d:' % (test + 1), *ans)

