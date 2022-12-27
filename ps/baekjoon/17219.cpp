#include <bits/stdc++.h>
using namespace std;

int N;
int M;
map<string, string> hash_table;

int main(void) {
    ios::sync_with_stdio(0); cin.tie(0);

    cin >> N >> M;
    while (N--) {
        string a, b;
        cin >> a >> b;
        hash_table[a] = b;
    }

    while (M--) {
        string a;
        cin >> a;
        cout << hash_table[a] << "\n";
    }
}