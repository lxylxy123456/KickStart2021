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

def V(x, P):
	if x == 0:
		return 0
	ans = 0
	while x % P == 0:
		x //= P
		ans += 1
	return ans

T = int(input())
for test in range(T):
	N, Q, P = map(int, input().split())
	A = list(map(int, input().split()))
	q = []
	for i in range(Q):
		q.append(tuple(map(int, input().split())))
	ans = []
	# sum(V(A[i]**S - (A[i] % P)**S), i, L, R)
	# A[i] = P * k + r
	# A[i]**S - (A[i] % P)**S
	#  = (P * k + r)**S - r**S
	#  = sum(C(S, i) * (P*k)**i * r**(S-i), i, 1, S)
	# print(P)
	for i in q:
		if i[0] == 1:
			A[i[1] - 1] = i[2]
		else:
			assert i[0] == 2
			_, S, L, R = i
			a = 0
			for j in range(L - 1, R):
				# print(A[j], S, V(A[j]**S - (A[j] % P)**S, P))
				a += V(A[j]**S - (A[j] % P)**S, P)
			ans.append(a)
	print('Case #%d:' % (test + 1), *ans)

