#include <iostream>
#include <algorithm>
#include <set>
#include <cassert>

using std::cin;
using std::cout;
using std::endl;
using std::abs;
using std::max;
using std::min;

#define INT long long int
#define keep_max 5

class Coordinate {
	public:
	Coordinate(int x, int y, INT n): x(x), y(y), n(n) {}
	bool operator<(const Coordinate& rhs) const {
		if (rhs.n < n)
			return true;
		if (n < rhs.n)
			return false;
		if (rhs.x < x)
			return true;
		if (x < rhs.x)
			return false;
		return rhs.y < y;
	}
	int x, y;
	INT n;
};

int main() {
	int T;
	cin >> T;
	for (int index = 0; index < T; index++) {
		int R, C;
		cin >> R >> C;
		INT m[R][C];
		INT n[R][C];
		int skip[R][C];
		std::set<Coordinate> q;
		for (int i = 0; i < R; i++)
			for (int j = 0; j < C; j++) {
				cin >> m[i][j];
				n[i][j] = m[i][j];
				skip[i][j] = 0;
				if (n[i][j]) {
					Coordinate a = {i, j, n[i][j]};
					q.insert(a);
				}
			}
		for (const Coordinate& i : q) {
			int xi = i.x, yi = i.y;
//			std::cout << xi << ' ' << yi << ' ' << i.n << std::endl;
			{
				if (skip[xi][yi])
					continue;
				INT lowerx = max(0ll, xi - n[xi][yi]);
				INT upperx = min((INT) R, xi + n[xi][yi] + 1);
				for (int xj = lowerx; xj < upperx; xj++) {
					INT boundx = n[xi][yi] - abs(xi - xj);
//					if (boundx <= 0)
//						assert(0); // continue;
					INT lowery = max(0ll, yi - boundx);
					INT uppery = min((INT) C, yi + boundx + 1);
					for (int yj = lowery; yj < uppery; yj++) {
						INT bound = boundx - abs(yi - yj);
						if (n[xj][yj] < bound) {
							n[xj][yj] = bound;
							skip[xj][yj] = 1;
						}
					}
				}
			}
		}
		/*
		for (int xi = 0; xi < R; xi++)
			for (int yi = 0; yi < C; yi++) {
				if (skip[xi][yi])
					continue;
				for (int xj = 0; xj < R; xj++) {
					int boundx = n[xi][yi] - abs(xi - xj);
					if (boundx <= 0)
						continue;
					for (int yj = 0; yj < C; yj++) {
						INT bound = boundx - abs(yi - yj);
						if (n[xj][yj] < bound) {
							n[xj][yj] = bound;
							skip[xj][yj] = 1;
						}
					}
				}
			}
		*/
		INT ans = 0;
		for (int i = 0; i < R; i++)
			for (int j = 0; j < C; j++)
				ans += n[i][j] - m[i][j];
		cout << "Case #" << (index + 1) << ": " << ans << endl;
	}
}

