#include <bits/stdc++.h>
using namespace std;

int main() {
    string s;
    int n;
    cin >> s;
    cin >> n;
    cout << s.substr(0,n-1)+s.substr(n) << endl;
}