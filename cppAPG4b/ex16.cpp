#include <bits/stdc++.h>
// #include <atcoder/all>
using namespace std;
// using namespace atcoder;

int main() {
    int A, last = -1;
    for (int i = 0; i < 5; i++){
        cin >> A;
        if (A == last) {
            cout << "YES" << endl;
            return 0;
        }
        else {
            last = A;
        }
    }
    cout << "NO" << endl;
    return 0;
}
