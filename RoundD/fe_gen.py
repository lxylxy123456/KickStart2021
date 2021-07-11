import random

T = 100
print(T)
LIM_A = 10**7
for t in range(T):
	N = random.randrange(1, 10**5)
	# A = random.sample(range(1, LIM_A), N)
	# A.sort()
	A = set()
	while len(A) < N:
		A.add(random.randrange(1, LIM_A))
	A = sorted(A)
	A.append(LIM_A)
	B = []
	for i, j in zip(A, A[1:]):
		B.append(random.randrange(i, j))
	M = 0
	for a, b in zip(A, B):
		M += b - a + 1
	M = random.randrange(1, min(M + 1, 10**5))
	print(N, M)
	for a, b in zip(A, B):
		print(a, b)
	S = []
	for i in range(M):
		S.append(random.randrange(1, LIM_A))
	print(*S)

