#include <iostream>
#include <cmath>
#include <cassert>
#include <numeric>
#include <vector>
#include <map>

using namespace std;

typedef long long int INT_A;

int main(int argc, char *argv[]) {
	int T;
	cin >> T;
	for (int test = 0; test < T; test++) {
		int N, Q;
		cin >> N >> Q;
		vector<map<int, pair<int, INT_A>>> al(N);
		for (int i = 0; i < N - 1; i++) {
			int x, y, l;
			INT_A a;
			cin >> x >> y >> l >> a;
			x--;
			y--;
			al[x][y] = pair<int, INT_A>(l, a);
			al[y][x] = pair<int, INT_A>(l, a);
		}
		vector<int> fringe;
		vector<bool> visited(N, false);
		vector<pair<int, pair<int, INT_A>>> prev(N, {-1, {-1, -1}});
		{
			// dfs
			fringe.push_back(0);
			while (fringe.size()) {
				int s = *(fringe.rbegin());
				fringe.pop_back();
				visited[s] = true;
				for (auto i = al[s].begin(); i != al[s].end(); i++) {
					const int &t = i->first;
					const pair<int, INT_A> &la = i->second;
					if (visited[t])
						continue;
					prev[t].first = s;
					prev[t].second = la;
					fringe.push_back(t);
				}
			}
		}
		cout << "Case #" << (test + 1) << ":";
		for (int i = 0; i < Q; i++) {
			int num_tolls = 0;
			INT_A gcd_tolls = 0;
			int c, w;
			cin >> c >> w;
			c--;
			while (c) {
				const int &s = prev[c].first;
				const int &l = prev[c].second.first;
				const INT_A &a = prev[c].second.second;
				if (w >= l) {
					if (num_tolls == 0) {
						gcd_tolls = a;
						num_tolls++;
					} else {
						gcd_tolls = std::gcd(gcd_tolls, a);
						num_tolls++;
					}
				}
				c = s;
			}
			cout << " " << gcd_tolls;
		}
		cout << endl;
	}
}

/*
	ans = []
	for c, w in zip(QC, QW):
		tolls = []
		while c:
			s, l, a = prev[c]
			if w >= l:
				tolls.append(a)
			c = s
		ans.append(gcd(tolls))
	print('Case #%d:' % (test + 1), ' '.join(map(str, ans)))
*/
