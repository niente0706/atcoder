#include <bits/stdc++.h>
using namespace std;

int main () {
    int N;
    cin >> N;
    vector<int> A(N);
    for (int i = 0; i < N; i++) {
        cin >> A.at(i);
    }
    
    unordered_map<int, int> Count;
    for (int x : A) {
        if (Count.count(x)) {
            Count.at(x)++;
        }
        else {
            Count[x] = 1;
        }
    }
    
    int count_max = 0, x_max = -1;
    for (pair<int, int> p : Count) {
        int x = p.first;
        int count = p.second;
        if (count > count_max) {
            x_max = x;
            count_max = count;
        }
    }
    
    cout << x_max << ' ' << count_max << endl;
}
