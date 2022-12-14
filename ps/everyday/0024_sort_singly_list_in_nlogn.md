## Sort the list in O(nlogn) time complexity
단방향 연결 리스트(singly linked list)가 주어지면 O(nlogn) 시간복잡도로 정렬하시오

Given a singly linked list, sort the list in O(nlogn) time complexity.

```javascript
function Node(value) {
  this.value = value
  this.next = null
}

Node.prototype.toString = function() {
  let temp = this
  let result = []
  while(temp) {
    result.push(temp.value)
    temp = temp.next
  }
  return result.join(',')
}

function makeSinglyLinkedList(values) {
  if (values.length <= 0) {
    return null
  } else {
    const value = new Node(values.shift())
    const next = makeSinglyLinkedList(values)
    value.next = next
    return value
  }
}

function getMiddleNode(head) {
  if (!head) return head
  let slow = head
  let fast = head
  let prev = null
  while(fast && fast.next) {
    prev = slow
    slow = slow.next
    fast = fast.next.next
  }
  prev.next = null
  return slow
}

function merge(left, right) {
  let merged = new Node()
  let mHead = merged

  while(left && right) {
    if (left.value > right.value) {
      mHead.next = right
      right = right.next
    } else {
      mHead.next = left
      left = left.next
    }
    mHead = mHead.next
  }

  mHead.next = left ? left : right
  return merged.next
}

function mergeSort(head) {
  if (!head || !head.next) return head
  const mid = getMiddleNode(head)
  return merge(mergeSort(head), mergeSort(mid))
}

const data = [
  { input: [3,1,5,6], expected: [1,3,5,6] },
  { input: [6,5,4,3,2,1], expected: [1,2,3,4,5,6] },
  { input: [6,3,1,2,5,4], expected: [1,2,3,4,5,6] }
]

data.forEach(({input, expected}) => {
  const linkedList = makeSinglyLinkedList(input)
  const sortedList = mergeSort(linkedList)
  if (sortedList.toString() !== expected.join(',')) {
    throw new Error('wrong answer')
  }
})
```
