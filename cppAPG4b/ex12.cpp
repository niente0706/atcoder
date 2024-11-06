#include <bits/stdc++.h>
using namespace std;

int main() {
    string S;
    cin >> S;
    int ans = 1, N = S.size();

    for (int i = 0; i < N; i++) {
        if (i % 2 == 1) {
            if (S[i] == '+') {
                ans++;
            }
            else {
                ans--;
            }
        }
    }
    cout << ans << endl;
}
