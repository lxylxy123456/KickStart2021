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

def remove_redundant(l):
	a = defaultdict(int)
	for i in l:
		a[i[1:]] += i[0]
	ans = []
	for k, v in a.items():
		ans.append((v, *k))
	ans.sort()
	return tuple(ans)

def simplify(parsed):
	if type(parsed) == int:
		if parsed == 0:
			return ()
		return ((parsed,),)
	a, b, c = parsed
	a = simplify(a)
	c = simplify(c)
	if b == '+':
		aa = list(a)
		cc = list(c)
		return remove_redundant(a + c)
	elif b == '*':
		ans = []
		for i in a:
			for j in c:
				ans.append((i[0] * j[0], *sorted(i[1:] + j[1:])))
		return remove_redundant(ans)
	elif b == '#':
		return ((1, (a, c)),)

if not 'test':
	for i, o in [
		('0',				() ),
		('1',				((1,),) ),
		('(2#3)',			((1, (((2,),), ((3,),))),) ),
		('(2#(3#4))',		((1, (((2,),), ((1, (((3,),), ((4,),))),))),) ),
		('(2#(5*(3#4)))',	((1, (((2,),), ((5, (((3,),), ((4,),))),))),) ),
		('(9*((2#3)*(6#7)))',
			((9, (((2,),), ((3,),)), (((6,),), ((7,),))),) ),
		('((9*(2#3))*(6#7))',
			((9, (((2,),), ((3,),)), (((6,),), ((7,),))),) ),
		('((2#3)+(5#6))',
			((1, (((2,),), ((3,),))), (1, (((5,),), ((6,),))),) ),
	]:
		print(i)
		print(simplify(parser(lexer(i))))
		print(o)
		print()

T = int(input())
for test in range(T):
	N = int(input())
	E = []
	S = []
	for i in range(N):
		E.append(parser(lexer(input())))
		S.append(simplify(E[-1]))
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
# 76 min, AC, AC (4 attempts total), using rigorous method

