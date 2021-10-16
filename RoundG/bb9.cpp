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
		long N, K;
		cin >> N >> K;
		long B[N];
		for (int i = 0; i < N; i++) {
			cin >> B[i];
		}
		long s[N + 1];
		long ans = N + 10;
		s[0] = 0;
		for (int i = 0; i < N; i++) {
			s[i + 1] = s[i] + B[i];
			if (B[i] == K) {
				ans = 1;
			}
		}
		int best[K];
		best[0] = 0;
		for (int i = 1; i < K; i++) {
			best[i] = N + 10;
		}
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < i; j++) {
				long k = s[i] - s[j];
				if (k >= 0 && k < K) {
					if (best[k] > i - j) {
						best[k] = i - j;
					}
				}
			}
			for (int j = i + 1; j <= N; j++) {
				long k = K - (s[j] - s[i]);
				if (k >= 0 && k < K) {
					if (ans > best[k] + j - i) {
						ans = best[k] + j - i;
					}
				}
			}
		}
		if (ans > N) {
			ans = -1;
		}
		cout << "Case #" << (test + 1) << ": " << (ans) << endl;
	}
	return 0;
}

