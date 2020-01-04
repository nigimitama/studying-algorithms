#include <bits/stdc++.h>
using namespace std;
// 解説みたがWA
int median(vector<int> v) {
    int size = v.size();
    vector<int> _v(v.size());
    copy(v.begin(), v.end(), back_inserter(_v));
    int tmp;
    for (int i = 0; i < size - 1; i++){
        for (int j = i + 1; j < size; j++) {
            if (_v[i] > _v[j]){
                tmp = _v[i];
                _v[i] = _v[j];
                _v[j] = tmp;
            }
        }
    }
    if (size % 2 == 1) {
        return _v[(size - 1) / 2];
    } else {
        return (_v[(size / 2) - 1] + _v[size / 2]) / 2;
    }
}

int main() {
    int n;
    cin >> n;

    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a.at(i);
    }

    // 解説によれば絶対誤差を最小化するのはmedianらしい
    vector<int> B(n);
    for (int i = 0; i < n; i++) {
        B.at(i) = a.at(i) - (i+1);
    }
    int b = median(B);

    int s = 0;
    for (int i = 0; i < n; i++) {
        s += abs(a.at(i) - (b + i+1));
    }
    cout << s << endl;
}



//  memo: mean vs median

// int median(vector<int> v) {
//     int size = v.size();
//     vector<int> _v(v.size());
//     copy(v.begin(), v.end(), back_inserter(_v));
//     int tmp;
//     for (int i = 0; i < size - 1; i++){
//         for (int j = i + 1; j < size; j++) {
//             if (_v[i] > _v[j]){
//                 tmp = _v[i];
//                 _v[i] = _v[j];
//                 _v[j] = tmp;
//             }
//         }
//     }
//     if (size % 2 == 1) {
//         return _v[(size - 1) / 2];
//     } else {
//         return (_v[(size / 2) - 1] + _v[size / 2]) / 2;
//     }
// }

// int mean(vector<int> v) {
//     int size = v.size();
//     int sum = 0;
//     for (int i = 0; i < size; i++){
//         sum += v[i];
//     }
//     return sum / size;
// }

// int main() {
//     int n;
//     cin >> n;

//     vector<int> a(n);
//     for (int i = 0; i < n; i++) {
//         cin >> a.at(i);
//     }

//     vector<int> b(n);
//     for (int i = 0; i < n; i++) {
//         b.at(i) = a.at(i) - i;
//     }
//     int b_mean = mean(b);
//     int b_median = median(b);
//     cout << b_mean << endl;
//     cout << b_median << endl;

// }









// WA
// int main() {
//     int n;
//     cin >> n;

//     vector<int> a(n);
//     for (int i = 0; i < n; i++) {
//         cin >> a.at(i);
//     }

//     int min_s = pow(10, 9);
//     for (int b = -n; b <= n; b++) {
//         int s = 0;
//         for (int i = 0; i < n; i++) {
//             s += abs(a.at(i) - (b + i+1));
//         }
//         if (s < min_s) {
//             min_s = s;
//         }
//     }
//     cout << min_s << endl;
// }



// int main() {
//     int n;
//     cin >> n;

//     vector<int> a(n);
//     for (int i = 0; i < n; i++) {
//         cin >> a.at(i);
//     }

//     // (1 + 2 + ... + n) / n
//     int mean_i = (n-1);
//     int sum_a = 0;
//     for (int i = 0; i < n; i++) {
//         sum_a += a.at(i);
//     }
//     int mean_a = sum_a / n;
//     int b = mean_a - mean_i;
//     cout << b << endl;

//     int s = 0;
//     for (int i = 0; i < n; i++) {
//         s += abs(a.at(i) - (b + i+1));
//     }
//     cout << s << endl;
// }

