#include <bits/stdc++.h>
using namespace std;

#define X first
#define Y second

string board[101];
int visited[101][101];
int N;

int dx[4] = {-1,1,0,0};
int dy[4] = {0,0,-1,1};

void reset() {
    for(int i=0; i<N; i++)
        for(int j=0; j<N; j++)
            visited[i][j] = 0;
}

void bfs(int r, int c, char base) {
    queue <pair<int, int> > Q;
    visited[r][c] = 1;
    Q.push(make_pair(r, c));
    
    while(!Q.empty()) {
        auto cur = Q.front(); Q.pop();
        for(int i=0; i<4; i++) {
            int nx = dx[i] + cur.X;
            int ny = dy[i] + cur.Y;
            
            if(nx < 0 || nx >= N || ny < 0 || ny >= N) continue;
            if(board[nx][ny] != base) continue;
            if(visited[nx][ny]) continue;
            
            visited[nx][ny] = 1;
            Q.push(make_pair(nx, ny));
        }
    }
}

int solve() {
    int answer = 0;
    for(int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            if(visited[i][j] == 0) {
                answer++;
                bfs(i, j, board[i][j]);
            }
        }
    }
    return answer;
}

int main(void) {
    ios::sync_with_stdio(0); cin.tie(0);
    cin >> N;
    
    for(int i=0; i<N; i++) cin >> board[i];
    
    cout << solve() << " ";
    
    for(int i=0; i<N; i++)
        for(int j=0; j<N; j++)
            if (board[i][j] == 'G') board[i][j] = 'R';
    
    reset();
    cout << solve();
}
