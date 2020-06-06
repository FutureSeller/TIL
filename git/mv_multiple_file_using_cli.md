TIL의 파일들을 directory를 만들고 하위에 파일들을 옮기는 작업을 하고 있었는데, 일일이 하기에는 너무 귀찮은 일이다.

그래서 방법들을 찾다보니 아래와 같은 방법이 있었다.

General한 방법은 아래와 같다.

```bash
for file in $(git ls-files | grep %filenamematch% | sed -e 's/\(%filenamematch%[^/]*\).*/\1/' | uniq); git mv $file $(echo $file | sed -e 's/%filenamematch%/%replacement%/')
```

실제로 `algorithm/leetcode_blahblah.md`에 해당하는 파일들을
`algorithm/leetcode` 디렉토리를 생성한 후, `blahblah.md`를 하위에 옮기고자한다.

```bash
mkdir -p algorithm/leetcode

for file in $(git ls-files); git mv $file $(echo $file | sed -e 's/leetcode_//');
```

---

## Reference

- https://stackoverflow.com/questions/9984722/git-rename-many-files-and-folders
