#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    if (N == 0) {
        cout << 2 << endl;
        return 0;
    }
    else if (N == 1) {
        cout << 1 << endl;
        return 0;
    }
    
    vector<long long> luca(N + 1);
    luca.at(0) = 2;
    luca.at(1) = 1;
    for (int i = 2; i <= N; i++) {
        luca.at(i) = luca.at(i - 1) + luca.at(i - 2);
    }
    
    cout << luca.at(N) << endl;
}