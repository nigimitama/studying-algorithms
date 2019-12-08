#include <bits/stdc++.h>
using namespace std;

int main() {
    float a, b;
    cin >> a >> b;
    float x = (a + b) / 2;
    int integer = floor(x);
    float decimal = x - integer;
    if (decimal != 0) {
      cout << integer + 1 << endl;
    } else {
      cout << integer << endl;
    }
}
