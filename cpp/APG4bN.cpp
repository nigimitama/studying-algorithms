#include <bits/stdc++.h>
using namespace std;

int main()
{
    int N;
    cin >> N;

    vector<int> math(N);
    vector<int> english(N);
    for (int i = 0; i < N; i++)
    {
        cin >> math.at(i);
        cin >> english.at(i);
        cout << math.at(i) + english.at(i) << endl;
    }
}
