#include <bits/stdc++.h>
using namespace std;

int main() {
    vector<int> a(3);
    for (int i = 0; i < 3; i++) {
        cin >> a.at(i);
    }
    sort(a.begin(), a.end());

    int s = 0;
    for (int i = 1; i >= 0; i--) {
        int j = i + 1;
        s += abs(a.at(j) - a.at(i));
    }
    cout << s << endl;
}