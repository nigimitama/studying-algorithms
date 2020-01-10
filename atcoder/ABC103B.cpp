#include <bits/stdc++.h>
using namespace std;

int main() {
    string s, t;
    cin >> s;
    cin >> t;

    bool flag = false;
    int n = s.size();
    if (s == t) {
        flag = true;
    }
    for (int i = 0; i < n; i++){
        s = s.at(n-1) + s.substr(0, n-1);
        if (s == t) {
            flag = true;
        }
    }
    if (flag == false) {
        cout << "No" << endl;
    } else {
        cout << "Yes" << endl;
    }
}