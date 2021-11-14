#include <iostream>
#include <cmath>
#include <cassert>
// #include <algorithm>
// #include <vector>
#include <list>
// #include <map>
#include <unordered_map>

using namespace std;

int main(int argc, char *argv[]) {
	int T;
	cin >> T;
	for (int test = 0; test < T; test++) {
		int N;
		cin >> N;
		char S[N + 1];
		cin >> S;
		list<int> s;
		for (int i = 0; i < N; i++) {
			s.push_back(S[i] - '0');
		}
		// Build index
		unordered_map<>
		for (auto i = s.begin(); i != s.end(); i++) {
			
		}
		bool found = true;
		while (found) {
			for (int i = 0; i < 10; i++) {
				
			}
		}
		// Output
		for (int &i : s) {
			i += '0';
		}
		string ans(s.begin(), s.end());
		cout << "Case #" << (test + 1) << ": " << (ans) << endl;
	}
	return 0;
}

