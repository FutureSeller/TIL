## Find the closest distance between two given points
0과 1로 만들어진 2D 정수 배열이 있습니다. 
0은 장애물이고 1은 도로일때, 두 좌표가 주어지면, 첫번째 좌표에서 두번째 좌표까지 가장 가까운 거리를 구하시오. 
두 좌표는 모두 도로에서 시작되고 좌, 우, 아래, 위로 움직이며 대각선으로는 움직일 수 없습니다. 
만약 갈 수 없다면 -1을 리턴하시오.

Given a 2D array with 0s and 1s, 0 represents an obstacle and 1 represents a road. 
Find the closest distance between two given points. 
You must only move up down right left. 
You cannot move through an obstacle.

``` javascript
/*
예제)
Input:
[
 [1, 0, 0, 1, 1, 0],
 [1, 0, 0, 1, 0, 0],
 [1, 1, 1, 1, 0, 0],
 [1, 0, 0, 0, 0, 1],
 [1, 1, 1, 1, 1, 1],
]

Start: [0, 0]
Finish: [0, 4]
Output: 8
*/

const isValidEntry = (maze, [i, j]) => maze && maze[i][j]
const idx2Val = ([i, j], col) => ((i * col) + j)

const moveLeft = ([i, j]) => (j < 1 ? [] : [i, j-1])
const moveRight = ([i, j], col) => (j >= col-1 ? [] : [i, j+1])
const moveTop = ([i, j]) => (i < 1 ? [] : [i-1, j])
const moveBottom = ([i, j], row) => (i >= row-1 ? [] : [i+1, j])

const getPoints = (point, row, col) => {
  const points = [
    moveLeft(point), 
    moveRight(point, col),
    moveTop(point), 
    moveBottom(point, row),
  ]
  return points.filter(point => point.length)
}

// Assumption: all inputs are always valid
function solve({maze, start, finish}) {
  if (!isValidEntry(maze, start)) {
    return -1
  }

  const ROW = maze.length
  const COL = maze[0].length
  const finishValue = idx2Val(finish, COL)
  const queue = [{ 
    raw: start, 
    val: idx2Val(start, COL), 
    path: [idx2Val(start, COL)],
  }]

  while (queue.length) {
    const directions = queue.length
    for (let i = 0; i < directions; i += 1) {
      const { raw, val, path } = queue.shift()
      if (val === finishValue) {
        return path.length - 1
      }
      getPoints(raw, ROW, COL)
        .filter(point => (
          isValidEntry(maze, point) && !path.includes(idx2Val(point, COL))
        ))
        .map(point => ({ 
          raw: point, 
          val: idx2Val(point, COL),
          path: path.concat(idx2Val(point, COL)),
        }))
        .forEach(point => queue.push(point))
    }
  }
  return -1
}

const data = [
  {
    maze: [
      [1, 0, 0, 1, 1, 0],
      [1, 0, 0, 1, 0, 0],
      [1, 1, 1, 1, 0, 0],
      [1, 0, 0, 0, 0, 1],
      [1, 1, 1, 1, 1, 1],
    ],
    start: [0,0],
    finish: [0,4],
    expected: 8,
  },
  {
    maze: [
      [1, 0, 0, 1, 1, 0],
      [1, 0, 0, 1, 0, 0],
      [1, 1, 1, 1, 0, 0],
      [1, 0, 0, 0, 0, 1],
      [1, 1, 1, 1, 1, 1],
    ],
    start: [0,0],
    finish: [3,5],
    expected: 10,
  },
  {
    maze: [[0,1]],
    start: [0,0],
    finish: [0,1],
    expected: -1,
  },
  {
    maze: [[1,0]],
    start: [0,0],
    finish: [0,1],
    expected: -1,
  },
]

data.forEach(({expected, ...data}) => {
  const actual = solve(data)
  if (actual !== expected) {
    throw new Error('wrong answer')
  }
})
```