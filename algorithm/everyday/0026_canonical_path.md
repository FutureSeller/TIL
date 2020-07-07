# Get Canonical Path

"./"과 "../" 이 포함된 파일 경로를 "./"과 "../"이 없는 유닉스 파일 경로로 바꾸시오.

"./"는 현재의 위치를 뜻하고, "../"는 상위 디렉토리를 뜻합니다.


Given a file path containing "./" and "../", 
convert the path to a unix standard file path that does not contain "./" and "../".

```
input: "/usr/bin/../"
output: "/usr/"

input: "/usr/./bin/./test/../"
output: "/usr/bin/"
```

```javascript
function solve(input) {
  const result = []
  const subpaths = input.split('/')

  for (const subpath of subpaths) {
    if (result.length > 0 && subpath === '..') {
      result.pop()
    } else if (subpath !== '.' && subpath !== '..' && subpath !== '') {
      result.push(subpath)
    }
  }

  return '/' + result.join('/')
}

const data = [
  { input: '/usr/bin/../', expected: '/usr' },
  { input: '/usr/./bin/./test/../', expected: '/usr/bin' },
  { input: '/tmp/../tmp/../tmp', expected: '/tmp' },
  { input: '/home//foo/', expected: '/home/foo' },
  { input: '/a/./b/../../c/', expected: '/c' },
  { input: '/a//b////c/d//././/..', expected: '/a/b/c' },
  { input: '/...', expected: '/...' },
  { input: '//home', expected: '/home' },
  { input: '/.', expected: '/' },
  { input: '/..', expected: '/' },
]

data.forEach(({ input, expected }) => {
  const actual = solve(input)
  if (actual !== expected) {
    throw new Error('wrong answer')
  }
})

```
