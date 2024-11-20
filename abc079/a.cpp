#include <bits/stdc++.h>
// #include <atcoder/all>
using namespace std;
// using namespace atcoder;

int main() {
    int N;
    cin >> N;

    int d1 = N / 1000, d2 = N / 100 % 10, d3 = N / 10 % 10, d4 = N % 10;
    if (d1 == d2 && d2 == d3 || d2 == d3 && d3 == d4) {
        cout << "Yes" << endl;
    }
    else {
        cout << "No" << endl;
    }
}
