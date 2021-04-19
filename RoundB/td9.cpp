#include <iostream>
#include <cmath>
#include <cassert>
#include <numeric>
#include <vector>
#include <map>
#include <unordered_map>
#include <cstdio>

using namespace std;

typedef long long int INT_A;

vector<int> X, Y, L, C, W;
vector<INT_A> A, ans;
vector<vector<int>> al, c2q;
vector<int> prev_v;

void dfs(int s) {
	for (int i : al[s]) {
		const int t = X[i] == s ? Y[i] : X[i];
		if (prev_v[t] != -1)
			continue;
		prev_v[t] = i;
		dfs(t);
	}
}

int main(int argc, char *argv[]) {
	int T;
	scanf("%d", &T);
	for (int test = 0; test < T; test++) {
		int N, Q;
		scanf("%d %d", &N, &Q);
		// Read edges
		X.clear();
		Y.clear();
		L.clear();
		A.clear();
		al.clear();
		al.resize(N);
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
		// Read queries
		C.clear();
		W.clear();
		ans.clear();
		ans.resize(Q, -1);
		c2q.clear();
		c2q.resize(N);
		for (int i = 0; i < Q; i++) {
			int c, w;
			scanf("%d %d", &c, &w);
			c--;
			C.push_back(c);
			W.push_back(w);
			c2q[c].push_back(i);
		}
		// DFS
		prev_v.clear();
		prev_v.resize(N, -1);
		prev_v[0] = -2;
		dfs(0);
		printf("Case #%d:", test + 1);
		for (int i = 0; i < Q; i++) {
			int num_tolls = 0;
			INT_A gcd_tolls = 0;
			int c = C[i], w = W[i];
			while (c) {
				int i = prev_v[c];
				const int s = X[i] == s ? Y[i] : X[i];
				if (w >= L[i]) {
					if (num_tolls == 0) {
						gcd_tolls = A[i];
					} else {
						gcd_tolls = std::gcd(gcd_tolls, A[i]);
					}
					num_tolls++;
				}
				c = s;
			}
			printf(" %lld", gcd_tolls);
		}
		printf("\n");
	}
}

