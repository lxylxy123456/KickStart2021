import random
print(1)
N = 1000
Q = 2
print(N, Q)
print(random.randrange(10**6 + 1))
for i in range(N - 1):
	print(i + 1,
			random.randrange(10**6 + 1),
			random.randrange(10**6 + 1))
for i in range(Q):
	print(random.randrange(N) + 1, random.randrange(N) + 1)

