#include <iostream>
#include <cmath>
#include <cassert>
// #include <algorithm>
#include <vector>
#include <set>
#include <map>
// #include <unordered_map>

using namespace std;

int main(int argc, char *argv[]) {
	int T;
	cin >> T;
	for (int test = 0; test < T; test++) {
		int D, N, K;
		cin >> D >> N >> K;
		vector<int> H, S, E;
		multiset<pair<int, int>> events;
		for (int i = 0; i < N; i++) {
			int h, s, e;
			cin >> h >> s >> e;
			H.push_back(h);
			S.push_back(s);
			E.push_back(e);
			events.insert({s * 2, h});
			events.insert({e * 2 + 1, -h});
		}
		long long int ans = 0;
		long long int high_sum = 0;
		multiset<int> high;
		multiset<int> low;
		for (auto e : events) {
			// cout << e.first << ',' << e.second << endl;
			int h = e.second;
			if (h > 0) {
				// start
				if (h <= *high.begin()) {
					low.insert(h);
					while (low.size() && (high.size() < K)) {
						auto it = low.end();
						it--;
						int tmp = *it;
						low.erase(it);
						high.insert(tmp);
						high_sum += tmp;
					}
				} else {
					high.insert(h);
					high_sum += h;
					while (high.size() > K) {
						auto it = high.begin();
						int tmp = *it;
						high.erase(it);
						low.insert(tmp);
						high_sum -= tmp;
					}
				}
			} else {
				// end
				auto it = low.find(-h);
				if (it != low.end()) {
					low.erase(it);
				} else {
					auto it = high.find(-h);
					assert(it != high.end());
					high.erase(it);
					high_sum -= -h;
					while (low.size() && (high.size() < K)) {
						auto it = low.end();
						it--;
						int tmp = *it;
						low.erase(it);
						high.insert(tmp);
						high_sum += tmp;
					}
				}
			}
			ans = max(ans, high_sum);
		}
		cout << "Case #" << (test + 1) << ": " << (ans) << endl;
	}
	return 0;
}

