## Merge the two linked lists
두개의 정렬된(sorted) 정수 링크드리스트(linked list)가 주어지면, 두 리스트를 합친 정렬된 링크드리스트를 만드시오.

Given two sorted integer linked lists, merge the two linked lists. Merged linked list must also be sorted.

예제)

Input: 1->2->3, 1->2->3
Output: 1->1->2->2->3->3

Input: 1->3->5->6, 2->4
Output: 1->2->3->4->5->6

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

function solve(l1, l2) {
  let l1Head = l1.head;
  let l2Head = l2.head;

  const result = new LinkedList();

  while (l1Head && l2Head) {
    if (l1Head.value > l2Head.value) {
      result.add(l2Head.value);
      l2Head = l2Head.next;
    } else {
      result.add(l1Head.value);
      l1Head = l1Head.next;
    }
  }

  while (l1Head) {
    result.add(l1Head.value);
    l1Head = l1Head.next;
  }

  while (l2Head) {
    result.add(l2Head.value);
    l2Head = l2Head.next;
  }

  return result.toString();
}

const data = [
  { l1: '1->2->3', l2: '1->2->3', expected: '1->1->2->2->3->3' },
  { l1: '1->3->5->6', l2: '2->4', expected: '1->2->3->4->5->6' },
  { l1: '1->2->3', l2: '', expected: '1->2->3' },
  { l1: '', l2: '', expected: '' }
];

data.forEach(({l1, l2, expected}) => {
  const list1 = new LinkedList(l1);
  const list2 = new LinkedList(l2);

  const actual = solve(list1, list2);
  if (actual !== expected) {
    throw new Error('wrong answer');
  }
});
```