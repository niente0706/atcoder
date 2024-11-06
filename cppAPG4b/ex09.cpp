#include <bits/stdc++.h>
#include <atcoder/all>

using namespace std;
using namespace atcoder;

int main() {
    int x, a, b;
    cin >> x >> a >> b;

    x++;
    cout << x << endl;
    x *= (a + b);
    cout << x << endl;
    x *= x;
    cout << x << endl;
    x--;
    cout << x << endl;
}
