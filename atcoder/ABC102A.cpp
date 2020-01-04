#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, y;
    cin >> N;
    if (N % 2 == 0) {
        y = N;
    } else {
        y = 2*N;
    }
    cout << y << endl;
}