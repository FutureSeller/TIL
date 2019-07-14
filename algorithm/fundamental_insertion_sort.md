# Insertion Sort
- pros
  - simple implementation
  - performs well on a small list
  - most efficient that other simple quadratic algorithms(selection, bubble)
  - in-place sorting
  - stable
  - Space complexity: O(1)
- cons
  - poor efficiency when dealing with a huge list of items
  - Time complexity: O(n^2)

## How it works 
0. 오름차순이라고 가정
1. 특정 index에 위치한 값이 특정 범위 내에서 가장 작은 값이여야함
2. 1을 풀어서 말하자면 [start..end]는 이미 정렬된 상태
3. 정렬된 상태의 [start..end]를 유지하기 위해, 가장 큰 값부터 작은 값이 나올때까지 swap

``` python
def insertion_sort(array):
  for i in range(1, len(array)):
    j = i - 1
    key = array[i]
    while array[j] > key and j >= 0:
      x[j+1] = x[j]
      j -= 1
    x[j+1] = key
  return array
```

## Questions
#### Insertion Sort vs. Selection Sort?
- 모든 키가 정렬된 상황이라면
  - insertion sort: O(N)
  - selection sort: O(N^2)
  - Why? inner loop
    - selection sort: unsorted elements
    - insertion sort: sorted elements
- Write (Swap)이 매우매우매우 비싼 연산이라면?
  - insertion < selection 일 수도 있음
  - selection은 swap을 n번만 하기 때문

---
## Reference
- https://ko.wikipedia.org/wiki/%EC%82%BD%EC%9E%85_%EC%A0%95%EB%A0%AC
