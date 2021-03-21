#include <iostream>
#include <algorithm>
#include <map>

using namespace std;

template <typename T>
T disj_find(map<T, T> &m, T x) {
	if (m.find(x) == m.end())
		return x;
	return m[x] = disj_find(m, m[x]);
}

int main() {
	int T;
	cin >> T;
	for (int index = 0; index < T; index++) {
		int N;
		cin >> N;
		int A[N][N];
		int B[N][N];
		for (int i = 0; i < N; i++)
			for (int j = 0; j < N; j++)
				cin >> A[i][j];
		for (int i = 0; i < N; i++)
			for (int j = 0; j < N; j++)
				cin >> B[i][j];
		{
			int tmp;
			for (int i = 0; i < 2; i++)
				for (int j = 0; j < N; j++)
					cin >> tmp;
		}
		int ans = 0;
		multimap<int, pair<int, int>> m;
		for (int i = 0; i < N; i++)
			for (int j = 0; j < N; j++)
				if (A[i][j] == -1)
					m.emplace(B[i][j], pair<int, int>{i, j});
		
		map<pair<int, int>, pair<int, int>> disj_map;
		for (auto i = m.rbegin(); i != m.rend(); i++) {
			pair<int, int> p1 = {0, i->second.first},
							p2 = {2, i->second.second};
			pair<int, int> f1 = disj_find(disj_map, p1),
							f2 = disj_find(disj_map, p2);
			if (f1 == f2)
				ans += i->first;
			else
				disj_map[f1] = f2;
		}
		cout << "Case #" << (index + 1) << ": " << ans << endl;
	}
}

