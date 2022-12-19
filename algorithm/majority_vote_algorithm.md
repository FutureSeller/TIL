# Majority Vote Algorithm

> This algorithm, which Bob Boyer and I invented in 1980 decides which element of a sequence is in the majority, provided there is such an element. How would you determine the majority element of sequence.

즉, 사람들이 투표를 했을 때 과반의 표를 받은 대상이 있는지 어떤 대상인지 밝혀내는 방법. 시간 복잡도는 O(N), 공간 복잡도를 O(1)로 풀 수 있다.

다만, 항상 배열 내에 과반수가 넘는 원소가 존재한다는 보장되어있어야한다.

```python
def find_majority(nums):
  major, count = num[0], 0
  for num in nums:
    if num == major:
      count += 1
    elif count == 0:
      major, count = num, 1
    else:
      count -= 1
  return major
```

적절한 예시가 무엇이 있을까 고민해보다가, [링크](https://sgc109.github.io/2020/11/30/boyer-moore-majority-vote-algorithm/)의 글을 발견했고, 증명 부분에 잘 정의되어있다.

---

## Reference

- https://www.cs.utexas.edu/~moore/best-ideas/mjrty/
