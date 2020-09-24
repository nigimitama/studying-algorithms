#include <bits/stdc++.h>
using namespace std;

int main() {
    string s;
    cin >> s;
    bool is_same;
    bool has_same = false;
    for (int i=0; i < s.size(); i++) {
        for (int j=i; j < s.size(); j++) {
            if (i != j) {
                is_same = s.at(i) == s.at(j);
                if (is_same || has_same) {
                    has_same = true;
                }
            }
        }
    }
    if (has_same) {
        cout << "NG" << endl;
    } else {
        cout << "OK" << endl;
    }
    
}