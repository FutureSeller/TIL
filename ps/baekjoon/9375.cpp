#include <bits/stdc++.h>
using namespace std;

int T;

int main(void) {
    ios::sync_with_stdio(0); cin.tie(0);

    cin >> T;
    while (T--) {
      int N;
      cin >> N;

      string a, b;
      map<string, int> hash_tab;

      int idx = 0;
      while (idx++ < N) {
        cin >> a >> b;
        hash_tab[b]++;
      }

      int answer = 1;
      for(auto it = hash_tab.begin(); it != hash_tab.end(); it++) {
        answer *= (it->second + 1);
      }

      cout << answer - 1 << "\n";
    }
}