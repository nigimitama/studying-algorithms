#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a.at(i);
    }

    int tmp, d = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            tmp = abs(a.at(i) - a.at(j));
            if (tmp > d) {
                d = tmp;
            }
        }
    }
    cout << d << endl;
}