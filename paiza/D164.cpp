#include <bits/stdc++.h>
using namespace std;

int main() {
    int x;
    cin >> x;
    float y = x;
    while (y > 2) {
        y = y / 2;
    }
    if (y == 2) {
        cout << "OK" << endl;
    } else {
        cout << "NG" << endl;
    }
}