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

def is_odd_prime(z):
	for i in range(3, z, 2):
		if z % i == 0:
			return False
		if i * i > z:
			return True
	return True

def next_odd_prime(z, inc):
	while not is_odd_prime(z):
		z += inc
	return z

import math
T = int(input())
for test in range(T):
	Z = int(input())
	if Z < 15:
		ans = 2 * 3
	elif Z < 35:
		ans = 3 * 5
	else:
		s = int(math.sqrt(Z))
		if s % 2 == 0:
			s -= 1
		p0 = next_odd_prime(s, -2)
		p1 = next_odd_prime(s + 2, 2)
		while p1 * p0 > Z:
			p1 = p0
			p0 = next_odd_prime(p0 - 2, -2)
		ans = p0 * p1
	print('Case #%d:' % (test + 1), ans)

