# Selection Sort
- pros
  - performs well on a small list
  - in-place sorting
  - Space complexity: O(1)
- cons
  - poor efficiency when dealing with a huge list of items
  - Time complexity: O(n^2)
- "only suitable for a list of few elements that are in random order"

## How it works 
1. 주어진 리스트 중 최소 값을 찾는다.
2. 그 값을 맨 앞에 위치한 값과 교체한다.
3. 맨 처음 위치를 뺀 나머지 리스트를 같은 방법으로 교체한다.

``` python
def selection_sort(array):
  for i in range(len(array)-1):
    indexMin = i
    for j in range(i+1, len(array)):
      if x[indexMin] > x[j]:
        indexMin = j
    x[i], x[indexMin] = x[indexMin], x[i]
  return array
```

## Questions
- Q1. 왜 random order 일 때 더 이득인가?
  - 정렬된 여부와 상관 없이 최솟값을 찾기위해 어차피 한 round를 돌기때문
- Q2. Selection Sort는 Stable한가?
  - no. unstable.
  - input: [{3, 'kim'}, {3, 'lee'}, {1, '...'}]
  - output: [{1, '...'}, {3, 'lee'}, {3, 'kim'}]

---
## Reference
- https://sciencing.com/the-advantages-disadvantages-of-sorting-algorithms-12749529.html
- https://ko.wikipedia.org/wiki/%EC%84%A0%ED%83%9D_%EC%A0%95%EB%A0%AC
