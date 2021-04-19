T = 100
print(T)
for i in range(T):
	if i < 20:
		N = 50000
		Q = 100000
	else:
		N = 1000
		Q = 1000
	print(N, Q)
	for i in range(N - 1):
		print(i + 1, i + 2, 1, 1)
	for i in range(Q):
		print(1, 1)

