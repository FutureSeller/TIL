# N+1 Problem (Database)
- 쿼리 1번으로 N건을 가져왔는데, 관련 컬럼을 얻기 위해 쿼리를 N번 추가 수행하는 문제
- 쿼리결과 건수마다 참조 정보를 얻기 위해 건수만큼 반복해서 쿼리를 수행하게 되는 문제

```javascript
const books = async exec('SELECT * FROM books');
for await (const book of books) {
  const [author] = async exec(`SELECT name FROM authors WHERE id = ${book.author}`)
}
```

### 해결 방법
- eager 로딩
  - 위의 예제코드를 lazy loading, 실제로 필요할 때 하나씩 로딩
  - eager는 일단 data를 로딩해놓고 데이터에 접근하는 방식

  ```javascript
  const books = async exec('SELECT * FROM books');
  const authors = async exec('SELECT * FROM authors')
  for (const book of books) {
    const author = authors[book.author]
  }
  ```
  
  - Batching Queries라고도 하는 듯 함. Load all data before iterating through it

- JOIN
```javascript
const results = async exec(`
  SELECT b.*, a.author FROM books b LEFT JOIN a ON b.author=a.id
`);
```

---
## Reference
- https://zetawiki.com/wiki/N%2B1_%EC%BF%BC%EB%A6%AC_%EB%AC%B8%EC%A0%9C
- https://secure.phabricator.com/book/phabcontrib/article/n_plus_one/
