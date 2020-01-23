#include <bits/stdc++.h>
using namespace std;

int main() {
    string a = "aiueo";
    string s;
    cin >> s;
    bool is_ok;

    string d = "";
    for (int i=0; i < s.size(); i++) {
        is_ok = true;
        for (int j=0; j < a.size(); j++) {
            if (s.at(i) == a.at(j)) {
                is_ok = false;
            }
        }
        if (is_ok == true) {
            d += s.at(i);
        }
    }
    cout << d << endl;
}