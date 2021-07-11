#include <iostream>
#include <cmath>
#include <cassert>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
// #include <unordered_map>

using namespace std;

typedef long long int INT;

int main(int argc, char *argv[]) {
	int T;
	cin >> T;
	for (int test = 0; test < T; test++) {
		int N, M;
		cin >> N >> M;
		map<INT, INT> AB;
		for (int i = 0; i < N; i++) {
			INT a, b;
			cin >> a >> b;
			AB[a] = b;
		}
		vector<INT> S;
		for (int i = 0; i < M; i++) {
			INT s;
			cin >> s;
			S.emplace_back(s);
		}
		vector<INT> ans;
		cout << "Case #" << (test + 1) << ":";
		// int sndex = 0;
		for (INT s : S) {
			map<INT, INT>::iterator i = upper_bound(
				AB.begin(), AB.end(), std::pair<const INT, INT>(s, s));
			if (i == AB.begin()) {
				ans.push_back(i->first);
				pair<INT, INT> ii = *i;
				ii.first++;
				AB.erase(i);
				if (ii.first <= ii.second) {
					AB[ii.first] = ii.second;
				}
			} else {
				map<INT, INT>::iterator j = i;
				j--;
				if (s <= j->second) {
					assert(j->first <= s);
					ans.push_back(s);
					INT sec = j->second;
					j->second = s - 1;
					if (j->first > j->second) {
						AB.erase(j);
					}
					if (s + 1 <= sec) {
						AB[s + 1] = sec;
					}
				} else {
					INT da = (i == AB.end()) ? 0x7fffffffffffffff : i->first;
					INT db = j->second;
					if (db <= da) {
						ans.push_back(j->second);
						j->second--;
						if (j->first > j->second) {
							AB.erase(j);
						}
					} else {
						ans.push_back(i->first);
						pair<INT, INT> ii = *i;
						ii.first++;
						AB.erase(i);
						if (ii.first <= ii.second) {
							ans[ii.first] = ii.second;
						}
					}
				}
			}
			cout << ' ' << *ans.rbegin();
			// cout << flush;
			// cerr << "[" << sndex++ << "]" << flush;
		}
		cout << endl;
	}
	return 0;
}

