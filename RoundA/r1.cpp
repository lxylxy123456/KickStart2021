#include <iostream>
#include <algorithm>

using std::cin;
using std::cout;
using std::endl;
using std::abs;
using std::max;

#define INT unsigned long long int

int main() {
	int T;
	cin >> T;
	for (int index = 0; index < T; index++) {
		int R, C;
		cin >> R >> C;
		INT m[R][C];
		INT n[R][C];
		for (int i = 0; i < R; i++)
			for (int j = 0; j < C; j++) {
				cin >> m[i][j];
				n[i][j] = m[i][j];
			}
		for (int xi = 0; xi < R; xi++)
			for (int yi = 0; yi < C; yi++)
				for (int xj = 0; xj < R; xj++)
					for (int yj = 0; yj < C; yj++) {
						INT&& _1 = abs(xi - xj) + abs(yi - yj);
						if (n[xj][yj] >= _1) {
							INT&& _2 = n[xj][yj] - _1;
							if (n[xi][yi] < _2)
								n[xi][yi] = _2;
						}
					}
		INT ans = 0;
		for (int i = 0; i < R; i++)
			for (int j = 0; j < C; j++)
				ans += n[i][j] - m[i][j];
		cout << "Case #" << (index + 1) << ": " << ans << endl;
	}
}

