# Sort an array with million integers.

백만개의 정수가 들어있는 배열을 가장 빨리 정렬하시오. 모든 정수는 1조보다 작습니다.

힌트) 퀵소트 아님.

Sort an array with million integers.

```javascript
// radix sort
function solve(array) {
  const maxValue = Math.max.apply(null, array)

  for (let exponential = 10; maxValue / exponential > 0; exponential *= 10) {
    const bucket = new Array(10)
    for (const value of array) {
      const mod = value % exponential
      if (bucket[mod] === undefined) {
        bucket[mod] = []
      }

      bucket[mod].push(value)
    }

    let position = 0
    for (const entry of bucket) {
      while (entry && entry.length > 0) {
        array[position++] = entry.shift()
      }
    }
  }

  return array
}
```
