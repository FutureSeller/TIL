## Find the sum of all even fibonacci numbers
피보나치 배열은 0과 1로 시작하며,
다음 피보나치 수는 바로 앞의 두 피보나치 수의 합이 된다.
정수 N이 주어지면, N보다 작은 모든 짝수 피보나치 수의 합을 구하여라.

Fibonacci sequence starts with 0 and 1
where each fibonacci number is a sum of two previous fibonacci numbers.
Given an integer N, find the sum of all even fibonacci numbers.

예제)
Input: N = 12
Output: 10 // 0, 1, 2, 3, 5, 8 중 짝수인 2 + 8 = 10.

``` javascript
function firstTrial(N) {
  if (N < 2) {
    return 0;
  }

  let fn1 = 0;
  let fn2 = 1;
  let fn3 = fn1 + fn2;
  let sum = 0;
  while(fn3 <= N) {
    if (fn3 % 2 === 0) sum += fn3;
    fn1 = fn2;
    fn2 = fn3;
    fn3 = fn1 + fn2;
  }
  return sum;
}

/*
   0       3       6         9          12
  [0] 1 1 [2] 3 5 [8] 13 21 [34] 55 89 [144]

  if N = 0: return 0
  if N = 1: return 2
  F(3N) = 4 * F(3(N-1)) + F(3(N-2))
*/
function secondTrial(N) {
  if (N < 2) {
    return 0;
  }
  let fn1 = 0;
  let fn2 = sum = 2;
  let fn3 = 4 * fn2 + fn1;
  while (fn3 <= N) {
    sum += fn3;
    fn1 = fn2;
    fn2 = fn3;
    fn3 = 4 * fn2 + fn1;
  }
  return sum;
}

// 144: [0] 1 1 [2] 3 5 [8] 13 21 [34] 55 89 [144] = 188
console.time('1stTrial');
console.log(firstTrial(144));
console.timeEnd('1stTrial');

console.time('2ndTrial');
console.log(secondTrial(144));
console.timeEnd('2ndTrial');

/*
188
1stTrial: 3.140ms
188
2ndTrial: 0.298ms
*/
```
