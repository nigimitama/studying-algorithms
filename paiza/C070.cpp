#include <bits/stdc++.h>
#include <map>
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

map<int, int> count(vector<int> v) {
    map<int, int> counts;
    for (int i = 0; i < v.size(); i++) {
        counts[v.at(i)] += 1;
    }
    return counts;
}


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
        // TODO: count pair
        return "Two Pair";
    } else if (max_counts == 2) {
        return "One Pair";
    } else {
        return "No Pair";
    }
}

int main() {
    vector<int> v = {2,3,4};
    map<int, int> c = count(v);
    for (int i=0; i<c.size(); i++) {
        cout << c.at(i) << endl;
    }
    // int n;
    // cin >> n;
    // string cards;
    // for (int i=0; i<n; i++) {
    //     cin >> cards;
    //     cout << detect(cards) << endl;
    // }
}