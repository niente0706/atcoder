#include <bits/stdc++.h>
// #include <atcoder/all>
using namespace std;
// using namespace atcoder;

int main() {
    char A, B, C, D;
    cin >> A >> B >> C >> D;
    int base = (int)'0';
    int a = (int)A - base, b = (int)B - base, c = (int)C - base, d = (int)D - base;
    
    if (a + b + c + d == 7) {
        cout << a << '+' << b << '+' << c << '+' << d << "=7";
    }
    else if (a + b + c - d == 7) {
        cout << a << '+' << b << '+' << c << '-' << d << "=7";
    }
    else if (a + b - c + d == 7) {
        cout << a << '+' << b << '-' << c << '+' << d << "=7";
    }
    else if (a - b + c + d == 7) {
        cout << a << '-' << b << '+' << c << '+' << d << "=7";
    }
    else if (a + b - c - d == 7) {
        cout << a << '+' << b << '-' << c << '-' << d << "=7";
    }
    else if (a - b + c - d == 7) {
        cout << a << '-' << b << '+' << c << '-' << d << "=7";
    }
    else if (a - b - c + d == 7) {
        cout << a << '-' << b << '-' << c << '+' << d << "=7";
    }
    else if (a - b - c - d == 7) {
        cout << a << '-' << b << '-' << c << '-' << d << "=7";
    }
}
