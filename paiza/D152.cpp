#include <bits/stdc++.h>
using namespace std;

int main() {
    string s;
    int n, count;
    cin >> s;
    cin >> n;
    count = 0;
    for (int i = 0; i < 5; i++) {
        if (s.at(i) == 'R') {
            count += 1;
        }
    }
    if (count >= n) {
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }
}