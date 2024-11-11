#include <bits/stdc++.h>
// #include <atcoder/all>
using namespace std;
// using namespace atcoder;

int rec(int x, vector<vector<int>> &children_vec, vector<int> &ans_vec) {
    if (ans_vec.at(x) >= 0) {
        return ans_vec.at(x);
    }
    int ret = 1;
    for (int c : children_vec.at(x)) {
        ret += rec(c, children_vec, ans_vec);
    }
    return ret;
}

int main() {
    int N;
    cin >> N;
    vector<int> P(N);
    P.at(0) = -1;
    for (int i = 1; i < N; i++) {
        cin >> P.at(i);
    }
    vector<vector<int>> children(N);
    for (int i = 1; i < N; i++) {
        int parent = P.at(i);
        children.at(parent).push_back(i);
    }
    vector<int> ans(N, -1);
    for (int i = 0; i < N; i++) {
        cout << rec(i,children, ans) << endl;
    }
}
