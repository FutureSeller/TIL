## Print all elements in a circular spiral shape starting from [0][0].
2차 정수 배열(2D int array)가 주어지면, 소용돌이 모양으로 원소들을 프린트하시오. 예제를 보시오.

Given a 2D integer array, print all elements in a circular spiral shape starting from [0][0]. See example.

```
예제)

input:
[[1, 2, 3],
[8, 9, 4],
[7, 6, 5]]

Output:
1, 2, 3, 4, 5, 6, 7, 8, 9
```

``` javascript
const LEFT_TO_RIGHT = 0
const TOP_TO_BOTTOM = 1
const RIGHT_TO_LEFT = 2
const BOTTOM_TO_TOP = 3

function update(input, state) {
  const { direction } = state
  const result = []
  switch (direction) {
    case LEFT_TO_RIGHT: {
      let { minRow, minCol, maxCol } = state
      for (; minCol <= maxCol; minCol += 1) {
        result.push(input[minRow][minCol])
      }
      break
    }
    case TOP_TO_BOTTOM: {
      let { minRow, maxRow, maxCol } = state
      for (; minRow <= maxRow; minRow += 1) {
        result.push(input[minRow][maxCol])
      }
      break
    }
    case RIGHT_TO_LEFT: {
      let { maxRow, minCol, maxCol } = state
      for (; maxCol >= minCol; maxCol -= 1) {
        result.push(input[maxRow][maxCol])
      }
      break
    }
    case BOTTOM_TO_TOP: {
      let { minRow, maxRow, minCol } = state
      for (; maxRow >= minRow; maxRow -= 1) {
        result.push(input[maxRow][minCol])
      }
      break
    }
  }
  return result
}

function solve(input) {
  const result = []
  const row = input.length
  const col = input[0].length
  let state = {
    direction: LEFT_TO_RIGHT,
    minRow: 0,
    maxRow: row - 1,
    minCol: 0,
    maxCol: col - 1,
  }

  while (result.length < row * col) {
    // left to right
    result.push.apply(result, update(input, state))
    state = {
      ...state,
      direction: TOP_TO_BOTTOM,
      minRow: state.minRow + 1,
    }

    // top to bottom
    result.push.apply(result, update(input, state))
    state = {
      ...state,
      direction: RIGHT_TO_LEFT,
      maxCol: state.maxCol - 1,
    }

    // right to left
    result.push.apply(result, update(input, state))
    state = {
      ...state,
      direction: BOTTOM_TO_TOP,
      maxRow: state.maxRow - 1,
    }

    // bottom to top
    result.push.apply(result, update(input, state))
    state = {
      ...state,
      direction: LEFT_TO_RIGHT,
      minCol: state.minCol + 1,
    }
  }
  return result.join(',')
}

const data = [
  { 
    input: [
      [1, 2, 3],
      [8, 9, 4],
      [7, 6, 5],
    ], 
    expected: [1,2,3,4,5,6,7,8,9].join(','),
  },
  {
    input: [[3,2,1]],
    expected: [3,2,1].join(','),
  },
  {
    input: [
      [1, 2, 3, 4],
      [10, 11, 12, 5],
      [9, 8, 7, 6],
    ],
    expected: [1,2,3,4,5,6,7,8,9,10,11,12].join(','),
  },
  {
    input: [[1],[2],[3],[4]],
    expected: [1,2,3,4].join(','),
  }
]

data.forEach(({input, expected}) => {
  const actual = solve(input)
  if (actual !== expected) {
    new Error('wrong answer')
  }
})
```