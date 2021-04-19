#include <iostream>
#include <cmath>
#include <cassert>
#include <numeric>
#include <vector>
#include <map>
#include <cstdio>

using namespace std;

typedef long long int INT_A;

int main(int argc, char *argv[]) {
	int T;
	scanf("%d", &T);
	for (int test = 0; test < T; test++) {
		int N, Q;
		scanf("%d %d", &N, &Q);
		vector<int> X, Y, L;
		vector<INT_A> A;
		vector<vector<int>> al(N);
		for (int i = 0; i < N - 1; i++) {
			int x, y, l;
			INT_A a;
			scanf("%d %d %d %lld", &x, &y, &l, &a);
			x--;
			y--;
			X.push_back(x);
			Y.push_back(y);
			L.push_back(l);
			A.push_back(a);
			al[x].push_back(i);
			al[y].push_back(i);
		}
		vector<int> fringe;
		vector<int> prev(N, -1);
		{
			// dfs
			fringe.push_back(0);
			prev[0] = -2;
			int counter = 0;
			while (fringe.size()) {
				if (counter++ > N * 2 + 100) {
					return 0;
				}
				int s = fringe.back();
				fringe.pop_back();
				for (auto i = al[s].begin(); i != al[s].end(); i++) {
					const int t = X[*i] == s ? Y[*i] : X[*i];
					if (prev[t] != -1)
						continue;
					prev[t] = *i;
					fringe.push_back(t);
				}
			}
			fprintf(stderr, "%d\n", counter);
		}
		printf("Case #%d:", test + 1);
		for (int i = 0; i < Q; i++) {
			int num_tolls = 0;
			INT_A gcd_tolls = 0;
			int c, w;
			scanf("%d %d", &c, &w);
			c--;
			int counter = 0;
			while (c) {
				if (counter++ > N * 2 + 100) {
					return 0;
				}
				int i = prev[c];
				const int s = X[i] == s ? Y[i] : X[i];
				if (w >= L[i]) {
					if (num_tolls == 0) {
						gcd_tolls = A[i];
						num_tolls++;
					} else {
						gcd_tolls = std::gcd(gcd_tolls, A[i]);
						num_tolls++;
					}
				}
				c = s;
			}
			printf(" %lld", gcd_tolls);
		}
		printf("\n");
	}
}

