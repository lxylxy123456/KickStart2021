import sys
a = sys.stdin.read()
xy = []
for i in a.split('\n'):
	if i.strip():
		xy.append(list(map(int, i.split())))

import matplotlib.pyplot as plt
for (x1, y1), (x2, y2) in zip(xy, xy[1:] + xy[:1]):
	plt.plot((x1, x2), (y1, y2))
	print((x1, y1), (x2, y2))

plt.show()

