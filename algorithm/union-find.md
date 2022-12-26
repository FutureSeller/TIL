# Union-Find, Disjoint-set, 서로소 집합

- 서로소 집합(서로 중복되지 않는 부분 집합들)을 표현하는 자료구조, 부분 집합들의 합집합이 곧 전체집합임.

## 필요한 연산

- `init()`: 초기화. 각각의 원소를 유일한 집합으로 만드는 연산
- `find(x)`: 요소 x가 어느 부분집합에 속해있는지 확인하는 연산. 집합의 대표값을 반환함.
- `uni(x, y)`: 각각의 요소가 속한 부분집합을 합하는 연산

## 배열로 표현하기

```c++
int parent[51];

void init() {
  for(int i=0; i<51; i++) {
    parent[i] = i;
  }
}

int find(int x) {
  if (parent[x] == x) return x;
  else return find(parent[x]);
}

void uni(int x, int y) {
  x = find(x);
  y = find(y);
  parent[x] = y;
}

// 최악의 경우를 생각해보자. 1 -> 2 -> 3 -> 4 -> 5; find(1) --> 5가 되기까지 4번을 거침
// find를 사용했을 때, 경로 압축을 사용함; find(1) 하면, parent[4] = parent[3] = parent[2] = parent[1] = 5;
int find(int x) {
  if (parent[x] == x) return x;
  else parent[x] = find(parent[x]);
}
```

## Union-by-rank (Union-by-height)

- rank에 트리의 높이를 저장함. 항상 높이가 더 낮은 트리를 높은 트리 밑에 넣음.
- 배열로 표현하기에서 의문이였던 것은, `uni` 함수의 합집합연산에서 `parent`의 인덱스로 어떤 값이 들어가야할까? 였다.
  - x, y의 위치를 바꿔서 (= 부분 집합의 대표값을 바꿔도 되는데) 좀 더 나은 방법이 있을까?
  - find 연산을 조금 더 효율적으로 취할 수 있을 것 같은데?

```c++
int rank[51], size[51];

void init() {
  for(int i=0 i<51; i++) {
    parent[i] = i;
    rank[i] = 1;
    size[i] = 0;
  }
}

void uni(int x, int y) {
  x = find(x);
  y = find(y);

  if (rank[x] == rank[y]) {
    rank[x]++;
    parent[y] = x;
  }
  // y가 더 깊은 depth를 가지는 경우. x를 y의 subset으로 만듬. (대표값을 y로 바꾸는 거니까)
  // 깊이가 더 짧은 쪽을 하위에 넣는게, find를 사용했을때 비용을 줄일 수 있음.
  else if (rank[x] < rank[y]) {
    parent[x] = y;
    size[y] += size[x];
  } else {
    parent[y] = x;
    size[x] += size[y];
  }
}
```

## 활용되는 곳

- Connectivity example: p -> q를 연결하는 경로가 존재하는가?
- 소셜 네트워크에서 친구관계 표현
- 컴퓨터들의 네트워크 표현

---

## Reference

- https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2012/dbbca5218779336114dcd3b3195e7783_MIT6_046JS12_lec16.pdf
