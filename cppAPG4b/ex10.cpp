#include <bits/stdc++.h>
#include <atcoder/all>

using namespace std;
using namespace atcoder;

int main() {
    int A, B;
    cin >> A >> B;

    string a = "", b = "";
    int i = 0, j = 0;
    while (i < A) {
        a += "]";
        i++;
    }
    while (j < B) {
        b += "]";
        j++;
    }

    cout << "A:" << a << endl;
    cout << "B:" << b << endl;
}
