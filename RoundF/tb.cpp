#include <iostream>
#include <cmath>
#include <cassert>
// #include <algorithm>
// #include <vector>
// #include <set>
// #include <map>
// #include <unordered_map>

using namespace std;

int main(int argc, char *argv[]) {
	int T;
	cin >> T;
	for (int test = 0; test < T; test++) {
		int N;
		char S[500010];
		cin >> N;
		cin >> S;
		int l[500010];
		int r[500010];
		int cur = N;
		for (int i = 0; i < N; i++) {
			if (S[i] == '1')
				cur = i;
			l[i] = cur;
		}
		cur = -1;
		for (int i = N - 1; i >= 0; i--) {
			if (S[i] == '1')
				cur = i;
			r[i] = cur;
		}
		long long int ans = 0;
		for (int i = 0; i < N; i++) {
			ans += min(abs(l[i] - i), abs(r[i] - i));
		}
		cout << "Case #" << (test + 1) << ": " << (ans) << endl;
	}
	return 0;
}

