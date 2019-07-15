코드를 읽다보니 거의 모든 `package.json`에 `semver`가 있었다.
`semver`는 도대체 무엇일까?

- semver = Semantic Versioning
- 버전 형식에 의미를 부여하여 좀 더 체계적인 버전 관리를 하고자 함
- 형식
  - Major.Minor.Patch
  - Major: 호환 불가능한 API 변경 
  - Minor: 이전 버전과 호환 되면서 기능 update
  - Patch: 버그 수정
- Versioning만을 참고하여 호환성을 고려한 버그/취약점에 대해 대응할 수 있음

---
## Reference
- https://www.npmjs.com/package/semver
- https://github.com/npm/node-semver
- https://semver.org/
