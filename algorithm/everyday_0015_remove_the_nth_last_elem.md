## Remove the Nth last element and return the head node

링크드 리스트(linked list)의 머리 노드(head node)와 정수 N이 주어지면, 끝에서 N번째 노드(node)를 제거하고 머리 노드(head node)를 리턴하시오.

단, 리스트를 한번만 돌면서 풀어야합니다. N은 리스트 길이보다 크지 않습니다.

Given a head node of a singly linked list, remove the Nth last element and return the head node.

예제)

Input: 1->2->3->4->5, N=2
Output: 1->2->3->5

Input: 1->2->3, N=3
Output: 2->3

Input: 1, N=1
Output: null

``` javascript
class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

class LinkedList {
  constructor(input) {
    this.head = null;
    if (input) {
      input.split('->').forEach(value => this.add(value));
    }
  }

  add(value) {
    if (this.head) {
      let nodePtr = this.head;
      while (nodePtr.next) {
        nodePtr = nodePtr.next;
      }
      nodePtr.next = new Node(value);
    } else {
      this.head = new Node(value);
    }
  }

  toString() {
    const values = [];
    let nodePtr = this.head;
    while (nodePtr) {
      values.push(nodePtr.value);
      nodePtr = nodePtr.next;
    }
    return values.join('->');
  }
}

function solve(list, n) {
  let fast = list.head;
  let slow = list.head;

  let idx = 0;
  while (idx < n) {
    fast = fast.next;
    idx += 1;
  }

  if (fast === null) {
    list.head = list.head.next;
    return list.head ? `${list}` : null;
  }

  while (fast.next !== null) {
    fast = fast.next;
    slow = slow.next;
  }
  slow.next = slow.next.next;

  return list.head ? `${list}` : null;
}

const data = [
  { input: '1->2->3->4->5', n: 2, expected: '1->2->3->5' },
  { input: '1->2->3', n: 3, expected: '2->3' },
  { input: '1', n: 1, expected: null },
];

data.forEach(({input, n, expected}) => {
  const linkedList = new LinkedList(input);
  const actual = solve(linkedList, n);
  if (actual !== expected) {
    throw new Error('wrong answer');
  }
});
```