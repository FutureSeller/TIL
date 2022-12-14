# Implement a queue using stacks

스택(Stack)을 이용해서 큐(Queue)를 구현하시오.

```javascript
class Queue {
  constructor() {
    this.stack1 = []
    this.stack2 = []
  }

  enqueue(value) {
    this.stack1.push(value)
  }

  dequeue() {
    while(this.stack1.length > 0) {
      this.stack2.push(this.stack1.pop())
    }

    const value = this.stack2.pop()

    while(this.stack2.length > 0) {
      this.stack1.push(this.stack2.pop())
    }

    return value
  }

  size() {
    return this.stack1.length
  }
}

const queue = new Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)

while(queue.size() > 0) {
  console.log(queue.size(), queue.dequeue())
}
```
