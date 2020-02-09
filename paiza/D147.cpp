#include <bits/stdc++.h>
using namespace std;

int main() {
    int s;
    vector<int> a(4);
    cin >> s;
    for (int i=0; i < 4; i++) {
        cin >> a.at(i);
    }
    int min_a = 51;
    for (int i=0; i < 4; i++) {
        if (min_a > a.at(i)) {
            min_a = a.at(i);
        }
    }
    cout << min_a*s << endl;
}