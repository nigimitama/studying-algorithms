#include <bits/stdc++.h>
using namespace std;

int main() {
    string s = "1234";
    bool is_same;
    bool has_same = false;
    for (int i=0; i < s.size(); i++) {
        for (int j=i; j < s.size(); j++) {
            cout << "s.at(i): "+s.at(i) << endl;
            cout << "s.at(j): "+s.at(j) << endl;

            is_same = s.at(i) == s.at(j);
            if (is_same || has_same) {
                has_same = true;
            }
        }
    }
    if (has_same) {
        cout << "NG" << endl;
    } else {
        cout << "OK" << endl;
    }
    
}