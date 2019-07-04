# TIL
Today I Learned

## 작성 규칙
- 문서 생성은 [GFM (Github Flavored Markdown)](https://help.github.com/articles/github-flavored-markdown/) 을 사용한다.
  - 확장자 `.md`
  - column은 120을 넘지 않도록 한다.
  - `tab`을 사용하지 않고 `space`를 사용한다. (현재 tab == 2 spaces를 유지 중)
  - 예외
    - grave accent 내부에 작성된 내용은 스크롤이 되므로 예외로 둔다. (되도록 지킬 것)
- 언어나 기술명으로 Directory를 만든다. 
  - root에 문서를 만들지 않는다.
  - Sub directory를 만들지 않는다.
- 파일명은 영어로 만든다.
- commit은 다음과 같은 format으로 작성한다. 
  - date: yyyymmdd
  - dirname: 현재 문서가 위치한 dirname. root일 경우 empty
  - msg: commit message
  - format: `[${date}:${dirname}] ${msg}`
  - example
    - @args(date=20190701, dirname=algorithm, msg="merge sort") → `[20190701:algorithm] merge sort`
    - @args(date=20190701, dirname= , msg="update README.md") → `[20190701] update README.md`
