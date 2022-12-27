#include <bits/stdc++.h>
using namespace std;

int N;
int dp[50001];

int main(void) {
    ios::sync_with_stdio(0); cin.tie(0);

    cin >> N;

    for(int i=1; i<=N; i++) {
      dp[i] = 4;

      for(int j=1; j * j <= i; j++) {
        dp[i] = min(1 + dp[i - j * j], dp[i]);
      }
    }

    cout << dp[N];
}
