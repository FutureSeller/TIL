# TIL
Today I Learned

## 작성 규칙

### Name
- 모든 파일과 디렉토리 명은 영어로 만든다.
- space가 필요한 경우 `_`를 사용한다.
- 디렉토리: 언어, 기술명, 주제등을 사용한다.
- 파일: 해당 문서를 읽지않고도 무엇에 대한 문서인지 알 수 있도록 명명한다.

### Document
- [GFM (Github Flavored Markdown)](https://help.github.com/articles/github-flavored-markdown/)을 사용(확장자 `.md`)
- column: max 120
- indentation: two-spaces
- 예외: grave accent 내부에 작성된 내용은 스크롤이 되므로 예외로 둔다. (되도록 지킬 것)

### Commit
- format: `[${date}:${dirname}] ${msg}`
- date: yyyymmdd; 시차가 날 경우, 현지 시간을 따른다
- dirname: 현재 문서가 위치한 dirname. root일 경우 empty
- msg: commit message. 점진적인 update 필요 시, `..ing`를 뒤에 붙임
- example
  - @args(date=20190701, dirname=algorithm, msg="merge sort") → `[20190701:algorithm] merge sort`
  - @args(date=20190701, dirname= , msg="update README.md") → `[20190701] update README.md`
  - @args(date=20190701, dirname=react , msg="CRA ..ing") → `[20190701:react] CRA ..ing`

## Reference
- [JayJin님의 TIL](https://github.com/milooy/TIL)
