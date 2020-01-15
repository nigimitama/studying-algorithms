#include <bits/stdc++.h>
using namespace std;

// # 文字列の型変換全然うまくいかない。あきらめた

int ctoi(const char c){
  if('0' <= c && c <= '9') return (c-'0');
  return -1;
}

int func(string N) {
    int total = 0;
    for (int i = 0; i < N.size(); i++) {
        total += ctoi(N.at(i));
    }
    return total;
}


int main() {
    string N;
    if (stoi(N) % func(N) == 0) {
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }
}
