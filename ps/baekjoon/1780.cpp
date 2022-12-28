#include <bits/stdc++.h>
using namespace std;

int N;
int board[2187][2187];

int M;
int Z;
int O;

int traverse(int r, int c, int size) {
  if (size == 1) {
    return board[r][c];
  }

  int gap = size / 3;

  vector<int> values;

  for(int row=r; row<r+size; row += gap) {
    for(int col=c; col<c+size; col += gap) {
      values.push_back(traverse(row, col, gap));
    }
  }

  int m_count = count(values.begin(), values.end(), -1);
  int z_count = count(values.begin(), values.end(), 0);
  int o_count = count(values.begin(), values.end(), 1);

  if (m_count == 9) return -1;
  if (z_count == 9) return 0;
  if (o_count == 9) return 1;

  for(auto &v: values) {
    if (v == 1) O++;
    else if (v == -1) M++;
    else if (v == 0) Z++;
  }

  return -2;
}


int main(void) {
    ios::sync_with_stdio(0); cin.tie(0);
    
    cin >> N;

    for(int i=0; i<N; i++) {
      for(int j=0; j<N; j++) {
        cin >> board[i][j];
      }
    }

    int value = traverse(0, 0, N);
    if (value == 1) O++;
    else if (value == -1) M++;
    else if (value == 0) Z++;

    cout << M << "\n";
    cout << Z << "\n";
    cout << O << "\n";
}
