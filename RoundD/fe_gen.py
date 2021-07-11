import random

T = 100
print(T)
for t in range(T):
	N = random.randrange(1, 10**2)
	A = random.sample(range(1, 10**3), N)
	A.sort()
	A.append(10**3)
	B = []
	for i, j in zip(A, A[1:]):
		B.append(random.randrange(i, j))
	M = 0
	for a, b in zip(A, B):
		M += b - a + 1
	M = random.randrange(1, M + 1)
	print(N, M)
	for a, b in zip(A, B):
		print(a, b)
	S = []
	for i in range(M):
		S.append(random.randrange(1, 10**3))
	print(*S)

