#include <bits/stdc++.h>
using namespace std;


bool is_all_even(vector<int> A) {
    bool is_all_even_ = true;
    bool is_even;
    for (int i=0; i < A.size(); i++) {
        is_even = (A.at(i) % 2 == 0);
        is_all_even_ = is_all_even_ && is_even;
        if (!is_all_even_) {
            break;
        }
    }
    return is_all_even_;
}

 
int main() {
    int N;
    vector<int> A(N);
    for (int i = 0; i < N; i++) {
        cin >> A.at(i);
    }
    for (int i = 0; i < N; i++) {
        cout << A.at(i) << endl;
    }
    // int N = 3;
    // vector<int> A = { 8 , 12, 40 };
    // int count = 0;
    // while (is_all_even(A)) {
    //     for (int i = 0; i < N; i++) {
    //         A.at(i) /= 2;
    //     }
    // }
    // cout << count << endl;
}