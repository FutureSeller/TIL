#include <bits/stdc++.h>
using namespace std;

#define X first
#define Y second

int R;
int C;
string maze[1002];
int fire[1002][1002];
int jihoon[1002][1002];

int dx[4] = {0,0,-1,1};
int dy[4] = {-1,1,0,0};

int main(void){
  ios::sync_with_stdio(0); cin.tie(0);
  cin >> R >> C;

  for(int i=0; i<R; i++) {
    fill(fire[i], fire[i] + C + 1, -1);
    fill(jihoon[i], jihoon[i] + C + 1, -1);
  }

  for(int i=0; i<R; i++) cin >> maze[i];

  queue <pair<int, int> > f_q;
  queue <pair<int, int> > j_q;

  for(int i=0; i<R; i++) {
    for(int j=0; j<C; j++) {
      if(maze[i][j] == 'F') {
        f_q.push(make_pair(i, j));
        fire[i][j] = 0;
      }
      if(maze[i][j] == 'J') {
        j_q.push(make_pair(i, j));
        jihoon[i][j] = 0;
      }
    }
  }

  while(!f_q.empty()) {
    auto cur = f_q.front(); f_q.pop();
    
    for(int i=0; i<4; i++) {
      int nx = dx[i] + cur.X;
      int ny = dy[i] + cur.Y;

      if (nx < 0 || nx >= R || ny < 0 || ny >= C) continue;
      if (maze[nx][ny] == '#' || fire[nx][ny] >= 0) continue;

      fire[nx][ny] = fire[cur.X][cur.Y] + 1;
      f_q.push(make_pair(nx, ny));
    }
  }

  while(!j_q.empty()) {
    auto cur = j_q.front(); j_q.pop();
    if (cur.X == 0 || cur.X == R-1 || cur.Y == 0 || cur.Y == C-1) {
      cout << jihoon[cur.X][cur.Y] + 1;
      return 0;
    }   

    for(int i=0; i<4; i++) {
      int nx = dx[i] + cur.X;
      int ny = dy[i] + cur.Y;

      if (nx < 0 || nx >= R || ny < 0 || ny >= C) continue;
      if (maze[nx][ny] == '#' || jihoon[nx][ny] >= 0) continue;
      if (fire[nx][ny] >= 0 && (fire[nx][ny] <= jihoon[cur.X][cur.Y] + 1)) continue;

      jihoon[nx][ny] = jihoon[cur.X][cur.Y] + 1;
      j_q.push(make_pair(nx, ny));
    }
  }

  cout << "IMPOSSIBLE";
}

