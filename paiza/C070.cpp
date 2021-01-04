#include <bits/stdc++.h>
using namespace std;


int max(vector<int> v) {
    int max_v = 0;
    for (int i = 0; i < v.size(); i++) {
        if (v.at(i) > max_v) {
            max_v = v.at(i);
        }
    }
    return max_v;
}

vector<int> count(vector<int> v) {
    vector<int> counts(max(v));
    for (int i = 0; i < v.size(); i++) {
        counts(v.at(i)) += 1;
    }
    return counts;
}
// WIP/FIXME: エラー解決できず


string detect(string cards) {
    vector<int> counts(9);
    int card;
    for (int i = 0; i < cards.size(); i++) {
        card = cards.at(i);
        counts.at(card) += 1;
    }
    int max_counts = max(counts);
    if (max_counts == 4) {
        return "Four Card";
    } else if (max_counts == 3) {
        return "Three Card";
    } else if (max_counts == 2) {
        return "Two Pair";
    } else if (max_counts == 2) {
        return "One Pair";
    } else {
        return "No Pair";
    }
}

int main() {
    int n;
    cin >> n;
    string cards;
    for (int i=0; i<n; i++) {
        cin >> cards;
        cout << detect(cards) << endl;
    }
}