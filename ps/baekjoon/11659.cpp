#include <bits/stdc++.h>
using namespace std;

int N;
int M;
long long values[100001];

int main(void) {
    ios::sync_with_stdio(0); cin.tie(0);

    cin >> N >> M;

    int idx = 1;
    while(idx <= N) {
      int v;
      cin >> v;
      values[idx] = v + values[idx-1];
      idx++;
    }

    while(M--) {
      int left, right;
      cin >> left >> right;
      cout << values[right] - values[left-1] << "\n";
    } 
}
