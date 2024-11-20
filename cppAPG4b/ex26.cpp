#include <bits/stdc++.h>
using namespace std;

vector<int> operator+(vector<int> A, vector<int> B) {
    int la = A.size(), lb = B.size(), l = max(la, lb);
    vector<int> ret(l, 0);
    for (int i = 0; i < l; i++) {
        if (i < la) {
            ret[i] += A[i];
        }
        if (i < lb) {
            ret[i] += B[i];
        }
    }
    return ret;
}

vector<int> operator-(vector<int> A, vector<int> B) {
    int la = A.size(), lb = B.size(), l = max(la, lb);
    vector<int> ret(l, 0);
    for (int i = 0; i < l; i++) {
        if (i < la) {
            ret[i] += A[i];
        }
        if (i < lb) {
            ret[i] -= B[i];
        }
    }
    return ret;
}

int read_single_int(char chr, unordered_map<char, int> &var_int) {
    if (var_int.count(chr)) {
        return var_int[chr];
    }
    else {
        return int(chr - '0');
    }
}

int read_full_int(vector<char> vec, unordered_map<char, int> &var_int) {
    int N = vec.size(), val = read_single_int(vec.at(0), var_int);
    char op;
    int term;
    for (int i = 1; i < N; i += 2) {
        op = vec.at(i);
        term  = read_single_int(vec.at(i + 1), var_int);
        if (op == '+') {
            val += term;
        }
        else {
            val -= term;
        }
    }
    return val;
}

vector<int> read_single_vec(vector<char> vec, unordered_map<char, int> &var_int, unordered_map<char, vector<int>> &var_vec) {
    int N = vec.size();
    if (N == 1) {
        return var_vec[vec[0]];
    }
    vector<int> ret = {};
    vector<char> acc = {};
    int i = 1;
    while (i < N - 1) {
        if (vec.at(i) == ',') {
            ret.push_back(read_full_int(acc, var_int));
            acc = {};
        }
        else {
            acc.push_back(vec.at(i));
        }
        i++;
    }
    ret.push_back(read_full_int(acc, var_int));
    return ret;
}


vector<int> read_full_vec(vector<char> vec, unordered_map<char, int> &var_int, unordered_map<char, vector<int>> &var_vec) {
    int N = vec.size();
    unordered_set<char> operations = {'+', '-'};
    vector<char> acc = {};
    char elem;
    int i = 0;
    while (i < N) {
        elem = vec.at(i);
        if (operations.count(elem)) {
            break;
        }
        else {
            acc.push_back(elem);
        }
        i++;
    }
    vector<int> ret = read_single_vec(acc, var_int, var_vec);
    acc = {};
    char op;
    while (i < N) {
        op = vec.at(i);
        i++;
        while (i < N and ! operations.count(vec.at(i))) {
            acc.push_back(vec.at(i));
            i++;
        }
        vector<int> dvec = read_single_vec(acc, var_int, var_vec);
        acc = {};
        if (op == '+') {
            ret = ret + dvec;
        }
        else {
            ret = ret - dvec;
        }
    }
    return ret;
}

pair<string, vector<char>> full_order() {
    string order;
    cin >> order;
    vector<char> ret = {};
    char word;
    while (cin >> word) {
        if (word == ';') {
            break;
        }
        else {
            ret.push_back(word);
        }
    }
    return make_pair(order, ret);
}

int main() {
    int N;
    cin >> N;
    unordered_map<char, int> variables_int;
    unordered_map<char, vector<int>> variables_vec;
    
    for (int i = 0; i < N; i++) {
        string order;
        vector<char> order_contents;
        pair<string, vector<char>> input = full_order();
        tie(order, order_contents) = input;
        if (order == "int") {
            char key = order_contents.at(0);
            vector<char> int_expression = vector<char>(order_contents.begin() + 2, order_contents.end());
            int val = read_full_int(int_expression, variables_int);
            variables_int[key] = val;
        }
        else if (order == "print_int") {
            int val = read_full_int(order_contents, variables_int);
            cout << val << endl;
        }
       else if (order == "vec") {
           char key = order_contents.at(0);
           vector<char> vec_expression = vector<char>(order_contents.begin() + 2, order_contents.end());
           vector<int> val = read_full_vec(vec_expression, variables_int, variables_vec);
           variables_vec[key] =  val;
       }
       else {
           vector<int> val = read_full_vec(order_contents, variables_int, variables_vec);
           cout << "[ ";
           for (int x : val) {
               cout << x << " ";
           }
           cout << "]" << endl;
       }
    }
}
