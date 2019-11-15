이것도 자꾸 까먹어서 오랜만에 Node.js 모듈을 작성할 기회가 생겨서 기록해놓는다.

Node.js로 간단한 모듈을 작성할 때, `require.main`을 사용하여 간단하게 결과를 볼 수 있다.

python의 `__name__ == '__main__'`과 동일한 효과를 볼 수 있다.

**물론 나중에 테스트 코드를 작성하면 더 좋다.**

``` javascript
// module.js

const scrap = (html) => {
  const $ = cheerio.load(html)
  .....
  .....
  return ...
}

if (module === require.main) {
  const html = fs.readFileSync(.....)
  scrap(html)
} else {
  module.exports = { ..., scrap }
}


```
