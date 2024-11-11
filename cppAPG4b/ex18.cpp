#include <bits/stdc++.h>
// #include <atcoder/all>
using namespace std;
// using namespace atcoder;

int main() {
    int N, M;
    cin >> N >> M;
    vector<vector<char>> match(N, vector<char>(N, '-'));
    for (int i = 0; i < M; i++) {
        int a, b;
        cin >> a >> b;
        a--; b--;
        match.at(a).at(b) = 'o';
        match.at(b).at(a) = 'x';
    }
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cout << match.at(i).at(j);
            if (j < N - 1) {
                cout << " ";
            }
        }
        cout << endl;
    }
}
