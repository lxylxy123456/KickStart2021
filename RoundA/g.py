import sys
stdin = sys.stdin
stdin = open('g.txt')
input = lambda: stdin.readline()[:-1]


import operator

def goodness(N, S):
	assert len(S) == N
	# 6: 1 6, 2 5, 3 4
	n = N // 2
	return sum(list(map(operator.ne, S[: n], ''.join(reversed(S[N - n :])))))

T = int(input())
for i in range(T):
	N, K = map(int, input().split())
	S = input()
	print('Case #%d:' % (i + 1), abs(K - goodness(N, S)))

