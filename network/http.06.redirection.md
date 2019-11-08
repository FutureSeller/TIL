# Redirection

> URL 리다이렉션 혹은 URL 포워딩은 페이지 따위의 실제 리소스, 폼 혹은 전체 웹 애플리케이션이 다른 URL에 위치하고 있는 상태에서 링크를 존속시키는 기술

### Why?
- 사이트 유지보수가 진행되고 있는 상태에서 일시적인 리다이렉션
- 사이트 아키텍쳐 변경 이 후, 외부 링크를 동작하는 상태로 유지 등등

### HTTP 리다이렉션
- 요청에 대해 `3xx` 상태 코드를 지닌 응답
- 사용자에게는 invisible, 적은 성능 저하를 일으킴

#### 영속적인 리다이렉션
- 원래의 URL이 더 이상 사용되지 않고 새로운 URL
- 검색 엔진 bot 들에게 indexing 갱신 유발
- `301: Moved Permanently`
- `302: Permanent Redirect`

#### 일시적인 리다이렉션
- 검색 엔진 bot들에게 의미 없음
- `302: Found`
- `303: See Other`
- `307: Temporary Redirect`

#### 특수 리다이렉션
- `300: Multiple Choice` : 수동 리다이렉션. 가능한 것들을 나열. 사용자가 선택해야함
- `304: Not Modified`: 로컬에 캐시된 복사본으로 페이지를 리다이렉트

### 대체 방법
- HTML 리다이렉션: `<meta>`
  -`<meta http-equiv="refresh" content="0;URL='http://www.example.com/'" />`
  - `content=0;URL='http://www....`
    - 리다이렉트하기 전 얼마만큼의 시간을 기다려야하는 지 숫자로 나타냄
    - 더 나은 접근성을 위해 0으로 설정
  - 뒤로가기 버튼을 무효화
- 자바스크립트 리다이렉션
  - `window.location = "http://www.example.com"`

### 우선순위
- HTTP > HTML > 자바스크립트

---
## Reference
- https://developer.mozilla.org/ko/docs/Web/HTTP/Redirections