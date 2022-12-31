#include <bits/stdc++.h>
using namespace std;

int N;
int K;
int dp[100001];

int main(void) {
    ios::sync_with_stdio(0); cin.tie(0);
    cin >> N >> K;
    
    fill(dp, dp+100001, -1);

    queue <int> Q;
    dp[N] = 0;
    Q.push(N);
    
    while(dp[K] == -1) {
        int value = Q.front(); Q.pop();

        vector<int> vec;
        vec.push_back(value-1);
        vec.push_back(value+1);
        vec.push_back(value*2);

        for(int v: vec) {
            if (v < 0 || v > 100000) continue;
            if (dp[v] != -1) continue;
            dp[v] = dp[value] + 1;
            Q.push(v);
        }
    }
    cout << dp[K];
}
