#include <iostream>
#include <cmath>
#include <cassert>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
// #include <unordered_map>

using namespace std;

bool comp_first(const std::pair<int, int> a, const std::pair<int, int> b) {
	return a.first < b.first;
}

bool comp_second(const std::pair<int, int> a, const std::pair<int, int> b) {
	return a.second < b.second;
}

void swap_set(set<pair<int, int>>& AB, set<pair<int, int>>::iterator i, int f,
				int s) {
	AB.erase(i);
	if (f <= s) {
		AB.emplace(f, s);
	}
}

int main(int argc, char *argv[]) {
	int T;
	cin >> T;
	for (int test = 0; test < T; test++) {
		int N, M;
		cin >> N >> M;
		set<pair<int, int>> AB;
		for (int i = 0; i < N; i++) {
			int a, b;
			cin >> a >> b;
			AB.emplace(a, b);
		}
		vector<int> S;
		for (int i = 0; i < M; i++) {
			int s;
			cin >> s;
			S.emplace_back(s);
		}
		vector<int> ans;
		for (int s : S) {
			auto i = upper_bound(AB.begin(), AB.end(),
									std::pair<int, int>(s, s), comp_first);
			auto j = lower_bound(AB.begin(), AB.end(),
									std::pair<int, int>(s, s), comp_second);
			if (i == AB.begin()) {
				ans.push_back(i->first);
				swap_set(AB, i, i->first + 1, i->second);
			} else if (j == AB.end()) {
				auto k = AB.find(*AB.rbegin());
				ans.push_back(k->second);
				swap_set(AB, k, k->first, k->second - 1);
			} else if ((--i)++ == j) {
				ans.push_back(s);
				if (j->first == s) {
					swap_set(AB, j, j->first + 1, j->second);
				} else if (j->second == s) {
					swap_set(AB, j, j->first, j->second - 1);
				} else {
					int b = j->second;
					swap_set(AB, j, j->first, s - 1);
					AB.emplace(s + 1, b);
				}
			} else if (i == j) {
				j--;
				int db = s - j->second;
				int da = i->first - s;
				if (db <= da) {
					ans.push_back(j->second);
					swap_set(AB, j, j->first, j->second - 1);
				} else {
					ans.push_back(i->first);
					swap_set(AB, i, i->first + 1, i->second);
				}
			} else {
				assert(0);
			}
		}
		
		cout << "Case #" << (test + 1) << ":";
		for (int i : ans) {
			cout << ' ' << i;
		}
		cout << endl;
	}
	return 0;
}

