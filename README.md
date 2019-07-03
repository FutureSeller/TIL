# TIL
Today I Learned

## 작성 규칙
- 문서 생성은 [GFM (Github Flavored Markdown)](https://help.github.com/articles/github-flavored-markdown/) 을 사용한다. (확장자 `.md`)
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
