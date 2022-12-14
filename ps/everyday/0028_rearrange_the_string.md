반복된 알파벳으로 이루어진 문자배열이 주어지면 연속으로 중복된 알파벳이 없도록 문자배열을 재배열하여 리턴하시오. 
불가능 하다면 empty string을 리턴하시오.



Given a string with repeated characters, rearrange the string so that no two adjacent characters are the same. 
If this is impossible, return an empty string.


```
input: "aaabbc"
output: "ababac"

input: "aaac"
output: ""
```

```javascript
class PriorityQueue { // MaxHeap
  constructor() {
    this.heap = []
  }

  compare(a, b) {
    if (a.priority === b.priority) {
      return b.key.charCodeAt() - a.key.charCodeAt()
    }

    return a.priority - b.priority
  }


  isEmpty() {
    return this.heap.length < 1
  }

  size() {
    return this.heap.length
  }

  push(value) {
    this.heap.push(value)
    this.upHeap()
  }

  pop() {
    if (this.isEmpty()) { return null }

    const result = this.heap[0]
    const end = this.heap.pop()
    if (this.heap.length > 0) {
      this.heap[0] = end
      this.downHeap()
    }

    return result
  }


  upHeap() {
    let idx = this.heap.length - 1
    while (idx > 0) {
      const elem = this.heap[idx]
      const parentIdx = Math.floor((idx + 1) / 2) - 1
      const parentElem = this.heap[parentIdx]

      if (this.compare(elem, parentElem) < 0) {
        break
      }

      this.heap[idx] = parentElem
      this.heap[parentIdx] = elem
      idx = parentIdx
    }
  }

  downHeap(idx = 0) {
    const rightChild = idx * 2 + 2
    const leftChild = idx * 2 + 1
    const elem = this.heap[idx]
    const length = this.heap.length - 1

    let targetIdx = idx
    if (leftChild <= length && this.compare(elem, this.heap[leftChild]) < 0) {
      targetIdx = leftChild
    }

    if (rightChild <= length && this.compare(this.heap[targetIdx], this.heap[rightChild]) < 0) {
      targetIdx = rightChild
    }

    if (targetIdx !== idx) {
      this.heap[idx] = this.heap[targetIdx]
      this.heap[targetIdx] = elem
      this.downHeap(targetIdx)
    }
  }
}

function solve(input) {
  const pq = new PriorityQueue()

  const frequencyMap = {}
  for (const value of input) {
    if (frequencyMap[value] === undefined) {
      frequencyMap[value] = 0
    }

    frequencyMap[value] += 1
  }

  const entries = Object.entries(frequencyMap)
  for (const [key, priority] of entries) {
    pq.push({ key, priority })
  }

  let result = ''


  while(pq.size() > 1) {
    const p = pq.pop()
    const q = pq.pop()

    result += p.key + q.key

    if (--p.priority) {
      pq.push({ key: p.key, priority: p.priority })
    }

    if (--q.priority) {
      pq.push({ key: q.key, priority: q.priority })
    }
  }

  const elem = pq.pop()
  if (!elem) {
    return result
  }

  return elem.priority === 1 ? result + elem.key : ''
}

const data = [
  { input: 'aaabbc', expected: 'ababac' },
  { input: 'aaaabbca', expected: '' },
  { input: 'aaac', expected: '' },
  { input: 'ab', expected: 'ab' },
  { input: 'ccaa', expected: 'acac' },
  { input: 'aaabbbccc', expected: 'abcabcabc' },
  { input: 'abc', expected: 'abc' },
  { input: 'a', expected: 'a' },
]

data.forEach(({ input, expected }) => {
  const actual = solve(input)
  if (actual !== expected) {
    throw new Error(`wrong answer: ${actual}, ${expected}`)
  }
})
```
