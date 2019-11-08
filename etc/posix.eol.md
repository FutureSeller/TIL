JS 스터디의 코드 리뷰를 보던 중, 아래와 같은 문구를 보게되었다.

> 전체적으로 end of line이 없는 것 같습니다. 
> File의 EOL은 POSIX환경에서 정해놓은 일종의 명세이니 지켜주시면 좋습니다.

예전부터 궁금한 점이였지만, 굳이 찾아보지 않고 마지막 개행을 지웠다.
생각해보니 마지막 줄 개행을 추가해준 이유가 있을 거라 뒤늦게 리뷰를 보고 깨달았다.

## 파일 끝에 개행을 추가해야 하는 이유
- POSIX 명세가 그러하다
  - [Text File](https://pubs.opengroup.org/onlinepubs/000095399/basedefs/xbd_chap03.html#tag_03_392)
  - [Line](https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap03.html#tag_03_206)
  - 종합해보면 Text File은 행의 집합 + 행의 끝은 EOL
- 잠재적인 문제가 될 수 있다 - OS에 따라.
  - OS에 따라 다른 개행문자로 인해, 텍스트 줄바꿈이 하나도 안되는 경우가 있을 수 있음 (e.g., `\n` vs. `\r\n`)
  - 협업. 대표적으로 git: 개발환경에 따라 개행으로 인해 의미 없는 diff 혹은 conflict가 생길 수 있음

---
## Reference
- https://stackoverflow.com/questions/729692/why-should-text-files-end-with-a-newline
- https://blog.coderifleman.com/2015/04/04/text-files-end-with-a-newline
- https://velog.io/@doondoony/posix-eol
- https://help.github.com/en/github/using-git/configuring-git-to-handle-line-endings