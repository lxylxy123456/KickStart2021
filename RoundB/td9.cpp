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

// leaf: mink = maxk is load of road, value is toll of road
// non-leaf: mink and maxk record key range of descendant leaves
//           value is combined toll
class Node {
public:
	Node(int key, INT_A value): mink(key), maxk(key), value(value),
								left(nullptr), right(nullptr) {}
	Node(int mink, int maxk, INT_A value): mink(mink), maxk(maxk), value(value),
											left(nullptr), right(nullptr) {}
	bool is_leaf() const {
		return left == nullptr && right == nullptr;
	}

	int mink, maxk;
	INT_A value;
	Node *left, *right;
};

class SegmentTree {
public:
	SegmentTree() {
		root = new Node(-1, 0);
	}
	~SegmentTree() {
		// Not implemented
	}
	void set_key(int key, INT_A value) {
		root = set_key(key, value, root);
	}
	Node *set_key(int key, INT_A value, Node *n) {
		if (n->is_leaf()) {
			if (key == n->mink) {
				// Update
				n->value = value;
				return n;
			} else {
				// Replace leaf node
				int mink = min(n->mink, key);
				int maxk = max(n->mink, key);
				Node *m = new Node(mink, maxk, gcd(n->value, value));
				if (n->mink < key) {
					m->left = n;
					m->right = new Node(key, value);
				} else {
					m->left = new Node(key, value);
					m->right = n;
				}
				return m;
			}
		} else {
			if (key < n->right->mink) {
				// recurse to left
				n->left = set_key(key, value, n->left);
				n->mink = n->left->mink;
			} else {
				// recurse to right
				n->right = set_key(key, value, n->right);
				n->maxk = n->right->maxk;
			}
			n->value = gcd(n->left->value, n->right->value);
			return n;
		}
	}
	INT_A query_key(int key) {
		// Return merge of all leaves whose key <= key in parameter
		return query_key(key, root);
	}
	INT_A query_key(int key, Node *n) {
		// Return merge of all leaves whose key <= key in parameter
		if (n->maxk <= key) {
			return n->value;
		} else if (key < n->mink) {
			return 0;
		} else if (n->left->maxk <= key) {
			return gcd(n->left->value, query_key(key, n->right));
		} else {
			return query_key(key, n->left);
		}
	}

	Node *root;
};

vector<int> X, Y, L, C, W;
vector<INT_A> A, ans;
vector<vector<int>> al, c2q;
vector<int> prev_v;

void dfs(int s, SegmentTree &st) {
	// Handle all queries on s
	for (int i : c2q[s]) {
		ans[i] = st.query_key(W[i]);
	}
	for (int i : al[s]) {
		const int t = X[i] == s ? Y[i] : X[i];
		if (prev_v[t] != -1)
			continue;
		prev_v[t] = i;
		// Add edge i to edges
		st.set_key(L[i], A[i]);
		dfs(t, st);
		// Remove edge i to edges
		st.set_key(L[i], 0);
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
		SegmentTree st;
		dfs(0, st);
		printf("Case #%d:", test + 1);
		for (int i = 0; i < Q; i++) {
			/*
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
			*/
			printf(" %lld", ans[i]);
		}
		printf("\n");
	}
}

