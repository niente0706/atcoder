#include <bits/stdc++.h>
using namespace std;

int main () {
    int N;
    vector<pair<int, int>> acc;
    cin >> N;
    for (int i = 0; i < N; i++) {
        int a, b;
        cin >> a >> b;
        acc.push_back(make_pair(b, a));
    }
    sort(acc.begin(), acc.end());
    
    for (int i = 0; i < N; i++) {
        cout << acc.at(i).second << ' ' << acc[i].first << endl;
    }
}