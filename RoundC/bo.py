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

import random
# import math, sys
# sys.setrecursionlimit(100000000)
from collections import defaultdict
# A = list(map(int, input().split()))

import re

def lexer(e):
	while e:
		matched = re.match('(\d+)(?:[^\d]|$)', e)
		if matched:
			m = matched.groups()[0]
			yield m
			e = e[len(m):]
		else:
			assert e[0] in '()+*#'
			yield e[0]
			e = e[1:]

def parser(e):
	lst = list(e)
	start = 0
	def recu():
		nonlocal start
		if lst[start] == '(':
			start += 1
			a = recu()
			b = lst[start]; start += 1
			c = recu()
			assert lst[start] == ')'; start += 1
			return a, b, c
		else:
			a = int(lst[start]); start += 1
			return a
	return recu()

class Value():
	def __init__(self, a, b=None, c=None):
		self.data = []
		if type(a) is int and b is None and c is None:
			self.data.append((a, 1))
	def __add__(self, a):
		print(self, a)
		return self
	def hash_op(self, a):
		print(self, a)
		return self
	def __mul__(self, a):
		print(self, a, '*')
		return self

def simplify(parsed):
	if type(parsed) == int:
		return Value(parsed)
	a, b, c = parsed
	_a = simplify(a)
	_c = simplify(c)
	if b == '+':
		return _a + _c
	elif b == '*':
		return _a * _c
	elif b == '#':
		return _a.hash_op(_c)

def sign(E):
	a = defaultdict(lambda: random.randint(0, 100))
	ans = []
	def evaluate(e):
		if type(e) == int:
			return e
		i, j, k = e
		if j == '+':
			return evaluate(i) + evaluate(k)
		elif j == '*':
			return evaluate(i) * evaluate(k)
		elif j == '#':
			return a[(evaluate(i), evaluate(k))]
		else:
			raise ValueError
	for i in E:
		ans.append(evaluate(i))
	return ans

T = int(input())
for test in range(T):
	N = int(input())
	E = []
	S = []
	for i in range(N):
		E.append(parser(lexer(input())))
		S.append([])
	for i in range(10):
		list(map(lambda x, y: x.append(y), S, sign(E)))
	H = []
	for i in S:
		H.append(hash(tuple(i)))
	ans = []
	use = 0
	for index, i in enumerate(H):
		found = H.index(i)
		if found < index:
			ans.append(ans[found])
		else:
			use += 1
			ans.append(use)
	print('Case #%d:' % (test + 1), ' '.join(map(str, ans)))

# 38 min, AC, AC (1 attempts total)

